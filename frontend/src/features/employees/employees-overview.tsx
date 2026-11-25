import { Bot } from "lucide-react";
import { Badge } from "@/components/ui/badge";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

export function EmployeesOverview() {
  return (
    <div className="space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-3">
        <div className="flex items-center gap-3">
          <Bot className="h-6 w-6 text-primary" />
          <div>
            <h1 className="text-2xl font-semibold tracking-tight">AI Employees</h1>
            <p className="text-sm text-muted-foreground">
              Configure autonomous AI engineers, managers, reviewers, and model bindings.
            </p>
          </div>
        </div>
        <Badge variant="outline">API: /api/v1/employees</Badge>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Agent Roster</CardTitle>
          <CardDescription>
            Each AI employee has a role, seniority, reporting manager, and LLM configuration.
          </CardDescription>
        </CardHeader>
        <CardContent className="text-sm text-muted-foreground">
          Manage system prompts, tool permissions, and runtime status for every AI employee.
        </CardContent>
      </Card>
    </div>
  );
}
