import { ModulePlaceholder } from "@/components/layout/module-placeholder";

export default function CodeWorkspacePage() {
  return (
    <ModulePlaceholder
      title="Code Workspace"
      description="Isolated Docker-sandboxed coding environment with GitHub integration."
      phase="Phase 5"
      capabilities={[
        "GitHub repository indexing & analysis",
        "Sandboxed file edits & test generation",
        "Automated code review & bug fixing",
        "Branch creation & PR preparation",
      ]}
    />
  );
}
