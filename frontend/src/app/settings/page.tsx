import { ModulePlaceholder } from "@/components/layout/module-placeholder";

export default function SettingsPage() {
  return (
    <ModulePlaceholder
      title="Settings"
      description="Workspace preferences, authentication, and security policies."
      phase="Phase 1"
      capabilities={[
        "JWT & refresh token settings",
        "Organization RBAC policies",
        "Rate limiting & execution limits",
        "Theme & UI preferences",
      ]}
    />
  );
}
