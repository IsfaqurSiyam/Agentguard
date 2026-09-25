import Link from "next/link";

const navigation = [
  ["Dashboard", "/dashboard"], ["Agents", "/agents"], ["Tools", "/tools"],
  ["Policies", "/policies"], ["Activity", "/activity"], ["Incidents", "/incidents"],
  ["Approvals", "/approvals"], ["Settings", "/settings"],
] as const;

export function ConsoleShell({ title, children }: { title: string; children: React.ReactNode }) {
  return <div className="min-h-screen md:grid md:grid-cols-[15rem_1fr]">
    <aside className="border-b border-slate-700 bg-slate-950 p-5 md:border-b-0 md:border-r">
      <Link href="/dashboard" className="text-lg font-bold tracking-tight">AgentGuard</Link>
      <p className="mt-1 text-xs text-slate-400">Operator console · Phase 1</p>
      <nav aria-label="Primary navigation" className="mt-6 flex flex-wrap gap-2 md:flex-col">
        {navigation.map(([label, href]) => <Link key={href} href={href} className="rounded px-3 py-2 text-sm text-slate-300 hover:bg-slate-800 hover:text-white">{label}</Link>)}
      </nav>
    </aside>
    <main className="p-6 md:p-10"><h1 className="text-2xl font-semibold">{title}</h1>{children}</main>
  </div>;
}
