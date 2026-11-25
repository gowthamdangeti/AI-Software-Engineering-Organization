import { CheckSquare } from "lucide-react";
import { Badge } from "@/components/ui/badge";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

export function TasksOverview() {
  return (
    <div className="space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-3">
        <div className="flex items-center gap-3">
          <CheckSquare className="h-6 w-6 text-primary" />
          <div>
            <h1 className="text-2xl font-semibold tracking-tight">Tasks</h1>
            <p className="text-sm text-muted-foreground">
              Track engineering tickets, subtasks, priorities, and AI employee assignments.
            </p>
          </div>
        </div>
        <Badge variant="outline">API: /api/v1/tasks</Badge>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Task Board</CardTitle>
          <CardDescription>
            Monitor backlog, in-progress, review, and completed engineering work items.
          </CardDescription>
        </CardHeader>
        <CardContent className="text-sm text-muted-foreground">
          Tasks can be decomposed into subtasks and dispatched to ARQ background workers.
        </CardContent>
      </Card>
    </div>
  );
}
