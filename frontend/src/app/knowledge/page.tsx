import { ModulePlaceholder } from "@/components/layout/module-placeholder";

export default function KnowledgePage() {
  return (
    <ModulePlaceholder
      title="Knowledge"
      description="Organization, department, and project knowledge bases backed by pgvector."
      phase="Phase 2"
      capabilities={[
        "pgvector semantic retrieval",
        "Department & team knowledge sources",
        "Employee memory configuration",
        "Document ingestion via MinIO",
      ]}
    />
  );
}
