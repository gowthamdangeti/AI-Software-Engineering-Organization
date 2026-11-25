import { BarChart3 } from "lucide-react";
import { Badge } from "@/components/ui/badge";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

export function AnalyticsOverview() {
  return (
    <div className="space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-3">
        <div className="flex items-center gap-3">
          <BarChart3 className="h-6 w-6 text-primary" />
          <div>
            <h1 className="text-2xl font-semibold tracking-tight">Analytics</h1>
            <p className="text-sm text-muted-foreground">
              Observe throughput, token spend, task completion velocity, and SLA metrics.
            </p>
          </div>
        </div>
        <Badge variant="outline">Telemetry &amp; Cost</Badge>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Organization Metrics</CardTitle>
          <CardDescription>
            Real-time operational insights across departments, teams, and AI employees.
          </CardDescription>
        </CardHeader>
        <CardContent className="text-sm text-muted-foreground">
          Track LLM usage, cycle time, and workflow success rates per project.
        </CardContent>
      </Card>
    </div>
  );
}
