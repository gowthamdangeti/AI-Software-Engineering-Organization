import { Users } from "lucide-react";
import { Badge } from "@/components/ui/badge";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

export function TeamsOverview() {
  return (
    <div className="space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-3">
        <div className="flex items-center gap-3">
          <Users className="h-6 w-6 text-primary" />
          <div>
            <h1 className="text-2xl font-semibold tracking-tight">Teams</h1>
            <p className="text-sm text-muted-foreground">
              Organize cross-functional pods of AI engineers and team leads.
            </p>
          </div>
        </div>
        <Badge variant="outline">API: /api/v1/teams</Badge>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Engineering Teams</CardTitle>
          <CardDescription>
            Assign missions, team leads, and operational capacity per pod.
          </CardDescription>
        </CardHeader>
        <CardContent className="text-sm text-muted-foreground">
          Teams coordinate multi-agent collaboration across backend, frontend, and infrastructure tasks.
        </CardContent>
      </Card>
    </div>
  );
}
