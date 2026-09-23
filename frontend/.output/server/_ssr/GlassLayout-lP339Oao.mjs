import { i as require_jsx_runtime } from "../_libs/react+tanstack__react-query.mjs";
import { h as Link } from "../_libs/@tanstack/react-router+[...].mjs";
//#region node_modules/.nitro/vite/services/ssr/assets/GlassLayout-lP339Oao.js
var import_jsx_runtime = require_jsx_runtime();
var _1111_default = "/assets/1111-0ti_djOF.jpg";
var navItems = [
	{
		to: "/",
		label: "Overview"
	},
	{
		to: "/predictor",
		label: "Dahej Predictor"
	},
	{
		to: "/model",
		label: "Model Analytics"
	},
	{
		to: "/api",
		label: "API Architecture"
	}
];
function GlassLayout({ children }) {
	return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
		className: "relative min-h-screen",
		children: [
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
				className: "orb h-[500px] w-[500px] -top-24 -left-24",
				style: { background: "oklch(0.45 0.18 25 / 25%)" },
				"aria-hidden": true
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
				className: "orb h-[600px] w-[600px] -bottom-36 -right-24",
				style: { background: "oklch(0.38 0.16 20 / 20%)" },
				"aria-hidden": true
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
				className: "orb h-[450px] w-[450px] top-[40%] left-[35%]",
				style: { background: "oklch(0.50 0.15 30 / 18%)" },
				"aria-hidden": true
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
				className: "relative z-1 mx-auto max-w-[1440px] px-4 py-6 sm:px-6",
				children: [
					/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("header", {
						className: "glass glass-lift mb-7 flex flex-col gap-4 px-5 py-4 sm:px-8 lg:flex-row lg:items-center lg:justify-between",
						children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)(Link, {
							to: "/",
							className: "flex items-center gap-3 group",
							children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
								className: "relative flex h-11 w-11 items-center justify-center overflow-hidden rounded-[12px] border border-primary/40 shadow-[0_4px_14px_oklch(0.42_0.20_25/35%)] transition-transform group-hover:scale-105",
								children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)("img", {
									src: _1111_default,
									alt: "Calculate my Dahej Logo",
									className: "h-full w-full object-cover"
								})
							}), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("span", {
								className: "text-xl font-extrabold tracking-tight",
								children: ["Calculate my ", /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
									className: "text-primary",
									children: "Dahej"
								})]
							})]
						}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("nav", {
							className: "glass-subtle flex flex-wrap gap-1 p-1.5",
							children: navItems.map((item) => /* @__PURE__ */ (0, import_jsx_runtime.jsx)(Link, {
								to: item.to,
								activeOptions: { exact: item.to === "/" },
								className: "rounded-[10px] px-4 py-2.5 text-sm font-semibold transition-all",
								inactiveProps: { className: "text-muted-foreground hover:bg-primary/10 hover:text-primary" },
								activeProps: { className: "gradient-primary text-primary-foreground font-bold shadow-[0_2px_10px_oklch(0.42_0.20_25/35%)]" },
								children: item.label
							}, item.to))
						})]
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)("main", {
						className: "animate-in fade-in duration-500",
						children
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("footer", {
						className: "glass-subtle mt-8 flex flex-col gap-1 px-6 py-5 text-sm text-muted-foreground sm:flex-row sm:items-center sm:justify-between",
						children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", { children: "Ridge + NN Ensemble (equal weightage) · 400,000 synthetic records · 37 features" }), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", { children: "Production R² ~0.758 · MAE ₹187,674 · RMSE ₹242,985" })]
					})
				]
			})
		]
	});
}
function PageHeading({ eyebrow, title, description }) {
	return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
		className: "mb-6",
		children: [
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
				className: "label-caps text-primary",
				children: eyebrow
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h1", {
				className: "mt-2 text-3xl font-extrabold sm:text-4xl",
				children: title
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
				className: "mt-2 max-w-3xl text-[0.975rem] text-muted-foreground",
				children: description
			})
		]
	});
}
function HeroImage({ src, alt, className }) {
	return /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
		className: "mb-7 overflow-hidden rounded-[var(--radius-md)] border border-border shadow-[var(--glass-shadow-md)]",
		children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)("img", {
			src,
			alt,
			width: 1600,
			height: 900,
			className: `h-[340px] sm:h-[480px] w-full object-cover object-[center_15%] ${className || ""}`
		})
	});
}
//#endregion
export { HeroImage as n, PageHeading as r, GlassLayout as t };
