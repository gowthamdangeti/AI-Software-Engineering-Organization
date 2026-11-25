import { ModulePlaceholder } from "@/components/layout/module-placeholder";

export default function ProvidersPage() {
  return (
    <ModulePlaceholder
      title="API Keys & Providers"
      description="Fernet-encrypted LLM provider credentials and model routing configuration."
      phase="Phase 2"
      capabilities={[
        "OpenAI, Anthropic, Gemini, Groq, DeepSeek, OpenRouter",
        "Custom OpenAI-compatible endpoints",
        "Fernet-encrypted key storage",
        "Per-employee model assignment",
      ]}
    />
  );
}
