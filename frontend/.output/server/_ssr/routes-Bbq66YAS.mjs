import { i as __toESM } from "../_runtime.mjs";
import { a as require_react, i as require_jsx_runtime } from "../_libs/react+tanstack__react-query.mjs";
import { h as Link } from "../_libs/@tanstack/react-router+[...].mjs";
import { n as HeroImage, r as PageHeading, t as GlassLayout } from "./GlassLayout-lP339Oao.mjs";
import { M as ArrowRight, O as ChartPie, b as DollarSign, c as ShieldAlert, k as ChartColumn, m as Lightbulb, r as TrendingUp, s as ShieldCheck, t as Zap, w as CircleCheck } from "../_libs/lucide-react.mjs";
//#region node_modules/.nitro/vite/services/ssr/assets/routes-Bbq66YAS.js
var import_react = /* @__PURE__ */ __toESM(require_react());
var import_jsx_runtime = require_jsx_runtime();
var indian_wedding_hero_default = "/assets/indian-wedding-hero-IYmWfBLA.jpg";
var DEMO_PRESETS = [
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
		description: "Permanent government employment and family real estate create a premium security baseline."
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
		description: "Global foreign currency earnings and strong economic index elevate the valuation bracket."
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
		description: "Consistent monthly cash flow and city living provide a solid median market benchmark."
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
		description: "Substantial physical land assets and high family revenue cushion provide strong tangible capital."
	}
];
function HomePage() {
	const [activePreset, setActivePreset] = (0, import_react.useState)(DEMO_PRESETS[0]);
	return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)(GlassLayout, { children: [
		/* @__PURE__ */ (0, import_jsx_runtime.jsx)(HeroImage, {
			src: indian_wedding_hero_default,
			alt: "Indian Bride and Groom Wedding"
		}),
		/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("section", {
			className: "mb-10 text-center lg:text-left",
			children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(PageHeading, {
				eyebrow: "Platform Overview & Welcome",
				title: "Marriage are Arranged in Heaven But the Dahej are Arranged on the Earth",
				description: "It is compulsory to take the dahej as after marriage  your wife cheated on you and go to court for the alimony  \r\n          It is taken as a security money for the males as females are throwing males from the mountain cliff with the help of their bestfriend or boyfriend \r\n          use this for your safety and benfits."
			}), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
				className: "mb-8 flex flex-wrap items-center justify-center gap-3 lg:justify-start",
				children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)(Link, {
					to: "/predictor",
					className: "gradient-primary inline-flex items-center gap-2 rounded-[12px] px-6 py-3.5 text-sm font-bold text-primary-foreground shadow-[0_4px_20px_oklch(0.42_0.20_25/35%)] transition-all hover:scale-[1.02] active:scale-[0.98]",
					children: ["Launch Dahej Predictor", /* @__PURE__ */ (0, import_jsx_runtime.jsx)(ArrowRight, { className: "h-4 w-4" })]
				}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)(Link, {
					to: "/model",
					className: "glass-subtle inline-flex items-center gap-2 rounded-[12px] px-5 py-3.5 text-sm font-bold text-foreground transition-all hover:bg-accent",
					children: "View Model Analytics (~0.758 R²)"
				})]
			})]
		}),
		/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("section", {
			className: "mb-12 grid grid-cols-2 gap-4 sm:grid-cols-4",
			children: [
				/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
					className: "glass glass-lift p-5 text-center",
					children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
						className: "text-2xl font-extrabold text-primary sm:text-3xl",
						children: "400,000+"
					}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
						className: "mt-1 text-xs font-semibold text-muted-foreground uppercase tracking-wider",
						children: "Synthetic Records"
					})]
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
					className: "glass glass-lift p-5 text-center",
					children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
						className: "text-2xl font-extrabold text-primary sm:text-3xl",
						children: "37"
					}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
						className: "mt-1 text-xs font-semibold text-muted-foreground uppercase tracking-wider",
						children: "Feature Dimensions"
					})]
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
					className: "glass glass-lift p-5 text-center",
					children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
						className: "text-2xl font-extrabold text-primary sm:text-3xl",
						children: "0.7581"
					}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
						className: "mt-1 text-xs font-semibold text-muted-foreground uppercase tracking-wider",
						children: "Champion R² (MAE ₹188k)"
					})]
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
					className: "glass glass-lift p-5 text-center",
					children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
						className: "text-2xl font-extrabold text-primary sm:text-3xl",
						children: "<18 ms"
					}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
						className: "mt-1 text-xs font-semibold text-muted-foreground uppercase tracking-wider",
						children: "Inference Latency"
					})]
				})
			]
		}),
		/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("section", {
			className: "mb-14",
			children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
				className: "mb-6",
				children: [
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
						className: "label-caps text-primary",
						children: "The Big Picture"
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h2", {
						className: "mt-1 text-2xl font-extrabold sm:text-3xl",
						children: "What is Calculate my Dahej & Why Do You Need It?"
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
						className: "mt-2 text-sm text-muted-foreground max-w-3xl",
						children: "Think of Calculate my Dahej as a digital appraiser engineered with state-of-the-art machine learning. Instead of guessing based on rumors or opinions, it cross-analyzes 37 parity-weighted, intellectual property, and operational dimensions against 400,000 synthetic records."
					})
				]
			}), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
				className: "grid gap-6 sm:grid-cols-2 lg:grid-cols-4",
				children: [
					/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
						className: "glass glass-lift p-6 flex flex-col justify-between",
						children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { children: [
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
								className: "mb-4 flex h-10 w-10 items-center justify-center rounded-xl bg-primary/10 text-primary",
								children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(TrendingUp, { className: "h-5 w-5" })
							}),
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h3", {
								className: "text-base font-bold",
								children: "High Precision Bounds"
							}),
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
								className: "mt-2 text-xs text-muted-foreground leading-relaxed",
								children: "Rather than wide speculative estimates, our model delivers tight, empirical price bounds calibrated to an MAE of ±₹187,674 with 75.8% parity-constrained fit."
							})
						] }), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
							className: "mt-4 text-[11px] font-bold text-primary",
							children: "✓ Bounded Confidence Intervals"
						})]
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
						className: "glass glass-lift p-6 flex flex-col justify-between",
						children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { children: [
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
								className: "mb-4 flex h-10 w-10 items-center justify-center rounded-xl bg-primary/10 text-primary",
								children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(ChartPie, { className: "h-5 w-5" })
							}),
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h3", {
								className: "text-base font-bold",
								children: "Clear Factor Contributions"
							}),
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
								className: "mt-2 text-xs text-muted-foreground leading-relaxed",
								children: "See exactly how much recurring revenue, patent portfolios, cash reserves, and equipment add to the final valuation tag."
							})
						] }), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
							className: "mt-4 text-[11px] font-bold text-primary",
							children: "✓ Transparent Asset Weights"
						})]
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
						className: "glass glass-lift p-6 flex flex-col justify-between",
						children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { children: [
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
								className: "mb-4 flex h-10 w-10 items-center justify-center rounded-xl bg-primary/10 text-primary",
								children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(ShieldAlert, { className: "h-5 w-5" })
							}),
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h3", {
								className: "text-base font-bold",
								children: "Smart Risk Factor Analysis"
							}),
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
								className: "mt-2 text-xs text-muted-foreground leading-relaxed",
								children: "Automatically adjusts valuations for active legal disputes, brand reputation risks, or early-stage acquisition penalties."
							})
						] }), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
							className: "mt-4 text-[11px] font-bold text-primary",
							children: "✓ Risk-Adjusted Output"
						})]
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
						className: "glass glass-lift p-6 flex flex-col justify-between",
						children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { children: [
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
								className: "mb-4 flex h-10 w-10 items-center justify-center rounded-xl bg-primary/10 text-primary",
								children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(ChartColumn, { className: "h-5 w-5" })
							}),
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h3", {
								className: "text-base font-bold",
								children: "Batch Portfolio Evaluation"
							}),
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
								className: "mt-2 text-xs text-muted-foreground leading-relaxed",
								children: "Investors and VC funds can evaluate up to 100 entities in one go to compare deal-flow valuations effortlessly via the REST API."
							})
						] }), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
							className: "mt-4 text-[11px] font-bold text-primary",
							children: "✓ High-Throughput REST API"
						})]
					})
				]
			})]
		}),
		/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("section", {
			className: "mb-14 rounded-[var(--radius-md)] glass p-7 sm:p-9 border border-border",
			children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
				className: "text-center max-w-2xl mx-auto mb-9",
				children: [
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
						className: "label-caps text-primary",
						children: "Simple Workflow"
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h2", {
						className: "mt-1 text-2xl font-extrabold sm:text-3xl",
						children: "How It Works in 3 Simple Steps"
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
						className: "mt-2 text-sm text-muted-foreground",
						children: "No complex accounting spreadsheets needed. Get an instant valuation breakdown in under two minutes."
					})
				]
			}), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
				className: "grid gap-6 md:grid-cols-3",
				children: [
					/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
						className: "glass-subtle p-6 rounded-2xl relative",
						children: [
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
								className: "absolute -top-4 left-6 flex h-8 w-8 items-center justify-center rounded-full gradient-primary text-xs font-black text-primary-foreground",
								children: "1"
							}),
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h3", {
								className: "mt-2 text-base font-bold text-foreground",
								children: "Enter Match & Profile Metrics"
							}),
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
								className: "mt-2 text-xs text-muted-foreground leading-relaxed",
								children: "Use simple sliders and select controls to enter monthly salary, profession, job stability, family income, land ownership, and education."
							})
						]
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
						className: "glass-subtle p-6 rounded-2xl relative",
						children: [
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
								className: "absolute -top-4 left-6 flex h-8 w-8 items-center justify-center rounded-full gradient-primary text-xs font-black text-primary-foreground",
								children: "2"
							}),
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h3", {
								className: "mt-2 text-base font-bold text-foreground",
								children: "Ridge + NN Ensemble Inference"
							}),
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
								className: "mt-2 text-xs text-muted-foreground leading-relaxed",
								children: "A champion Ridge + Regularized NN (R² ~0.758) and Voting Ensemble (Ridge + Regularized NN) evaluate your parameters across 37 transformed dimensions."
							})
						]
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
						className: "glass-subtle p-6 rounded-2xl relative",
						children: [
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
								className: "absolute -top-4 left-6 flex h-8 w-8 items-center justify-center rounded-full gradient-primary text-xs font-black text-primary-foreground",
								children: "3"
							}),
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h3", {
								className: "mt-2 text-base font-bold text-foreground",
								children: "Get Instant Valuation & Breakdown"
							}),
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
								className: "mt-2 text-xs text-muted-foreground leading-relaxed",
								children: "Receive your valuation price tag in Indian Rupees (INR), minimum-maximum confidence ranges (±₹187,674 MAE), asset distribution chart, and 5-year projections."
							})
						]
					})
				]
			})]
		}),
		/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("section", {
			className: "mb-14",
			children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
				className: "mb-6",
				children: [
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
						className: "label-caps text-primary",
						children: "Interactive Preview"
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h2", {
						className: "mt-1 text-2xl font-extrabold sm:text-3xl",
						children: "See How Different Startups are Valued"
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
						className: "mt-2 text-sm text-muted-foreground",
						children: "Click on any sample startup profile below to see how business model, revenue type, and patents affect final valuation."
					})
				]
			}), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
				className: "grid gap-6 lg:grid-cols-[1fr_1.3fr]",
				children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
					className: "space-y-3",
					children: DEMO_PRESETS.map((preset) => {
						const isSelected = activePreset.id === preset.id;
						return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("button", {
							type: "button",
							onClick: () => setActivePreset(preset),
							className: `w-full text-left p-4 rounded-xl transition-all ${isSelected ? "glass glass-lift border-primary/50 shadow-[0_4px_16px_oklch(0.42_0.20_25/20%)]" : "glass-subtle hover:bg-accent/70"}`,
							children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
								className: "flex items-center justify-between",
								children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
									className: "font-bold text-sm text-foreground",
									children: preset.title
								}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
									className: "text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-primary/10 text-primary",
									children: preset.badge
								})]
							}), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
								className: "mt-2 flex items-center justify-between text-xs text-muted-foreground",
								children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", { children: preset.salary }), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
									className: "font-extrabold text-foreground",
									children: preset.estimatedValuation
								})]
							})]
						}, preset.id);
					})
				}), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
					className: "glass glass-lift p-6 sm:p-7 flex flex-col justify-between border-t-4 border-t-primary",
					children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { children: [
						/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
							className: "flex items-center justify-between mb-4",
							children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
								className: "text-xs font-bold uppercase tracking-wider text-muted-foreground",
								children: "Sample Valuation Result"
							}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
								className: "rounded-full bg-[oklch(0.55_0.135_162/15%)] px-3 py-1 text-xs font-bold text-success",
								children: "High Confidence (75.81% R² · MAE ₹188k)"
							})]
						}),
						/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h3", {
							className: "text-xl font-extrabold text-foreground",
							children: activePreset.title
						}),
						/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
							className: "mt-1 text-xs text-muted-foreground",
							children: activePreset.description
						}),
						/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
							className: "mt-6 grid grid-cols-2 gap-4 rounded-xl bg-accent/30 p-4",
							children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
								className: "text-[11px] font-semibold text-muted-foreground uppercase",
								children: "Estimated Valuation"
							}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
								className: "mt-1 text-2xl font-black text-primary",
								children: activePreset.estimatedValuation
							})] }), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
								className: "text-[11px] font-semibold text-muted-foreground uppercase",
								children: "Synthetic Price Range"
							}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
								className: "mt-1 text-sm font-bold text-foreground",
								children: activePreset.valuationRange
							})] })]
						}),
						/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
							className: "mt-5 space-y-2 text-xs",
							children: [
								/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
									className: "flex justify-between py-1 border-b border-border/50",
									children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
										className: "text-muted-foreground",
										children: "Monthly Salary:"
									}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
										className: "font-bold text-foreground",
										children: activePreset.salary
									})]
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
									className: "flex justify-between py-1 border-b border-border/50",
									children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
										className: "text-muted-foreground",
										children: "Education Level:"
									}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
										className: "font-bold text-foreground",
										children: activePreset.education
									})]
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
									className: "flex justify-between py-1 border-b border-border/50",
									children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
										className: "text-muted-foreground",
										children: "Family Wealth & Real Estate:"
									}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
										className: "font-bold text-foreground",
										children: activePreset.familyWealth
									})]
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
									className: "flex justify-between py-1",
									children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
										className: "text-muted-foreground",
										children: "Primary Value Driver:"
									}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
										className: "font-bold text-primary",
										children: activePreset.keyFactor
									})]
								})
							]
						})
					] }), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
						className: "mt-6 pt-4 border-t border-border flex items-center justify-between",
						children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
							className: "text-xs text-muted-foreground",
							children: "Want to calculate your custom numbers?"
						}), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)(Link, {
							to: "/predictor",
							className: "inline-flex items-center gap-1.5 text-xs font-bold text-primary hover:underline",
							children: ["Open Full Calculator ", /* @__PURE__ */ (0, import_jsx_runtime.jsx)(ArrowRight, { className: "h-3.5 w-3.5" })]
						})]
					})]
				})]
			})]
		}),
		/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("section", {
			className: "mb-14",
			children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
				className: "mb-6",
				children: [
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
						className: "label-caps text-primary",
						children: "Valuation Physics"
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h2", {
						className: "mt-1 text-2xl font-extrabold sm:text-3xl",
						children: "The 4 Key Drivers That Determine Your Valuation"
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
						className: "mt-2 text-sm text-muted-foreground",
						children: "What determines the baseline between ₹5 Lakhs and ₹20+ Lakhs? Here is how our 37-feature model evaluates parity-weighted parameters:"
					})
				]
			}), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
				className: "grid gap-5 sm:grid-cols-2",
				children: [
					/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
						className: "glass glass-lift p-6",
						children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
							className: "flex items-center gap-3",
							children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
								className: "flex h-9 w-9 items-center justify-center rounded-lg bg-primary/10 text-primary",
								children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(DollarSign, { className: "h-5 w-5" })
							}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("h3", {
								className: "font-bold text-base",
								children: "1. Groom Monthly Salary & Profession"
							})]
						}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
							className: "mt-3 text-xs text-muted-foreground leading-relaxed",
							children: "Monthly take-home salary is the single strongest financial multiplier. Permanent government jobs and business careers command a significant stability premium."
						})]
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
						className: "glass glass-lift p-6",
						children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
							className: "flex items-center gap-3",
							children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
								className: "flex h-9 w-9 items-center justify-center rounded-lg bg-primary/10 text-primary",
								children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(Lightbulb, { className: "h-5 w-5" })
							}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("h3", {
								className: "font-bold text-base",
								children: "2. Education & Working Abroad (NRI)"
							})]
						}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
							className: "mt-3 text-xs text-muted-foreground leading-relaxed",
							children: "Post-graduate degrees (Master's, Doctorate) and foreign employment abroad (NRI status) create a strong upward multiplier in prospective desirability."
						})]
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
						className: "glass glass-lift p-6",
						children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
							className: "flex items-center gap-3",
							children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
								className: "flex h-9 w-9 items-center justify-center rounded-lg bg-primary/10 text-primary",
								children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(Zap, { className: "h-5 w-5" })
							}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("h3", {
								className: "font-bold text-base",
								children: "3. Family Income & Land Ownership"
							})]
						}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
							className: "mt-3 text-xs text-muted-foreground leading-relaxed",
							children: "Annual family earnings combined with physical land holdings (Small, Medium, Large) and house ownership establish a solid tangible asset foundation."
						})]
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
						className: "glass glass-lift p-6",
						children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
							className: "flex items-center gap-3",
							children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
								className: "flex h-9 w-9 items-center justify-center rounded-lg bg-primary/10 text-primary",
								children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(ShieldCheck, { className: "h-5 w-5" })
							}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("h3", {
								className: "font-bold text-base",
								children: "4. Bride Profile & Compatibility Offsets"
							})]
						}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
							className: "mt-3 text-xs text-muted-foreground leading-relaxed",
							children: "Bride's education, independent career, and family background provide balanced economic equilibrium and risk mitigation across match criteria."
						})]
					})
				]
			})]
		}),
		/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("section", {
			className: "mb-14 glass glass-lift p-7 sm:p-9 rounded-[var(--radius-md)] border border-border",
			children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
				className: "mb-7",
				children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
					className: "label-caps text-primary",
					children: "Target Audience"
				}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("h2", {
					className: "mt-1 text-2xl font-extrabold sm:text-3xl",
					children: "Who is Calculate my Dahej Built For?"
				})]
			}), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
				className: "grid gap-6 sm:grid-cols-2 lg:grid-cols-4",
				children: [
					/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
						className: "flex items-center gap-2 font-bold text-foreground text-sm",
						children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(CircleCheck, { className: "h-4 w-4 text-primary" }), "Startup Founders"]
					}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
						className: "mt-2 text-xs text-muted-foreground leading-relaxed",
						children: "Walk into investment meetings or M&A negotiation tables with realistic, objective valuation data instead of arbitrary guesses."
					})] }),
					/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
						className: "flex items-center gap-2 font-bold text-foreground text-sm",
						children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(CircleCheck, { className: "h-4 w-4 text-primary" }), "Angel & VC Investors"]
					}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
						className: "mt-2 text-xs text-muted-foreground leading-relaxed",
						children: "Quickly screen pitch decks, benchmark founder valuation asks, and analyze entire portfolio deal flow in batch CSV format."
					})] }),
					/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
						className: "flex items-center gap-2 font-bold text-foreground text-sm",
						children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(CircleCheck, { className: "h-4 w-4 text-primary" }), "M&A Advisors"]
					}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
						className: "mt-2 text-xs text-muted-foreground leading-relaxed",
						children: "Provide clients with clear, transparent reports showing baseline valuations, lower/upper bounds, and risk score adjustments."
					})] }),
					/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
						className: "flex items-center gap-2 font-bold text-foreground text-sm",
						children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(CircleCheck, { className: "h-4 w-4 text-primary" }), "Business Buyers"]
					}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
						className: "mt-2 text-xs text-muted-foreground leading-relaxed",
						children: "Verify if an asking acquisition price is fair before entering deep due diligence or issuing an intent letter."
					})] })
				]
			})]
		})
	] });
}
//#endregion
export { HomePage as component };
