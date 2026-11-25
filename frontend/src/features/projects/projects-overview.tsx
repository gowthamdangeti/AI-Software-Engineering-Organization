import { FolderGit2 } from "lucide-react";
import { Badge } from "@/components/ui/badge";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

export function ProjectsOverview() {
  return (
    <div className="space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-3">
        <div className="flex items-center gap-3">
          <FolderGit2 className="h-6 w-6 text-primary" />
          <div>
            <h1 className="text-2xl font-semibold tracking-tight">Projects</h1>
            <p className="text-sm text-muted-foreground">
              Manage software repositories, deliverables, and active engineering initiatives.
            </p>
          </div>
        </div>
        <Badge variant="outline">API: /api/v1/projects</Badge>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Active Repositories</CardTitle>
          <CardDescription>
            Track project health, linked repositories, and assigned engineering teams.
          </CardDescription>
        </CardHeader>
        <CardContent className="text-sm text-muted-foreground">
          Each project hosts tasks, workflow graphs, and execution artifacts stored in MinIO.
        </CardContent>
      </Card>
    </div>
  );
}
