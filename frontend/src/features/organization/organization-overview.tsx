import { Building2 } from "lucide-react";
import { Badge } from "@/components/ui/badge";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

export function OrganizationOverview() {
  return (
    <div className="space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-3">
        <div className="flex items-center gap-3">
          <Building2 className="h-6 w-6 text-primary" />
          <div>
            <h1 className="text-2xl font-semibold tracking-tight">
              Engineering Organization
            </h1>
            <p className="text-sm text-muted-foreground">
              Manage virtual software engineering companies, tenants, and reporting hierarchies.
            </p>
          </div>
        </div>
        <Badge variant="outline">API: /api/v1/organizations</Badge>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Organization Directory</CardTitle>
          <CardDescription>
            Connected to PostgreSQL-backed organization endpoints.
          </CardDescription>
        </CardHeader>
        <CardContent className="text-sm text-muted-foreground">
          Create and manage isolated engineering organizations, reporting lines, and RBAC policies.
        </CardContent>
      </Card>
    </div>
  );
}
