import { Badge } from "@/components/ui/badge";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

interface ModulePlaceholderProps {
  title: string;
  description: string;
  phase: string;
  capabilities: string[];
}

export function ModulePlaceholder({
  title,
  description,
  phase,
  capabilities,
}: ModulePlaceholderProps) {
  return (
    <div className="space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-3">
        <div>
          <h1 className="text-2xl font-semibold tracking-tight">{title}</h1>
          <p className="text-sm text-muted-foreground mt-1">{description}</p>
        </div>
        <Badge variant="outline">Scheduled: {phase}</Badge>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Module Scope</CardTitle>
          <CardDescription>
            This module route is initialized in Phase 0 and will be connected to
            live PostgreSQL, Redis, and FastAPI services in {phase}.
          </CardDescription>
        </CardHeader>
        <CardContent>
          <ul className="grid gap-2 sm:grid-cols-2 text-sm text-muted-foreground">
            {capabilities.map((cap) => (
              <li key={cap} className="rounded-md border px-3 py-2">
                {cap}
              </li>
            ))}
          </ul>
        </CardContent>
      </Card>
    </div>
  );
}
