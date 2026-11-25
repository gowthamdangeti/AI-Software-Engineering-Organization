from collections.abc import Awaitable, Callable
from dataclasses import dataclass
from typing import Any


ToolHandler = Callable[..., Awaitable[Any]]


@dataclass(frozen=True, slots=True)
class ToolDefinition:
    """Metadata and handler for a tool callable by AI employees."""

    name: str
    description: str
    handler: ToolHandler


class ToolRegistry:
    """Registry of tools available to AI employee runtimes."""

    def __init__(self) -> None:
        self._tools: dict[str, ToolDefinition] = {}

    def register(self, tool: ToolDefinition) -> None:
        self._tools[tool.name] = tool

    def get(self, name: str) -> ToolDefinition | None:
        return self._tools.get(name)

    def list_names(self) -> list[str]:
        return sorted(self._tools.keys())


default_tool_registry = ToolRegistry()
