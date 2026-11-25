import { Layers } from "lucide-react";
import { Badge } from "@/components/ui/badge";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

export function DepartmentsOverview() {
  return (
    <div className="space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-3">
        <div className="flex items-center gap-3">
          <Layers className="h-6 w-6 text-primary" />
          <div>
            <h1 className="text-2xl font-semibold tracking-tight">Departments</h1>
            <p className="text-sm text-muted-foreground">
              Structure engineering divisions, leadership roles, and budgets.
            </p>
          </div>
        </div>
        <Badge variant="outline">API: /api/v1/departments</Badge>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Department Structure</CardTitle>
          <CardDescription>
            Group teams under specialized engineering departments.
          </CardDescription>
        </CardHeader>
        <CardContent className="text-sm text-muted-foreground">
          Define Platform, Product, QA, and Security departments with assigned heads.
        </CardContent>
      </Card>
    </div>
  );
}
