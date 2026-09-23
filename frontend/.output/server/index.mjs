globalThis.__nitro_main__ = import.meta.url;
import { n as HTTPError, r as defineLazyEventHandler, t as H3Core } from "./_libs/h3+rou3+srvx+unenv.mjs";
import { t as HookableCore } from "./_libs/hookable.mjs";
import { r as FastResponse } from "./_libs/h3-v2+rou3+srvx.mjs";
//#region #nitro-vite-setup
function lazyService(loader) {
	let promise, mod;
	return { fetch(req) {
		if (mod) return mod.fetch(req);
		if (!promise) promise = loader().then((_mod) => mod = _mod.default || _mod);
		return promise.then((mod) => mod.fetch(req));
	} };
}
var services = { ["ssr"]: lazyService(() => import("./_ssr/ssr.mjs")) };
globalThis.__nitro_vite_envs__ = services;
//#endregion
//#region #nitro/virtual/public-assets-data
var public_assets_data_default = {
	"/assets/gauge-DCOWsYze.js": {
		"type": "text/javascript; charset=utf-8",
		"etag": "\"2f8-sYbmJ2ZebsXxkvBVzweu6F7F4fw\"",
		"mtime": "2026-09-16T12:13:08.976Z",
		"size": 760,
		"path": "../public/assets/gauge-DCOWsYze.js"
	},
	"/assets/api-CSO70L5m.js": {
		"type": "text/javascript; charset=utf-8",
		"etag": "\"3b69-IEYAVbr2LIOfhhFvpkoWl1NZbuw\"",
		"mtime": "2026-09-16T12:13:08.976Z",
		"size": 15209,
		"path": "../public/assets/api-CSO70L5m.js"
	},
	"/assets/1111-0ti_djOF.jpg": {
		"type": "image/jpeg",
		"etag": "\"abbf-mR/80YCTzSd+G0pXNQTfPT7KOdU\"",
		"mtime": "2026-09-16T12:13:08.994Z",
		"size": 43967,
		"path": "../public/assets/1111-0ti_djOF.jpg"
	},
	"/assets/GlassLayout-BLiXnhJY.js": {
		"type": "text/javascript; charset=utf-8",
		"etag": "\"10ca-NZr+Xxetk7fh+GECsHqjYnLpz54\"",
		"mtime": "2026-09-16T12:13:08.974Z",
		"size": 4298,
		"path": "../public/assets/GlassLayout-BLiXnhJY.js"
	},
	"/assets/generateCategoricalChart-DR80mIWI.js": {
		"type": "text/javascript; charset=utf-8",
		"etag": "\"59018-8mMtYSZqkLibLvQa1UpJWkxolJs\"",
		"mtime": "2026-09-16T12:13:08.976Z",
		"size": 364568,
		"path": "../public/assets/generateCategoricalChart-DR80mIWI.js"
	},
	"/assets/index-DnNapi4D.js": {
		"type": "text/javascript; charset=utf-8",
		"etag": "\"5585d-iqnRnguXfMsLjn4JsG5gv//kChY\"",
		"mtime": "2026-09-16T12:13:08.974Z",
		"size": 350301,
		"path": "../public/assets/index-DnNapi4D.js"
	},
	"/assets/layers-DNJ9mYJH.js": {
		"type": "text/javascript; charset=utf-8",
		"etag": "\"1a0-1EytIkg5HFAP6q6Lyu4uCYxaICM\"",
		"mtime": "2026-09-16T12:13:08.976Z",
		"size": 416,
		"path": "../public/assets/layers-DNJ9mYJH.js"
	},
	"/assets/model-DqHAUVWR.js": {
		"type": "text/javascript; charset=utf-8",
		"etag": "\"a76c-phcylkgssdbRbxRHyUpSm61EICQ\"",
		"mtime": "2026-09-16T12:13:08.976Z",
		"size": 42860,
		"path": "../public/assets/model-DqHAUVWR.js"
	},
	"/assets/routes-1BNS0EZQ.js": {
		"type": "text/javascript; charset=utf-8",
		"etag": "\"5451-mt2cuYU1UUFdmeX7ayBB+El5rLE\"",
		"mtime": "2026-09-16T12:13:08.994Z",
		"size": 21585,
		"path": "../public/assets/routes-1BNS0EZQ.js"
	},
	"/assets/predictor-Cn_7PwYn.js": {
		"type": "text/javascript; charset=utf-8",
		"etag": "\"1552e-PPJEiXzdwYrvF4+MaWQ5DKEMytc\"",
		"mtime": "2026-09-16T12:13:08.994Z",
		"size": 87342,
		"path": "../public/assets/predictor-Cn_7PwYn.js"
	},
	"/assets/shield-check-BPJvEJS1.js": {
		"type": "text/javascript; charset=utf-8",
		"etag": "\"13b-7ijl9aGUlRTcjExBKGY1tqHI7Og\"",
		"mtime": "2026-09-16T12:13:08.994Z",
		"size": 315,
		"path": "../public/assets/shield-check-BPJvEJS1.js"
	},
	"/assets/trending-up-D5KwGgwd.js": {
		"type": "text/javascript; charset=utf-8",
		"etag": "\"aa-CaWPP4mRz45qVhHXIRQTyv28ByA\"",
		"mtime": "2026-09-16T12:13:08.994Z",
		"size": 170,
		"path": "../public/assets/trending-up-D5KwGgwd.js"
	},
	"/assets/zap-BdNJTCBN.js": {
		"type": "text/javascript; charset=utf-8",
		"etag": "\"101-EpYlnWjgNUiPnqIKllw2kiOdJGY\"",
		"mtime": "2026-09-16T12:13:08.994Z",
		"size": 257,
		"path": "../public/assets/zap-BdNJTCBN.js"
	},
	"/assets/boy_happy-BiLS1N1H.jpg": {
		"type": "image/jpeg",
		"etag": "\"d1a80-4L50YDSVqDwfPkg7D4OeU9STdlA\"",
		"mtime": "2026-09-16T12:13:08.996Z",
		"size": 858752,
		"path": "../public/assets/boy_happy-BiLS1N1H.jpg"
	},
	"/assets/boy_sad-DqJcWKls.jpg": {
		"type": "image/jpeg",
		"etag": "\"bcbbe-+IimgRRhN+vOeTim+M0DOelQlLw\"",
		"mtime": "2026-09-16T12:13:08.996Z",
		"size": 773054,
		"path": "../public/assets/boy_sad-DqJcWKls.jpg"
	},
	"/assets/styles-C1pI9BoX.css": {
		"type": "text/css; charset=utf-8",
		"etag": "\"15d6a-w3e87v8rrfMWcXbgq/SRk9CHbsY\"",
		"mtime": "2026-09-16T12:13:08.998Z",
		"size": 89450,
		"path": "../public/assets/styles-C1pI9BoX.css"
	},
	"/assets/girl_happy-Bkt34BzN.jpg": {
		"type": "image/jpeg",
		"etag": "\"dcf61-0ikoFqM0tR39N1IyO0yhGiFak7w\"",
		"mtime": "2026-09-16T12:13:08.996Z",
		"size": 905057,
		"path": "../public/assets/girl_happy-Bkt34BzN.jpg"
	},
	"/assets/girl_sad-Cza0DjJ_.jpg": {
		"type": "image/jpeg",
		"etag": "\"cbc0b-N7isWDt9A2IjZeEY13oviBN0578\"",
		"mtime": "2026-09-16T12:13:08.996Z",
		"size": 834571,
		"path": "../public/assets/girl_sad-Cza0DjJ_.jpg"
	},
	"/assets/indian-bride-groom-VwRk2ilA.jpg": {
		"type": "image/jpeg",
		"etag": "\"f6aa1-gu2TmJWj7GmzNmSH709dRKHfQIU\"",
		"mtime": "2026-09-16T12:13:08.998Z",
		"size": 1010337,
		"path": "../public/assets/indian-bride-groom-VwRk2ilA.jpg"
	},
	"/assets/indian-wedding-hero-IYmWfBLA.jpg": {
		"type": "image/jpeg",
		"etag": "\"103649-vboKkFVfi+wRkw1j/Er5dZrGAqw\"",
		"mtime": "2026-09-16T12:13:08.998Z",
		"size": 1062473,
		"path": "../public/assets/indian-wedding-hero-IYmWfBLA.jpg"
	}
};
//#endregion
//#region #nitro/virtual/public-assets
var publicAssetBases = {};
function isPublicAssetURL(id = "") {
	if (public_assets_data_default[id]) return true;
	for (const base in publicAssetBases) if (id.startsWith(base)) return true;
	return false;
}
//#endregion
//#region node_modules/nitro/dist/runtime/internal/route-rules.mjs
var headers = ((m) => function headersRouteRule(event) {
	for (const [key, value] of Object.entries(m.options || {})) event.res.headers.set(key, value);
});
//#endregion
//#region #nitro/virtual/routing
var findRouteRules = /* @__PURE__ */ (() => {
	const $0 = [{
		name: "headers",
		route: "/assets/**",
		handler: headers,
		options: { "cache-control": "public, max-age=31536000, immutable" }
	}];
	return (m, p) => {
		let r = [];
		if (p.charCodeAt(p.length - 1) === 47) p = p.slice(0, -1) || "/";
		let s = p.split("/");
		if (s.length > 1) {
			if (s[1] === "assets") r.unshift({
				data: $0,
				params: { "_": s.slice(2).join("/") }
			});
		}
		return r;
	};
})();
var _lazy_IN5eH1 = defineLazyEventHandler(() => import("./_chunks/ssr-renderer.mjs"));
var findRoute = /* @__PURE__ */ (() => {
	const data = {
		route: "/**",
		handler: _lazy_IN5eH1
	};
	return ((_m, p) => {
		return {
			data,
			params: { "_": p.slice(1) }
		};
	});
})();
[].filter(Boolean);
//#endregion
//#region node_modules/nitro/dist/runtime/internal/error/prod.mjs
var errorHandler = (error, event) => {
	const res = defaultHandler(error, event);
	return new FastResponse(typeof res.body === "string" ? res.body : JSON.stringify(res.body, null, 2), res);
};
function defaultHandler(error, event) {
	const unhandled = error.unhandled ?? !HTTPError.isError(error);
	const { status = 500, statusText = "" } = unhandled ? {} : error;
	if (status === 404) {
		const url = event.url || new URL(event.req.url);
		const baseURL = "/";
		if (/^\/[^/]/.test(baseURL) && !url.pathname.startsWith(baseURL)) return {
			status: 302,
			headers: new Headers({ location: `${baseURL}${url.pathname.slice(1)}${url.search}` })
		};
	}
	const headers = new Headers(unhandled ? {} : error.headers);
	headers.set("content-type", "application/json; charset=utf-8");
	return {
		status,
		statusText,
		headers,
		body: {
			error: true,
			...unhandled ? {
				status,
				unhandled: true
			} : typeof error.toJSON === "function" ? error.toJSON() : {
				status,
				statusText,
				message: error.message
			}
		}
	};
}
//#endregion
//#region #nitro/virtual/error-handler
var errorHandlers = [errorHandler];
async function error_handler_default(error, event) {
	for (const handler of errorHandlers) try {
		const response = await handler(error, event, { defaultHandler });
		if (response) return response;
	} catch (error) {
		console.error(error);
	}
}
//#endregion
//#region #nitro/virtual/app
function createNitroApp() {
	const captureError = (error, errorCtx) => {
		if (errorCtx?.event) {
			const errors = errorCtx.event.req.context?.nitro?.errors;
			if (errors) errors.push({
				error,
				context: errorCtx
			});
		}
	};
	const h3App = createH3App({ onError(error, event) {
		return error_handler_default(error, event);
	} });
	let appHandler = (req) => {
		req.context ||= {};
		req.context.nitro = req.context.nitro || { errors: [] };
		return h3App.fetch(req);
	};
	return {
		fetch: appHandler,
		h3: h3App,
		hooks: void 0,
		captureError
	};
}
function createH3App(config) {
	const h3App = new H3Core(config);
	h3App["~findRoute"] = (event) => findRoute(event.req.method, event.url.pathname);
	h3App["~getMiddleware"] = (event, route) => {
		const pathname = event.url.pathname;
		const method = event.req.method;
		const middleware = [];
		const routeRules = getRouteRules(method, pathname);
		event.context.routeRules = routeRules?.routeRules;
		if (routeRules?.routeRuleMiddleware.length) middleware.push(...routeRules.routeRuleMiddleware);
		if (route?.data?.middleware?.length) middleware.push(...route.data.middleware);
		return middleware;
	};
	return h3App;
}
//#endregion
//#region node_modules/nitro/dist/runtime/internal/app.mjs
var APP_ID = "default";
function useNitroApp() {
	let instance = useNitroApp._instance;
	if (instance) return instance;
	instance = useNitroApp._instance = createNitroApp();
	globalThis.__nitro__ = globalThis.__nitro__ || {};
	globalThis.__nitro__[APP_ID] = instance;
	return instance;
}
function useNitroHooks() {
	const nitroApp = useNitroApp();
	const hooks = nitroApp.hooks;
	if (hooks) return hooks;
	return nitroApp.hooks = new HookableCore();
}
function getRouteRules(method, pathname) {
	const m = findRouteRules(method, pathname);
	if (!m?.length) return { routeRuleMiddleware: [] };
	const routeRules = {};
	for (const layer of m) for (const rule of layer.data) {
		const currentRule = routeRules[rule.name];
		if (currentRule) {
			if (rule.options === false) {
				delete routeRules[rule.name];
				continue;
			}
			if (typeof currentRule.options === "object" && typeof rule.options === "object") currentRule.options = {
				...currentRule.options,
				...rule.options
			};
			else currentRule.options = rule.options;
			currentRule.route = rule.route;
			currentRule.params = {
				...currentRule.params,
				...layer.params
			};
		} else if (rule.options !== false) routeRules[rule.name] = {
			...rule,
			params: layer.params
		};
	}
	const middleware = [];
	const orderedRules = Object.values(routeRules).sort((a, b) => (a.handler?.order || 0) - (b.handler?.order || 0));
	for (const rule of orderedRules) {
		if (rule.options === false || !rule.handler) continue;
		middleware.push(rule.handler(rule));
	}
	return {
		routeRules,
		routeRuleMiddleware: middleware
	};
}
//#endregion
//#region node_modules/nitro/dist/presets/cloudflare/runtime/_module-handler.mjs
function createHandler(hooks) {
	const nitroApp = useNitroApp();
	const nitroHooks = useNitroHooks();
	return {
		async fetch(request, env, context) {
			globalThis.__env__ = env;
			augmentReq(request, {
				env,
				context
			});
			const ctxExt = {};
			const url = new URL(request.url);
			if (hooks.fetch) {
				const res = await hooks.fetch(request, env, context, url, ctxExt);
				if (res) return res;
			}
			return await nitroApp.fetch(request);
		},
		scheduled(controller, env, context) {
			globalThis.__env__ = env;
			context.waitUntil(nitroHooks.callHook("cloudflare:scheduled", {
				controller,
				env,
				context
			}) || Promise.resolve());
		},
		email(message, env, context) {
			globalThis.__env__ = env;
			context.waitUntil(nitroHooks.callHook("cloudflare:email", {
				message,
				event: message,
				env,
				context
			}) || Promise.resolve());
		},
		queue(batch, env, context) {
			globalThis.__env__ = env;
			context.waitUntil(nitroHooks.callHook("cloudflare:queue", {
				batch,
				event: batch,
				env,
				context
			}) || Promise.resolve());
		},
		tail(traces, env, context) {
			globalThis.__env__ = env;
			context.waitUntil(nitroHooks.callHook("cloudflare:tail", {
				traces,
				env,
				context
			}) || Promise.resolve());
		},
		trace(traces, env, context) {
			globalThis.__env__ = env;
			context.waitUntil(nitroHooks.callHook("cloudflare:trace", {
				traces,
				env,
				context
			}) || Promise.resolve());
		}
	};
}
function augmentReq(cfReq, ctx) {
	const req = cfReq;
	req.ip = cfReq.headers.get("cf-connecting-ip") || void 0;
	req.runtime ??= { name: "cloudflare" };
	req.runtime.cloudflare = {
		...req.runtime.cloudflare,
		...ctx
	};
	req.waitUntil = ctx.context?.waitUntil.bind(ctx.context);
}
//#endregion
//#region node_modules/nitro/dist/presets/cloudflare/runtime/cloudflare-module.mjs
var cloudflare_module_default = createHandler({ fetch(cfRequest, env, context, url) {
	if (env.ASSETS && isPublicAssetURL(url.pathname)) return env.ASSETS.fetch(cfRequest);
} });
//#endregion
export { cloudflare_module_default as default };
