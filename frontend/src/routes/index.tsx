import { createFileRoute, Link } from "@tanstack/react-router";
import { useState } from "react";
import {
  ArrowRight,
  BarChart3,
  CheckCircle2,
  DollarSign,
  Layers,
  Lightbulb,
  PieChart,
  ShieldAlert,
  ShieldCheck,
  Sparkles,
  TrendingUp,
  Zap,
} from "lucide-react";

import { GlassLayout, HeroImage, PageHeading } from "@/components/GlassLayout";
import weddingHero from "@/assets/indian-wedding-hero.jpg";

export const Route = createFileRoute("/")({
  head: () => ({
    meta: [
      { title: "Calculate my Dahej | Smart Dahej Valuation Calculator" },
      {
        name: "description",
        content:
          "Discover what your startup is truly worth in simple, non-technical terms. Data-backed acquisition valuations powered by 400,000 synthetic records, 37 parity-weighted features, and a production Ridge + NN Ensemble (equal weightage) (R² ~0.758, MAE ₹187,674).",
      },
      {
        property: "og:title",
        content: "Calculate my Dahej | Smart Dahej Valuation Calculator",
      },
      {
        property: "og:description",
        content:
          "Simple, objective startup valuation calculations based on 37 parity-weighted, intellectual property, and market risk dimensions.",
      },
    ],
  }),
  component: HomePage,
});

const DEMO_PRESETS = [
  {
    id: "govt_officer",
    title: "Government Officer (Gazetted / IAS)",
    badge: "Government Stability",
    salary: "₹1,400,000 / mo",
    education: "Post Graduate (Master)",
    familyWealth: "₹25 Lakhs / yr + Medium Land",
    estimatedValuation: "₹15,22,000",
    valuationRange: "₹14.62 L – ₹15.82 L (±₹60k MAE)",
    keyFactor: "1.28x Permanent Govt Multiplier + House Ownership",
    description: "Permanent government employment and family real estate create a premium security baseline.",
  },
  {
    id: "nri_tech_lead",
    title: "NRI Software Tech Lead (USA/EU)",
    badge: "NRI Global Income",
    salary: "₹2,20,000 / mo",
    education: "Post Graduate (Master)",
    familyWealth: "₹32 Lakhs / yr + Large Land",
    estimatedValuation: "₹18,45,000",
    valuationRange: "₹17.85 L – ₹19.05 L (±₹60k MAE)",
    keyFactor: "1.35x NRI Abroad Multiplier + High Salary",
    description: "Global foreign currency earnings and strong economic index elevate the valuation bracket.",
  },
  {
    id: "corporate_pro",
    title: "Corporate Private Professional",
    badge: "MNC Corporate",
    salary: "₹72,000 / mo",
    education: "Graduate (Bachelor)",
    familyWealth: "₹18 Lakhs / yr + Small Land",
    estimatedValuation: "₹9,80,000",
    valuationRange: "₹9.20 L – ₹10.40 L (±₹60k MAE)",
    keyFactor: "Stable Private Career + Urban Residence",
    description: "Consistent monthly cash flow and city living provide a solid median market benchmark.",
  },
  {
    id: "family_business",
    title: "Established Business Family",
    badge: "Asset & Real Estate Heavy",
    salary: "₹1,50,000 / mo",
    education: "Graduate (Bachelor)",
    familyWealth: "₹38 Lakhs / yr + Large Land",
    estimatedValuation: "₹14,20,000",
    valuationRange: "₹13.60 L – ₹14.80 L (±₹60k MAE)",
    keyFactor: "Extensive Land Ownership & High Family Income",
    description: "Substantial physical land assets and high family revenue cushion provide strong tangible capital.",
  },
];

