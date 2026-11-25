from dataclasses import dataclass, field
from typing import Any, Protocol
from uuid import UUID


@dataclass(slots=True)
class AgentContext:
    """Execution context passed to an AI employee runtime."""

    employee_id: UUID
    organization_id: UUID
    task_id: UUID
    model_provider: str
    model_name: str
    system_prompt: str = ""
    tools: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class AgentResult:
    """Structured output returned by an AI employee run."""

    success: bool
    output: str
    artifacts: list[str] = field(default_factory=list)
    usage: dict[str, int] = field(default_factory=dict)


class AgentRunner(Protocol):
    """Protocol for executing an AI employee against a task."""

    async def run(self, context: AgentContext, prompt: str) -> AgentResult: ...
