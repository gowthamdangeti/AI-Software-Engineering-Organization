import { GitBranch } from "lucide-react";
import { Badge } from "@/components/ui/badge";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

export function WorkflowsOverview() {
  return (
    <div className="space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-3">
        <div className="flex items-center gap-3">
          <GitBranch className="h-6 w-6 text-primary" />
          <div>
            <h1 className="text-2xl font-semibold tracking-tight">Workflows</h1>
            <p className="text-sm text-muted-foreground">
              Design and orchestrate multi-agent SDLC pipelines and approval gates.
            </p>
          </div>
        </div>
        <Badge variant="outline">API: /api/v1/workflows</Badge>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Orchestration Pipelines</CardTitle>
          <CardDescription>
            Visual DAG workflows powered by React Flow and the backend orchestration engine.
          </CardDescription>
        </CardHeader>
        <CardContent className="text-sm text-muted-foreground">
          Connect planning, coding, code review, testing, and deployment stages across teams.
        </CardContent>
      </Card>
    </div>
  );
}
