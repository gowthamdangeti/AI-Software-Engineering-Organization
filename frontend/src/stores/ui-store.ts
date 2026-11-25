import { create } from "zustand";

export type ThemeMode = "light" | "dark";

interface UiState {
  sidebarCollapsed: boolean;
  mobileMenuOpen: boolean;
  theme: ThemeMode;
  toggleSidebar: () => void;
  setMobileMenuOpen: (open: boolean) => void;
  setTheme: (theme: ThemeMode) => void;
  toggleTheme: () => void;
}

export const useUiStore = create<UiState>((set) => ({
  sidebarCollapsed: false,
  mobileMenuOpen: false,
  theme: "dark",
  toggleSidebar: () => set((state) => ({ sidebarCollapsed: !state.sidebarCollapsed })),
  setMobileMenuOpen: (open) => set({ mobileMenuOpen: open }),
  setTheme: (theme) => set({ theme }),
  toggleTheme: () =>
    set((state) => ({ theme: state.theme === "dark" ? "light" : "dark" })),
}));
