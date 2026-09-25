export function EmptyState({ children }: { children: React.ReactNode }) {
  return <section className="mt-6 rounded-lg border border-dashed border-slate-600 bg-slate-900/60 p-8 text-slate-300"><p>{children}</p></section>;
}
