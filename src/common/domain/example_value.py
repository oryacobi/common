from dataclasses import dataclass

from .exceptions import DomainValueError


@dataclass(frozen=True)
class ExampleValue:
    """Minimal example value object for demonstration and testing."""

    name: str

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise DomainValueError("name must be non-empty")

    def greeting(self) -> str:
        """Return a simple greeting that includes the configured name."""

        return f"Hello, {self.name}!"
