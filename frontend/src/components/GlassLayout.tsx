import { Link } from "@tanstack/react-router";
import type { ReactNode } from "react";
import logoImg from "@/assets/1111.jpg";

const navItems = [
  { to: "/", label: "Overview" },
  { to: "/predictor", label: "Dahej Predictor" },
  { to: "/model", label: "Model Analytics" },
  { to: "/api", label: "API Architecture" },
] as const;

export function GlassLayout({ children }: { children: ReactNode }) {
  return (
    <div className="relative min-h-screen">
      <div
        className="orb h-[500px] w-[500px] -top-24 -left-24"
        style={{ background: "oklch(0.45 0.18 25 / 25%)" }}
        aria-hidden
      />
      <div
        className="orb h-[600px] w-[600px] -bottom-36 -right-24"
        style={{ background: "oklch(0.38 0.16 20 / 20%)" }}
        aria-hidden
      />
      <div
        className="orb h-[450px] w-[450px] top-[40%] left-[35%]"
        style={{ background: "oklch(0.50 0.15 30 / 18%)" }}
        aria-hidden
      />

      <div className="relative z-1 mx-auto max-w-[1440px] px-4 py-6 sm:px-6">
        <header className="glass glass-lift mb-7 flex flex-col gap-4 px-5 py-4 sm:px-8 lg:flex-row lg:items-center lg:justify-between">
          <Link to="/" className="flex items-center gap-3 group">
            <div className="relative flex h-11 w-11 items-center justify-center overflow-hidden rounded-[12px] border border-primary/40 shadow-[0_4px_14px_oklch(0.42_0.20_25/35%)] transition-transform group-hover:scale-105">
              <img
                src={logoImg}
                alt="Calculate my Dahej Logo"
                className="h-full w-full object-cover"
              />
            </div>
            <span className="text-xl font-extrabold tracking-tight">
              Calculate my <span className="text-primary">Dahej</span>
            </span>
          </Link>

          <nav className="glass-subtle flex flex-wrap gap-1 p-1.5">
            {navItems.map((item) => (
              <Link
                key={item.to}
                to={item.to}
                activeOptions={{ exact: item.to === "/" }}
                className="rounded-[10px] px-4 py-2.5 text-sm font-semibold transition-all"
                inactiveProps={{
                  className: "text-muted-foreground hover:bg-primary/10 hover:text-primary",
                }}
                activeProps={{
                  className:
                    "gradient-primary text-primary-foreground font-bold shadow-[0_2px_10px_oklch(0.42_0.20_25/35%)]",
                }}
              >
                {item.label}
              </Link>
            ))}
          </nav>
        </header>

        <main className="animate-in fade-in duration-500">{children}</main>

        <footer className="glass-subtle mt-8 flex flex-col gap-1 px-6 py-5 text-sm text-muted-foreground sm:flex-row sm:items-center sm:justify-between">
          <span>
            Ridge + NN Ensemble (equal weightage) · 400,000 synthetic records · 37 features
          </span>
          <span>Production R² ~0.758 · MAE ₹187,674 · RMSE ₹242,985</span>
        </footer>
      </div>
    </div>
  );
}

export function PageHeading({
  eyebrow,
  title,
  description,
}: {
  eyebrow: string;
  title: string;
  description: string;
}) {
  return (
    <div className="mb-6">
      <p className="label-caps text-primary">{eyebrow}</p>
      <h1 className="mt-2 text-3xl font-extrabold sm:text-4xl">{title}</h1>
      <p className="mt-2 max-w-3xl text-[0.975rem] text-muted-foreground">
        {description}
      </p>
    </div>
  );
}

export function HeroImage({ src, alt, className }: { src: string; alt: string; className?: string }) {
  return (
    <div className="mb-7 overflow-hidden rounded-[var(--radius-md)] border border-border shadow-[var(--glass-shadow-md)]">
      <img
        src={src}
        alt={alt}
        width={1600}
        height={900}
        className={`h-[340px] sm:h-[480px] w-full object-cover object-[center_15%] ${className || ""}`}
      />
    </div>
  );
}
