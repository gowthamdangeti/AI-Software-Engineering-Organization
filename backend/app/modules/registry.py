from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ModuleSpec:
    """Descriptor for a domain module in the modular monolith."""

    name: str
    description: str
    enabled: bool = True


CORE_MODULES: tuple[ModuleSpec, ...] = (
    ModuleSpec(name="organization", description="Organizations, departments, teams, and AI employees"),
    ModuleSpec(name="projects", description="Projects, tasks, and workflow definitions"),
    ModuleSpec(name="agent_runtime", description="AI employee execution runtime"),
    ModuleSpec(name="orchestration", description="Multi-agent workflow DAG orchestration"),
    ModuleSpec(name="analytics", description="Organization velocity and cost analytics"),
)
