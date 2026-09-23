import { i as __toESM } from "../_runtime.mjs";
import { a as require_react, i as require_jsx_runtime, r as QueryClientProvider } from "../_libs/react+tanstack__react-query.mjs";
import { c as HeadContent, d as Outlet, f as lazyRouteComponent, g as useRouter, h as Link, m as createRootRouteWithContext, p as createFileRoute, s as Scripts, u as createRouter } from "../_libs/@tanstack/react-router+[...].mjs";
import { t as QueryClient } from "../_libs/tanstack__query-core.mjs";
//#region node_modules/.nitro/vite/services/ssr/assets/router-BvBGGSaB.js
var import_react = /* @__PURE__ */ __toESM(require_react());
var import_jsx_runtime = require_jsx_runtime();
var __defProp = Object.defineProperty;
var __exportAll = (all, no_symbols) => {
	let target = {};
	for (var name in all) __defProp(target, name, {
		get: all[name],
		enumerable: true
	});
	if (!no_symbols) __defProp(target, Symbol.toStringTag, { value: "Module" });
	return target;
};
var styles_default = "/assets/styles-C1pI9BoX.css";
function reportLovableError(error, context = {}) {
	if (typeof window === "undefined") return;
	window.__lovableEvents?.captureException?.(error, {
		source: "react_error_boundary",
		route: window.location.pathname,
		...context
	}, {
		mechanism: "react_error_boundary",
		handled: false,
		severity: "error"
	});
	const message = error instanceof Response ? `Response ${error.status}${error.url ? ` at ${error.url}` : ""}` : error instanceof Error ? error.message : String(error);
	const stack = error instanceof Error ? error.stack : void 0;
	window.__lovableReportRuntimeError?.({
		message,
		...stack !== void 0 && { stack },
		filename: window.location.pathname
	});
}
function NotFoundComponent() {
	return /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
		className: "flex min-h-screen items-center justify-center bg-background px-4",
		children: /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
			className: "max-w-md text-center",
			children: [
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h1", {
					className: "text-7xl font-bold text-foreground",
					children: "404"
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h2", {
					className: "mt-4 text-xl font-semibold text-foreground",
					children: "Page not found"
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
					className: "mt-2 text-sm text-muted-foreground",
					children: "The page you're looking for doesn't exist or has been moved."
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
					className: "mt-6",
					children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(Link, {
						to: "/",
						className: "inline-flex items-center justify-center rounded-md bg-primary px-4 py-2 text-sm font-medium text-primary-foreground transition-colors hover:bg-primary/90",
						children: "Go home"
					})
				})
			]
		})
	});
}
function ErrorComponent({ error, reset }) {
	console.error(error);
	const router = useRouter();
	(0, import_react.useEffect)(() => {
		reportLovableError(error, { boundary: "tanstack_root_error_component" });
	}, [error]);
	return /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
		className: "flex min-h-screen items-center justify-center bg-background px-4",
		children: /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
			className: "max-w-md text-center",
			children: [
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h1", {
					className: "text-xl font-semibold tracking-tight text-foreground",
					children: "This page didn't load"
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
					className: "mt-2 text-sm text-muted-foreground",
					children: "Something went wrong on our end. You can try refreshing or head back home."
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
					className: "mt-6 flex flex-wrap justify-center gap-2",
					children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("button", {
						onClick: () => {
							router.invalidate();
							reset();
						},
						className: "inline-flex items-center justify-center rounded-md bg-primary px-4 py-2 text-sm font-medium text-primary-foreground transition-colors hover:bg-primary/90",
						children: "Try again"
					}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("a", {
						href: "/",
						className: "inline-flex items-center justify-center rounded-md border border-input bg-background px-4 py-2 text-sm font-medium text-foreground transition-colors hover:bg-accent",
						children: "Go home"
					})]
				})
			]
		})
	});
}
var Route$4 = createRootRouteWithContext()({
	head: () => ({
		meta: [
			{ charSet: "utf-8" },
			{
				name: "viewport",
				content: "width=device-width, initial-scale=1"
			},
			{ title: "Calculate my Dahej" },
			{
				name: "description",
				content: "Calculate my Dahej - Smart AI Valuation Calculator Engine"
			},
			{
				name: "author",
				content: "Calculate my Dahej"
			},
			{
				property: "og:title",
				content: "Calculate my Dahej"
			},
			{
				property: "og:description",
				content: "Lovable Generated Project"
			},
			{
				property: "og:type",
				content: "website"
			},
			{
				name: "twitter:card",
				content: "summary_large_image"
			},
			{
				name: "twitter:site",
				content: "@Lovable"
			}
		],
		links: [{
			rel: "stylesheet",
			href: styles_default
		}, {
			rel: "icon",
			href: "/favicon.ico",
			type: "image/x-icon"
		}]
	}),
	shellComponent: RootShell,
	component: RootComponent,
	notFoundComponent: NotFoundComponent,
	errorComponent: ErrorComponent
});
function RootShell({ children }) {
	return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("html", {
		lang: "en",
		children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("head", { children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(HeadContent, {}) }), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("body", { children: [children, /* @__PURE__ */ (0, import_jsx_runtime.jsx)(Scripts, {})] })]
	});
}
function RootComponent() {
	const { queryClient } = Route$4.useRouteContext();
	return /* @__PURE__ */ (0, import_jsx_runtime.jsx)(QueryClientProvider, {
		client: queryClient,
		children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(Outlet, {})
	});
}
var $$splitComponentImporter$3 = () => import("./routes-Bbq66YAS.mjs");
var Route$3 = createFileRoute("/")({
	head: () => ({ meta: [
		{ title: "Calculate my Dahej | Smart Dahej Valuation Calculator" },
		{
			name: "description",
			content: "Discover what your startup is truly worth in simple, non-technical terms. Data-backed acquisition valuations powered by 400,000 synthetic records, 37 parity-weighted features, and a production Ridge + NN Ensemble (equal weightage) (R² ~0.758, MAE ₹187,674)."
		},
		{
			property: "og:title",
			content: "Calculate my Dahej | Smart Dahej Valuation Calculator"
		},
		{
			property: "og:description",
			content: "Simple, objective startup valuation calculations based on 37 parity-weighted, intellectual property, and market risk dimensions."
		}
	] }),
	component: lazyRouteComponent($$splitComponentImporter$3, "component")
});
var $$splitComponentImporter$2 = () => import("./api-B0oMxGwI.mjs");
var Route$2 = createFileRoute("/api")({
	head: () => ({ meta: [
		{ title: "Developer API & Architecture Portal | Calculate my Dahej" },
		{
			name: "description",
			content: "FastAPI backend architecture & REST endpoint reference for /health, /model/info, /predict and /predict/batch. Production Ridge + NN Ensemble & Ensemble with R² ~0.758, MAE ₹187,674, and 37 features."
		},
		{
			property: "og:title",
			content: "Developer API & Architecture Portal | Calculate my Dahej"
		},
		{
			property: "og:description",
			content: "Integrate the production valuation model (R² ~0.758, MAE ₹187,674) with high-speed FastAPI REST endpoints, OpenAPI docs, and multi-language snippets."
		}
	] }),
	component: lazyRouteComponent($$splitComponentImporter$2, "component")
});
var $$splitComponentImporter$1 = () => import("./model-DEVmVQTN.mjs");
var Route$1 = createFileRoute("/model")({
	head: () => ({ meta: [
		{ title: "Model Performance & Ensemble Analytics | Calculate my Dahej" },
		{
			name: "description",
			content: "Transparency dashboard for the Ridge + Regularized NN Ensemble: R² ~0.758, MAE ₹187,674, RMSE ₹242,985, MAPE ~10.1%, 37 transformed features across 400,000 synthetic records."
		},
		{
			property: "og:title",
			content: "Model Performance & Ensemble Analytics | Calculate my Dahej"
		},
		{
			property: "og:description",
			content: "Benchmark grid, 5-fold cross-validation variance, 37-feature weighting and residual diagnostics for the valuation pipeline."
		}
	] }),
	component: lazyRouteComponent($$splitComponentImporter$1, "component")
});
var $$splitComponentImporter = () => import("./predictor-DA1vVwkW.mjs");
var Route = createFileRoute("/predictor")({
	head: () => ({ meta: [
		{ title: "Empirical Dahej Predictor & Valuation Calculator" },
		{
			name: "description",
			content: "Predict data-driven dowry estimates in INR with our production Ridge + Regularized NN ensemble (R² ~0.758, MAE ₹187,674, equal weightage). Adjust empirical groom and bride parameters from the dataset for real-time confidence bounds."
		},
		{
			property: "og:title",
			content: "Empirical Dahej Predictor & Valuation Calculator"
		},
		{
			property: "og:description",
			content: "Live empirical valuation engine trained on 400,000 synthetic records and 37 parity-weighted features with dynamic confidence intervals."
		}
	] }),
	component: lazyRouteComponent($$splitComponentImporter, "component")
});
var glassTooltip = {
	background: "var(--glass-surface-strong)",
	backdropFilter: "blur(16px)",
	border: "1px solid var(--border)",
	borderRadius: "12px",
	color: "var(--foreground)",
	fontSize: 12
};
var rootRouteChildren = {
	IndexRoute: Route$3.update({
		id: "/",
		path: "/",
		getParentRoute: () => Route$4
	}),
	ApiRoute: Route$2.update({
		id: "/api",
		path: "/api",
		getParentRoute: () => Route$4
	}),
	ModelRoute: Route$1.update({
		id: "/model",
		path: "/model",
		getParentRoute: () => Route$4
	}),
	PredictorRoute: Route.update({
		id: "/predictor",
		path: "/predictor",
		getParentRoute: () => Route$4
	})
};
var routeTree = Route$4._addFileChildren(rootRouteChildren)._addFileTypes();
var router_exports = /* @__PURE__ */ __exportAll({ getRouter: () => getRouter });
var getRouter = () => {
	const queryClient = new QueryClient();
	return createRouter({
		routeTree,
		context: { queryClient },
		scrollRestoration: true,
		defaultPreloadStaleTime: 0
	});
};
//#endregion
export { glassTooltip as n, router_exports as t };
