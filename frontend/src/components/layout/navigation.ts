import {
  Activity,
  Bot,
  Boxes,
  Building2,
  CheckSquare,
  Code2,
  FolderKanban,
  GitBranch,
  KeyRound,
  LayoutDashboard,
  Library,
  Settings,
  ShieldCheck,
  Users,
  type LucideIcon,
} from "lucide-react";

export interface NavItem {
  label: string;
  href: string;
  icon: LucideIcon;
  phase: string;
}

export const NAV_ITEMS: NavItem[] = [
  { label: "Overview", href: "/", icon: LayoutDashboard, phase: "Phase 0" },
  {
    label: "Engineering Organization",
    href: "/organization",
    icon: Building2,
    phase: "Phase 1",
  },
  { label: "Departments", href: "/departments", icon: Boxes, phase: "Phase 1" },
  { label: "Teams", href: "/teams", icon: Users, phase: "Phase 1" },
  { label: "AI Employees", href: "/employees", icon: Bot, phase: "Phase 1" },
  { label: "Projects", href: "/projects", icon: FolderKanban, phase: "Phase 4" },
  { label: "Tasks", href: "/tasks", icon: CheckSquare, phase: "Phase 4" },
  { label: "Workflows", href: "/workflows", icon: GitBranch, phase: "Phase 4" },
  {
    label: "Code Workspace",
    href: "/code-workspace",
    icon: Code2,
    phase: "Phase 5",
  },
  { label: "Knowledge", href: "/knowledge", icon: Library, phase: "Phase 2" },
  { label: "Approvals", href: "/approvals", icon: ShieldCheck, phase: "Phase 4" },
  { label: "Analytics", href: "/analytics", icon: Activity, phase: "Phase 6" },
  {
    label: "API Keys & Providers",
    href: "/providers",
    icon: KeyRound,
    phase: "Phase 2",
  },
  { label: "Settings", href: "/settings", icon: Settings, phase: "Phase 1" },
];
