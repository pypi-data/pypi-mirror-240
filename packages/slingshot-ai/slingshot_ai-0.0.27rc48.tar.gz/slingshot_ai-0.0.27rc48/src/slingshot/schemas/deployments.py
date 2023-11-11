from abc import ABC
from typing import Annotated, Any, Literal, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel, model_validator
from typing_extensions import Self, override

from slingshot.sdk import backend_schemas
from slingshot.sdk.graphql import fragments

from ..sdk.errors import SlingshotException
from .components import AbstractComponentSpec
from .mixins import ComponentMountsMixin, ScriptBasedComponentMixin

STREAMING_TEXT_DEPLOYMENT_MODEL_MOUNT_PATH = '/mnt/model'


class AbstractDeploymentSpec(AbstractComponentSpec, ABC):
    model_config = ConfigDict(title="Deployment")
    using: Literal['custom', 'streaming-text'] = Field(
        ..., title="Using", description="The type of deployment to use, custom or streaming-text"
    )

    @override
    def diff(self, existing: fragments.ComponentSpec) -> list[str]:
        if existing.component_type != backend_schemas.ComponentType.DEPLOYMENT:
            raise ValueError(f"Cannot diff a run against a non-deployment.")

        return super().diff(existing)


class CustomDeploymentSpec(AbstractDeploymentSpec, ScriptBasedComponentMixin):
    """
    Deployment following a single request/response pattern per request, implemented with a custom Python handler.
    """

    using: Literal['custom'] = Field(
        ..., title="Using", description="The type of deployment to use, custom or streaming-text"
    )

    @override
    def diff(self, existing: fragments.ComponentSpec) -> list[str]:
        """Returns a list of differences between this and another app spec."""
        if (
            existing.deployment_sub_type is not None
            and existing.deployment_sub_type != backend_schemas.DeploymentSubType.CUSTOM
        ):
            raise ValueError(f"Cannot change the type of a deployment, remove and add it under a new name instead.")

        return super().diff(existing)


class StreamingTextDeploymentSpec(ComponentMountsMixin, AbstractDeploymentSpec):
    """Deployment backed by TGI as the engine, pointing to a trained model, no custom code."""

    using: Literal['streaming-text'] = Field(
        ..., title="Using", description="The type of deployment to use, custom or streaming-text"
    )

    @override
    def diff(self, existing: fragments.ComponentSpec) -> list[str]:
        if existing.deployment_sub_type != backend_schemas.DeploymentSubType.STREAMING_TEXT:
            raise ValueError(f"Cannot change the type of a deployment, remove and add it under a new name instead.")

        return super().diff(existing)

    @model_validator(mode="after")
    def validate_model_mounts(self) -> Self:
        if len(self.mounts) != 1:
            raise SlingshotException(
                "Streaming text deployments must contain exactly one mount for a model available at "
                f"'{STREAMING_TEXT_DEPLOYMENT_MODEL_MOUNT_PATH}'"
            )

        model_mount = self.mounts[0]
        if model_mount.path != STREAMING_TEXT_DEPLOYMENT_MODEL_MOUNT_PATH:
            raise SlingshotException(
                "Streaming text deployments must contain exactly one mount for a model available at "
                f"'{STREAMING_TEXT_DEPLOYMENT_MODEL_MOUNT_PATH}'"
            )
        if model_mount.mode not in ['DOWNLOAD', 'VOLUME']:
            raise SlingshotException("Mounts for streaming text models must support reads (download or volume)'")

        return self


DeploymentSpecUnion = Annotated[Union[CustomDeploymentSpec, StreamingTextDeploymentSpec], Field(discriminator='using'),]


class SafeDeploymentSpec(RootModel[DeploymentSpecUnion]):
    """
    Reads a deployment spec with extra validation for missing 'using'. Using a root model appears to be the only way to
    add validation before Pydantic picks the specific class to validate.
    """

    @model_validator(mode='before')
    @classmethod
    def default_sub_type_to_custom(cls, data: Any) -> Any:
        if isinstance(data, BaseModel):
            data = data.model_dump()

        if 'using' not in data or not data['using']:
            data['using'] = 'custom'

        return data
