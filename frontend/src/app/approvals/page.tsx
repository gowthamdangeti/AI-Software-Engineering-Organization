import { ModulePlaceholder } from "@/components/layout/module-placeholder";

export default function ApprovalsPage() {
  return (
    <ModulePlaceholder
      title="Approvals"
      description="Human-in-the-loop approval gates for sensitive operations and deployments."
      phase="Phase 4"
      capabilities={[
        "Pending approval queue",
        "Sensitive tool & PR gates",
        "Audit trail of decisions",
        "Resume blocked agent sessions",
      ]}
    />
  );
}
