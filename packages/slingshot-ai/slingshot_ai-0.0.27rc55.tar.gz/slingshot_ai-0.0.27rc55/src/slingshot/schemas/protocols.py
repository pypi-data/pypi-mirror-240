from abc import abstractmethod
from typing import Any, Protocol, runtime_checkable


@runtime_checkable
class HasAutoscalingParams(Protocol):
    @abstractmethod
    def get_min_replicas(self) -> int | None:
        ...

    @abstractmethod
    def get_max_replicas(self) -> int | None:
        ...


@runtime_checkable
class HasComponentConfig(Protocol):
    @abstractmethod
    def get_component_config(self) -> dict[str, Any]:
        ...
