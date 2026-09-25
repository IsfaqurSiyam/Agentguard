import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "AgentGuard",
  description: "Security gateway operator console",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return <html lang="en"><body>{children}</body></html>;
}