function HomePage() {
  const [activePreset, setActivePreset] = useState<(typeof DEMO_PRESETS)[number]>(
    DEMO_PRESETS[0]!
  );

  return (
    <GlassLayout>
      {/* Top Banner - Indian Wedding Bride and Groom */}
      <HeroImage src={weddingHero} alt="Indian Bride and Groom Wedding" />

      {/* Hero Section */}
      <section className="mb-10 text-center lg:text-left">
        <PageHeading
          eyebrow="Platform Overview & Welcome"
          title="Marriage are Arranged in Heaven But the Dahej are Arranged on the Earth"
          description="It is compulsory to take the dahej as after marriage  your wife cheated on you and go to court for the alimony  
          It is taken as a security money for the males as females are throwing males from the mountain cliff with the help of their bestfriend or boyfriend 
          use this for your safety and benfits."
        />

        <div className="mb-8 flex flex-wrap items-center justify-center gap-3 lg:justify-start">
          <Link
            to="/predictor"
            className="gradient-primary inline-flex items-center gap-2 rounded-[12px] px-6 py-3.5 text-sm font-bold text-primary-foreground shadow-[0_4px_20px_oklch(0.42_0.20_25/35%)] transition-all hover:scale-[1.02] active:scale-[0.98]"
          >
            Launch Dahej Predictor
            <ArrowRight className="h-4 w-4" />
          </Link>
          <Link
            to="/model"
            className="glass-subtle inline-flex items-center gap-2 rounded-[12px] px-5 py-3.5 text-sm font-bold text-foreground transition-all hover:bg-accent"
          >
            View Model Analytics (~0.758 R²)
          </Link>
        </div>
      </section>

      {/* Quick Stats Bar */}
      <section className="mb-12 grid grid-cols-2 gap-4 sm:grid-cols-4">
        <div className="glass glass-lift p-5 text-center">
          <p className="text-2xl font-extrabold text-primary sm:text-3xl">400,000+</p>
          <p className="mt-1 text-xs font-semibold text-muted-foreground uppercase tracking-wider">
            Synthetic Records
          </p>
        </div>
        <div className="glass glass-lift p-5 text-center">
          <p className="text-2xl font-extrabold text-primary sm:text-3xl">37</p>
          <p className="mt-1 text-xs font-semibold text-muted-foreground uppercase tracking-wider">
            Feature Dimensions
          </p>
        </div>
        <div className="glass glass-lift p-5 text-center">
          <p className="text-2xl font-extrabold text-primary sm:text-3xl">0.7581</p>
          <p className="mt-1 text-xs font-semibold text-muted-foreground uppercase tracking-wider">
            Champion R² (MAE ₹188k)
          </p>
        </div>
        <div className="glass glass-lift p-5 text-center">
          <p className="text-2xl font-extrabold text-primary sm:text-3xl">&lt;18 ms</p>
          <p className="mt-1 text-xs font-semibold text-muted-foreground uppercase tracking-wider">
            Inference Latency
          </p>
        </div>
      </section>

      {/* What is Calculate my Dahej in Plain English */}
      <section className="mb-14">
        <div className="mb-6">
          <p className="label-caps text-primary">The Big Picture</p>
          <h2 className="mt-1 text-2xl font-extrabold sm:text-3xl">
            What is Calculate my Dahej & Why Do You Need It?
          </h2>
          <p className="mt-2 text-sm text-muted-foreground max-w-3xl">
            Think of Calculate my Dahej as a digital appraiser engineered with state-of-the-art machine learning. Instead of guessing based on rumors or opinions, it cross-analyzes 37 parity-weighted, intellectual property, and operational dimensions against 400,000 synthetic records.
          </p>
        </div>

        <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
          <div className="glass glass-lift p-6 flex flex-col justify-between">
            <div>
              <div className="mb-4 flex h-10 w-10 items-center justify-center rounded-xl bg-primary/10 text-primary">
                <TrendingUp className="h-5 w-5" />
              </div>
              <h3 className="text-base font-bold">High Precision Bounds</h3>
              <p className="mt-2 text-xs text-muted-foreground leading-relaxed">
                Rather than wide speculative estimates, our model delivers tight, empirical price bounds calibrated to an MAE of ±₹187,674 with 75.8% parity-constrained fit.
              </p>
            </div>
            <span className="mt-4 text-[11px] font-bold text-primary">✓ Bounded Confidence Intervals</span>
          </div>

          <div className="glass glass-lift p-6 flex flex-col justify-between">
            <div>
              <div className="mb-4 flex h-10 w-10 items-center justify-center rounded-xl bg-primary/10 text-primary">
                <PieChart className="h-5 w-5" />
              </div>
              <h3 className="text-base font-bold">Clear Factor Contributions</h3>
              <p className="mt-2 text-xs text-muted-foreground leading-relaxed">
                See exactly how much recurring revenue, patent portfolios, cash reserves, and equipment add to the final valuation tag.
              </p>
            </div>
            <span className="mt-4 text-[11px] font-bold text-primary">✓ Transparent Asset Weights</span>
          </div>

          <div className="glass glass-lift p-6 flex flex-col justify-between">
            <div>
              <div className="mb-4 flex h-10 w-10 items-center justify-center rounded-xl bg-primary/10 text-primary">
                <ShieldAlert className="h-5 w-5" />
              </div>
              <h3 className="text-base font-bold">Smart Risk Factor Analysis</h3>
              <p className="mt-2 text-xs text-muted-foreground leading-relaxed">
                Automatically adjusts valuations for active legal disputes, brand reputation risks, or early-stage acquisition penalties.
              </p>
            </div>
            <span className="mt-4 text-[11px] font-bold text-primary">✓ Risk-Adjusted Output</span>
          </div>

          <div className="glass glass-lift p-6 flex flex-col justify-between">
            <div>
              <div className="mb-4 flex h-10 w-10 items-center justify-center rounded-xl bg-primary/10 text-primary">
                <BarChart3 className="h-5 w-5" />
              </div>
              <h3 className="text-base font-bold">Batch Portfolio Evaluation</h3>
              <p className="mt-2 text-xs text-muted-foreground leading-relaxed">
                Investors and VC funds can evaluate up to 100 entities in one go to compare deal-flow valuations effortlessly via the REST API.
              </p>
            </div>
            <span className="mt-4 text-[11px] font-bold text-primary">✓ High-Throughput REST API</span>
          </div>
        </div>
      </section>

      {/* How It Works - 3 Easy Steps */}
      <section className="mb-14 rounded-[var(--radius-md)] glass p-7 sm:p-9 border border-border">
        <div className="text-center max-w-2xl mx-auto mb-9">
          <p className="label-caps text-primary">Simple Workflow</p>
          <h2 className="mt-1 text-2xl font-extrabold sm:text-3xl">
            How It Works in 3 Simple Steps
          </h2>
          <p className="mt-2 text-sm text-muted-foreground">
            No complex accounting spreadsheets needed. Get an instant valuation breakdown in under two minutes.
          </p>
        </div>

        <div className="grid gap-6 md:grid-cols-3">
          <div className="glass-subtle p-6 rounded-2xl relative">
            <div className="absolute -top-4 left-6 flex h-8 w-8 items-center justify-center rounded-full gradient-primary text-xs font-black text-primary-foreground">
              1
            </div>
            <h3 className="mt-2 text-base font-bold text-foreground">
              Enter Match & Profile Metrics
            </h3>
            <p className="mt-2 text-xs text-muted-foreground leading-relaxed">
              Use simple sliders and select controls to enter monthly salary, profession, job stability, family income, land ownership, and education.
            </p>
          </div>

          <div className="glass-subtle p-6 rounded-2xl relative">
            <div className="absolute -top-4 left-6 flex h-8 w-8 items-center justify-center rounded-full gradient-primary text-xs font-black text-primary-foreground">
              2
            </div>
            <h3 className="mt-2 text-base font-bold text-foreground">
              Ridge + NN Ensemble Inference
            </h3>
            <p className="mt-2 text-xs text-muted-foreground leading-relaxed">
              A champion Ridge + Regularized NN (R² ~0.758) and Voting Ensemble (Ridge + Regularized NN) evaluate your parameters across 37 transformed dimensions.
            </p>
          </div>

          <div className="glass-subtle p-6 rounded-2xl relative">
            <div className="absolute -top-4 left-6 flex h-8 w-8 items-center justify-center rounded-full gradient-primary text-xs font-black text-primary-foreground">
              3
            </div>
            <h3 className="mt-2 text-base font-bold text-foreground">
              Get Instant Valuation & Breakdown
            </h3>
            <p className="mt-2 text-xs text-muted-foreground leading-relaxed">
              Receive your valuation price tag in Indian Rupees (INR), minimum-maximum confidence ranges (±₹187,674 MAE), asset distribution chart, and 5-year projections.
            </p>
          </div>
        </div>
      </section>

      {/* Interactive Sample Preset Showcase */}
      <section className="mb-14">
        <div className="mb-6">
          <p className="label-caps text-primary">Interactive Preview</p>
          <h2 className="mt-1 text-2xl font-extrabold sm:text-3xl">
            See How Different Startups are Valued
          </h2>
          <p className="mt-2 text-sm text-muted-foreground">
            Click on any sample startup profile below to see how business model, revenue type, and patents affect final valuation.
          </p>
        </div>

        <div className="grid gap-6 lg:grid-cols-[1fr_1.3fr]">
          {/* Preset Buttons */}
          <div className="space-y-3">
            {DEMO_PRESETS.map((preset) => {
              const isSelected = activePreset.id === preset.id;
              return (
                <button
                  key={preset.id}
                  type="button"
                  onClick={() => setActivePreset(preset)}
                  className={`w-full text-left p-4 rounded-xl transition-all ${
                    isSelected
                      ? "glass glass-lift border-primary/50 shadow-[0_4px_16px_oklch(0.42_0.20_25/20%)]"
                      : "glass-subtle hover:bg-accent/70"
                  }`}
                >
                  <div className="flex items-center justify-between">
                    <span className="font-bold text-sm text-foreground">{preset.title}</span>
                    <span className="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-primary/10 text-primary">
                      {preset.badge}
                    </span>
                  </div>
                  <div className="mt-2 flex items-center justify-between text-xs text-muted-foreground">
                    <span>{preset.salary}</span>
                    <span className="font-extrabold text-foreground">{preset.estimatedValuation}</span>
                  </div>
                </button>
              );
            })}
          </div>

          {/* Interactive Preset Output Display Card */}
          <div className="glass glass-lift p-6 sm:p-7 flex flex-col justify-between border-t-4 border-t-primary">
            <div>
              <div className="flex items-center justify-between mb-4">
                <span className="text-xs font-bold uppercase tracking-wider text-muted-foreground">
                  Sample Valuation Result
                </span>
                <span className="rounded-full bg-[oklch(0.55_0.135_162/15%)] px-3 py-1 text-xs font-bold text-success">
                  High Confidence (75.81% R² · MAE ₹188k)
                </span>
              </div>

              <h3 className="text-xl font-extrabold text-foreground">{activePreset.title}</h3>
              <p className="mt-1 text-xs text-muted-foreground">{activePreset.description}</p>

              <div className="mt-6 grid grid-cols-2 gap-4 rounded-xl bg-accent/30 p-4">
                <div>
                  <p className="text-[11px] font-semibold text-muted-foreground uppercase">
                    Estimated Valuation
                  </p>
                  <p className="mt-1 text-2xl font-black text-primary">
                    {activePreset.estimatedValuation}
                  </p>
                </div>
                <div>
                  <p className="text-[11px] font-semibold text-muted-foreground uppercase">
                    Synthetic Price Range
                  </p>
                  <p className="mt-1 text-sm font-bold text-foreground">
                    {activePreset.valuationRange}
                  </p>
                </div>
              </div>

              <div className="mt-5 space-y-2 text-xs">
                <div className="flex justify-between py-1 border-b border-border/50">
                  <span className="text-muted-foreground">Monthly Salary:</span>
                  <span className="font-bold text-foreground">{activePreset.salary}</span>
                </div>
                <div className="flex justify-between py-1 border-b border-border/50">
                  <span className="text-muted-foreground">Education Level:</span>
                  <span className="font-bold text-foreground">{activePreset.education}</span>
                </div>
                <div className="flex justify-between py-1 border-b border-border/50">
                  <span className="text-muted-foreground">Family Wealth & Real Estate:</span>
                  <span className="font-bold text-foreground">{activePreset.familyWealth}</span>
                </div>
                <div className="flex justify-between py-1">
                  <span className="text-muted-foreground">Primary Value Driver:</span>
                  <span className="font-bold text-primary">{activePreset.keyFactor}</span>
                </div>
              </div>
            </div>

            <div className="mt-6 pt-4 border-t border-border flex items-center justify-between">
              <span className="text-xs text-muted-foreground">
                Want to calculate your custom numbers?
              </span>
              <Link
                to="/predictor"
                className="inline-flex items-center gap-1.5 text-xs font-bold text-primary hover:underline"
              >
                Open Full Calculator <ArrowRight className="h-3.5 w-3.5" />
              </Link>
            </div>
          </div>
        </div>
      </section>

      {/* The 4 Core Valuation Pillars */}
      <section className="mb-14">
        <div className="mb-6">
          <p className="label-caps text-primary">Valuation Physics</p>
          <h2 className="mt-1 text-2xl font-extrabold sm:text-3xl">
            The 4 Key Drivers That Determine Your Valuation
          </h2>
          <p className="mt-2 text-sm text-muted-foreground">
            What determines the baseline between ₹5 Lakhs and ₹20+ Lakhs? Here is how our 37-feature model evaluates parity-weighted parameters:
          </p>
        </div>

        <div className="grid gap-5 sm:grid-cols-2">
          <div className="glass glass-lift p-6">
            <div className="flex items-center gap-3">
              <div className="flex h-9 w-9 items-center justify-center rounded-lg bg-primary/10 text-primary">
                <DollarSign className="h-5 w-5" />
              </div>
              <h3 className="font-bold text-base">1. Groom Monthly Salary & Profession</h3>
            </div>
            <p className="mt-3 text-xs text-muted-foreground leading-relaxed">
              Monthly take-home salary is the single strongest financial multiplier. Permanent government jobs and business careers command a significant stability premium.
            </p>
          </div>

          <div className="glass glass-lift p-6">
            <div className="flex items-center gap-3">
              <div className="flex h-9 w-9 items-center justify-center rounded-lg bg-primary/10 text-primary">
                <Lightbulb className="h-5 w-5" />
              </div>
              <h3 className="font-bold text-base">2. Education & Working Abroad (NRI)</h3>
            </div>
            <p className="mt-3 text-xs text-muted-foreground leading-relaxed">
              Post-graduate degrees (Master's, Doctorate) and foreign employment abroad (NRI status) create a strong upward multiplier in prospective desirability.
            </p>
          </div>

          <div className="glass glass-lift p-6">
            <div className="flex items-center gap-3">
              <div className="flex h-9 w-9 items-center justify-center rounded-lg bg-primary/10 text-primary">
                <Zap className="h-5 w-5" />
              </div>
              <h3 className="font-bold text-base">3. Family Income & Land Ownership</h3>
            </div>
            <p className="mt-3 text-xs text-muted-foreground leading-relaxed">
              Annual family earnings combined with physical land holdings (Small, Medium, Large) and house ownership establish a solid tangible asset foundation.
            </p>
          </div>

          <div className="glass glass-lift p-6">
            <div className="flex items-center gap-3">
              <div className="flex h-9 w-9 items-center justify-center rounded-lg bg-primary/10 text-primary">
                <ShieldCheck className="h-5 w-5" />
              </div>
              <h3 className="font-bold text-base">4. Bride Profile & Compatibility Offsets</h3>
            </div>
            <p className="mt-3 text-xs text-muted-foreground leading-relaxed">
              Bride's education, independent career, and family background provide balanced economic equilibrium and risk mitigation across match criteria.
            </p>
          </div>
        </div>
      </section>

      {/* Who Benefits Section */}
      <section className="mb-14 glass glass-lift p-7 sm:p-9 rounded-[var(--radius-md)] border border-border">
        <div className="mb-7">
          <p className="label-caps text-primary">Target Audience</p>
          <h2 className="mt-1 text-2xl font-extrabold sm:text-3xl">
            Who is Calculate my Dahej Built For?
          </h2>
        </div>

        <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
          <div>
            <div className="flex items-center gap-2 font-bold text-foreground text-sm">
              <CheckCircle2 className="h-4 w-4 text-primary" />
              Startup Founders
            </div>
            <p className="mt-2 text-xs text-muted-foreground leading-relaxed">
              Walk into investment meetings or M&A negotiation tables with realistic, objective valuation data instead of arbitrary guesses.
            </p>
          </div>

          <div>
            <div className="flex items-center gap-2 font-bold text-foreground text-sm">
              <CheckCircle2 className="h-4 w-4 text-primary" />
              Angel & VC Investors
            </div>
            <p className="mt-2 text-xs text-muted-foreground leading-relaxed">
              Quickly screen pitch decks, benchmark founder valuation asks, and analyze entire portfolio deal flow in batch CSV format.
            </p>
          </div>

          <div>
            <div className="flex items-center gap-2 font-bold text-foreground text-sm">
              <CheckCircle2 className="h-4 w-4 text-primary" />
              M&A Advisors
            </div>
            <p className="mt-2 text-xs text-muted-foreground leading-relaxed">
              Provide clients with clear, transparent reports showing baseline valuations, lower/upper bounds, and risk score adjustments.
            </p>
          </div>

          <div>
            <div className="flex items-center gap-2 font-bold text-foreground text-sm">
              <CheckCircle2 className="h-4 w-4 text-primary" />
              Business Buyers
            </div>
            <p className="mt-2 text-xs text-muted-foreground leading-relaxed">
              Verify if an asking acquisition price is fair before entering deep due diligence or issuing an intent letter.
            </p>
          </div>
        </div>
      </section>
    </GlassLayout>
  );
}
