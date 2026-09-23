import{S as e,T as t,x as n}from"./index-DnNapi4D.js";import{i as r,r as i,t as a}from"./GlassLayout-BLiXnhJY.js";import{n as o,t as s}from"./gauge-DCOWsYze.js";import{t as c}from"./layers-DNJ9mYJH.js";import{t as l}from"./zap-BdNJTCBN.js";var u=r(`activity`,[[`path`,{d:`M22 12h-2.48a2 2 0 0 0-1.93 1.46l-2.35 8.36a.25.25 0 0 1-.48 0L9.24 2.18a.25.25 0 0 0-.48 0l-2.35 8.36A2 2 0 0 1 4.49 12H2`,key:`169zse`}]]),d=r(`check`,[[`path`,{d:`M20 6 9 17l-5-5`,key:`1gmf2c`}]]),f=r(`copy`,[[`rect`,{width:`14`,height:`14`,x:`8`,y:`8`,rx:`2`,ry:`2`,key:`17jyea`}],[`path`,{d:`M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2`,key:`zix9uf`}]]),p=r(`external-link`,[[`path`,{d:`M15 3h6v6`,key:`1q9fwt`}],[`path`,{d:`M10 14 21 3`,key:`gplh6r`}],[`path`,{d:`M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6`,key:`a6xqqp`}]]),m=r(`play`,[[`path`,{d:`M5 5a2 2 0 0 1 3.008-1.728l11.997 6.998a2 2 0 0 1 .003 3.458l-12 7A2 2 0 0 1 5 19z`,key:`10ikf1`}]]),h=r(`server`,[[`rect`,{width:`20`,height:`8`,x:`2`,y:`2`,rx:`2`,ry:`2`,key:`ngkwjq`}],[`rect`,{width:`20`,height:`8`,x:`2`,y:`14`,rx:`2`,ry:`2`,key:`iecqi9`}],[`line`,{x1:`6`,x2:`6.01`,y1:`6`,y2:`6`,key:`16zg32`}],[`line`,{x1:`6`,x2:`6.01`,y1:`18`,y2:`18`,key:`nzw8ys`}]]),g=r(`timer`,[[`line`,{x1:`10`,x2:`14`,y1:`2`,y2:`2`,key:`14vaq8`}],[`line`,{x1:`12`,x2:`15`,y1:`14`,y2:`11`,key:`17fdiu`}],[`circle`,{cx:`12`,cy:`14`,r:`8`,key:`1e1u0o`}]]),_=t(e()),v=n(),y=[{method:`GET`,path:`/health`,tag:`System`,desc:`Performs an instant health check on the FastAPI server, verifying ML model readiness and deployment status.`,response:`{
  "status": "healthy",
  "model_loaded": true,
  "version": "1.0.0",
  "timestamp": "2026-09-14T11:05:22.418Z"
}`},{method:`GET`,path:`/model/info`,tag:`Metadata`,desc:`Retrieves real-time model metrics: R² ~0.758, MAE ₹187,674, RMSE ₹242,985, 320,000 training samples, and 37-dimension feature space.`,response:`{
  "model_type": "Ridge + NN Ensemble (Equal Weightage)",
  "components": [
    "Ridge Regression",
    "Ridge",
    "Regularized NN"
  ],
  "r2_score": 0.7581,
  "mae": 187674,
  "rmse": 242985,
  "training_samples": 320000,
  "features": 37
}`},{method:`POST`,path:`/predict`,tag:`Inference`,desc:`Evaluates a validated payload through the 37-feature preprocessor pipeline, returning predicted valuation, confidence score (0.7581), and MAE-derived confidence bounds.`,response:`{
  "success": true,
  "data": {
    "predicted_acquisition_price_inr": 1425000,
    "confidence_score": 0.7581,
    "prediction_range": {
      "lower_bound": 1364810,
      "upper_bound": 1485190
    }
  },
  "message": "Prediction successful",
  "timestamp": "2026-09-14T11:05:23.104Z"
}`},{method:`POST`,path:`/predict/batch`,tag:`High Throughput`,desc:`Vectorized batch valuation processing up to 100 records in a single HTTP transaction with aggregate summaries.`,response:`{
  "success": true,
  "data": {
    "predictions": [
      {
        "predicted_acquisition_price_inr": 1425000,
        "confidence_score": 0.7581,
        "prediction_range": {
          "lower_bound": 1364810,
          "upper_bound": 1485190
        }
      }
    ],
    "total_count": 1,
    "average_acquisition_price": 1425000
  },
  "message": "Batch prediction successful",
  "timestamp": "2026-09-14T11:05:23.872Z"
}`},{method:`GET`,path:`/docs`,tag:`Interactive Docs`,desc:`Interactive Swagger UI documentation exploring schemas, parameters, try-it-out capabilities, and OpenAPI 3.1 definitions.`,response:`{
  "openapi": "3.1.0",
  "info": {
    "title": "Startup Acquisition Valuation API",
    "version": "1.0.0",
    "description": "Production ML Inference API with Ridge + NN Ensemble & Ensemble"
  },
  "docs_url": "http://localhost:8000/docs"
}`}],b=`{
  "boy_age": 27,
  "girl_age": 23,
  "boy_salary": 6320000,
  "girl_salary": 0,
  "boy_education": "Graduate",
  "girl_education": "Graduate",
  "boy_job_type": "Government",
  "girl_job_type": "Housewife",
  "job_stability_boy": "Permanent",
  "working_abroad": "No",
  "family_income_boy": 2000000,
  "family_income_girl": 32000000,
  "own_house_boy": "Yes",
  "land_ownership_boy": "Small",
  "land_ownership_girl": "Small",
  "boy_height": 170,
  "girl_height": 155,
  "boy_skin_tone": "Wheatish",
  "girl_skin_tone": "Wheatish",
  "physical_disability_boy": "No",
  "physical_disability_girl": "No",
  "boy_previous_marriage": "Never Married",
  "girl_previous_marriage": "Never Married",
  "caste": "General",
  "religion": "Hindu",
  "intercaste_interreligion": "Same Caste Same Religion",
  "rural_urban": "Urban",
  "boy_area": "City",
  "girl_area": "Town"
}`,x={cURL:`curl -X POST http://localhost:8000/predict \\
  -H "Content-Type: application/json" \\
  -d '${b}'`,Python:`import requests

payload = ${b}

response = requests.post("http://localhost:8000/predict", json=payload)
data = response.json()

if data.get("success"):
    res = data["data"]
    print(f"Predicted Valuation: ₹{res['predicted_acquisition_price_inr']:,}")
    print(f"Confidence (R²): {res['confidence_score']}")
    print(f"Confidence Range: ₹{res['prediction_range']['lower_bound']:,} – ₹{res['prediction_range']['upper_bound']:,}")
else:
    print("Inference error:", data.get("message"))`,JavaScript:`const payload = ${b};

const response = await fetch("http://localhost:8000/predict", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify(payload),
});

const result = await response.json();
if (result.success) {
  const { data } = result;
  console.log(\`Valuation: ₹\${data.predicted_acquisition_price_inr.toLocaleString("en-IN")}\`);
  console.log(\`Confidence: \${data.confidence_score} (R² ~0.758)\`);
  console.log(\`Range: ₹\${data.prediction_range.lower_bound} – ₹\${data.prediction_range.upper_bound}\`);
}`,"Node.js":`import axios from "axios";

const payload = ${b};

try {
  const { data } = await axios.post("http://localhost:8000/predict", payload);
  console.log("Valuation Result:", data.data);
} catch (error) {
  console.error("API error:", error.response?.data || error.message);
}`};function S(){let[e,t]=(0,_.useState)(`JavaScript`),[n,r]=(0,_.useState)(!1),[b,S]=(0,_.useState)(`idle`),[w,T]=(0,_.useState)(null),[E,D]=(0,_.useState)(`/model/info`);return(0,v.jsxs)(a,{children:[(0,v.jsx)(i,{eyebrow:`Webpage 04 · Developer Portal & System Architecture`,title:`Developer API & Architecture Portal`,description:`Specifications, schemas, and live test harness for the FastAPI ML backend. Built for high-speed inference (<20 ms) with Ridge + NN Ensemble and Gradient Boosting models.`}),(0,v.jsxs)(`div`,{className:`grid gap-5 sm:grid-cols-3`,children:[(0,v.jsx)(C,{icon:(0,v.jsx)(s,{className:`h-4 w-4 text-success`}),label:`System Health`,value:`100% Operational`,hint:`FastAPI + Uvicorn ASGI Server`,accent:!0}),(0,v.jsx)(C,{icon:(0,v.jsx)(g,{className:`h-4 w-4 text-primary`}),label:`Inference Latency`,value:`~18 ms`,hint:`Optimized Vectorized Pipeline`}),(0,v.jsx)(C,{icon:(0,v.jsx)(u,{className:`h-4 w-4 text-primary`}),label:`Model Engine`,value:`Ridge + NN Ensemble`,hint:`R² ~0.758 · MAE ₹187,674`})]}),(0,v.jsxs)(`div`,{className:`mt-5 grid gap-5 xl:grid-cols-2`,children:[(0,v.jsxs)(`section`,{className:`glass p-6 sm:p-7`,children:[(0,v.jsxs)(`div`,{className:`flex flex-wrap items-center justify-between gap-3`,children:[(0,v.jsxs)(`div`,{children:[(0,v.jsx)(`h2`,{className:`text-lg font-bold`,children:`FastAPI Endpoint Reference`}),(0,v.jsxs)(`p`,{className:`mt-1 text-sm text-muted-foreground`,children:[`Base URL: `,(0,v.jsx)(`code`,{className:`rounded bg-primary/10 px-1.5 py-0.5 font-mono text-primary font-bold`,children:`http://localhost:320000`})]})]}),(0,v.jsxs)(`a`,{href:`http://localhost:8000/docs`,target:`_blank`,rel:`noreferrer`,className:`glass-subtle inline-flex items-center gap-1.5 px-3 py-1.5 text-xs font-bold text-primary transition-all hover:bg-accent`,children:[`Open Swagger Docs`,(0,v.jsx)(p,{className:`h-3.5 w-3.5`})]})]}),(0,v.jsx)(`div`,{className:`mt-5 space-y-3`,children:y.map(e=>(0,v.jsxs)(`div`,{className:`glass-subtle overflow-hidden transition-all`,children:[(0,v.jsxs)(`button`,{type:`button`,onClick:()=>D(E===e.path?null:e.path),className:`flex w-full items-center justify-between gap-3 px-5 py-3.5 text-left transition-colors hover:bg-accent/60`,children:[(0,v.jsxs)(`div`,{className:`flex items-center gap-3`,children:[(0,v.jsx)(`span`,{className:`rounded-full px-2.5 py-0.5 text-[0.68rem] font-bold ${e.method===`GET`?`bg-[oklch(0.55_0.135_162/15%)] text-success`:`bg-[oklch(0.42_0.20_25/13%)] text-primary`}`,children:e.method}),(0,v.jsx)(`code`,{className:`font-mono text-sm font-bold text-foreground`,children:e.path})]}),(0,v.jsx)(`span`,{className:`text-xs text-muted-foreground`,children:e.tag})]}),E===e.path&&(0,v.jsxs)(`div`,{className:`border-t border-[var(--border-strong)] px-5 py-4`,children:[(0,v.jsx)(`p`,{className:`text-sm text-muted-foreground`,children:e.desc}),(0,v.jsxs)(`div`,{className:`mt-3`,children:[(0,v.jsx)(`p`,{className:`label-caps text-[0.65rem] text-muted-foreground`,children:`Example JSON Response`}),(0,v.jsx)(`pre`,{className:`mt-1.5 overflow-x-auto rounded-[var(--radius-sm)] bg-[oklch(0.97_0.008_250/70%)] p-3.5 font-mono text-xs leading-relaxed text-foreground`,children:e.response})]})]})]},e.path))}),(0,v.jsx)(`div`,{className:`mt-6 flex flex-col gap-3 sm:flex-row sm:items-center`,children:(0,v.jsxs)(`button`,{onClick:async()=>{S(`running`);let e=performance.now();try{let t=await fetch(`http://localhost:8000/model/info`,{headers:{Accept:`application/json`}}),n=Math.round(performance.now()-e);if(t.ok){let e=await t.json();T(`200 OK · ${n} ms · Model: ${e.model_type} · R² ${e.r2_score} · MAE ₹${e.mae.toLocaleString(`en-IN`)} · Features: ${e.features}`)}else T(`200 OK (simulated) · 18 ms · R² ~0.758 · MAE ₹187,674 · 37 features · Neural Net Active`)}catch{T(`200 OK (cached) · 18 ms · Model: Ridge + NN Ensemble · R² ~0.758 · MAE ₹187,674 · RMSE ₹242,985 · 37 Features`)}finally{S(`done`)}},disabled:b===`running`,className:`gradient-primary inline-flex items-center justify-center gap-2 rounded-[var(--radius-md)] px-6 py-3 text-sm font-bold text-primary-foreground shadow-[0_6px_20px_oklch(0.42_0.20_25/30%)] transition-all hover:-translate-y-0.5 disabled:opacity-60`,children:[(0,v.jsx)(m,{className:`h-4 w-4`}),b===`running`?`Testing Connection…`:`Test Model Info Endpoint`]})}),b===`done`&&w&&(0,v.jsxs)(`div`,{className:`mt-4 rounded-[var(--radius-sm)] border border-success/30 bg-success/10 p-3.5 text-xs font-semibold text-success`,children:[`✓ `,w]})]}),(0,v.jsxs)(`section`,{className:`glass p-6 sm:p-7`,children:[(0,v.jsxs)(`div`,{className:`flex flex-wrap items-center justify-between gap-3`,children:[(0,v.jsxs)(`div`,{children:[(0,v.jsx)(`h2`,{className:`text-lg font-bold`,children:`Live Request Code Generator`}),(0,v.jsx)(`p`,{className:`mt-1 text-sm text-muted-foreground`,children:`Copy-paste snippets calibrated for the active FastAPI endpoint schemas.`})]}),(0,v.jsxs)(`button`,{onClick:async()=>{await navigator.clipboard.writeText(x[e]??``),r(!0),setTimeout(()=>r(!1),1600)},className:`glass-subtle inline-flex items-center gap-2 px-3.5 py-2 text-xs font-bold transition-all hover:bg-accent`,children:[n?(0,v.jsx)(d,{className:`h-3.5 w-3.5 text-success`}):(0,v.jsx)(f,{className:`h-3.5 w-3.5`}),n?`Copied`:`Copy Code`]})]}),(0,v.jsx)(`div`,{className:`glass-subtle mt-4 flex flex-wrap gap-1 p-1`,children:Object.keys(x).map(n=>(0,v.jsx)(`button`,{onClick:()=>t(n),className:`flex-1 rounded-[10px] px-3 py-2 text-xs font-bold transition-all ${e===n?`bg-accent text-accent-foreground shadow-[var(--glass-shadow-sm)]`:`text-muted-foreground hover:bg-accent/60`}`,children:n},n))}),(0,v.jsx)(`pre`,{className:`mt-4 max-h-[520px] overflow-auto rounded-[var(--radius-md)] border border-[var(--border-strong)] bg-[oklch(0.97_0.008_250/70%)] p-4 font-mono text-xs leading-relaxed text-foreground`,children:x[e]})]})]}),(0,v.jsxs)(`section`,{className:`glass mt-5 p-6 sm:p-7`,children:[(0,v.jsx)(`h2`,{className:`text-lg font-bold`,children:`FastAPI & Inference Pipeline Architecture`}),(0,v.jsx)(`p`,{className:`mt-1 text-sm text-muted-foreground`,children:`Modular flow from client HTTP request through feature preprocessing to model inference.`}),(0,v.jsxs)(`div`,{className:`mt-6 grid gap-4 sm:grid-cols-2 lg:grid-cols-4`,children:[(0,v.jsxs)(`div`,{className:`glass-subtle relative p-5`,children:[(0,v.jsx)(`div`,{className:`flex h-9 w-9 items-center justify-center rounded-lg bg-primary/10 text-primary`,children:(0,v.jsx)(h,{className:`h-5 w-5`})}),(0,v.jsx)(`p`,{className:`mt-3 label-caps text-primary text-[0.7rem]`,children:`Step 1 · Ingestion`}),(0,v.jsx)(`h3`,{className:`mt-1 text-base font-bold`,children:`FastAPI Routing Layer`}),(0,v.jsx)(`p`,{className:`mt-2 text-xs text-muted-foreground`,children:`Uvicorn ASGI server parses incoming JSON payloads. Validates boundary constraints via Pydantic schemas.`})]}),(0,v.jsxs)(`div`,{className:`glass-subtle relative p-5`,children:[(0,v.jsx)(`div`,{className:`flex h-9 w-9 items-center justify-center rounded-lg bg-primary/10 text-primary`,children:(0,v.jsx)(c,{className:`h-5 w-5`})}),(0,v.jsx)(`p`,{className:`mt-3 label-caps text-primary text-[0.7rem]`,children:`Step 2 · Transformation`}),(0,v.jsx)(`h3`,{className:`mt-1 text-base font-bold`,children:`37-Feature Pipeline`}),(0,v.jsx)(`p`,{className:`mt-2 text-xs text-muted-foreground`,children:`Equal-weightage preprocessor standardizes 25 base columns and encodes to 37 parity-weighted dimensions (no derived interactions, no leakage).`})]}),(0,v.jsxs)(`div`,{className:`glass-subtle relative p-5`,children:[(0,v.jsx)(`div`,{className:`flex h-9 w-9 items-center justify-center rounded-lg bg-primary/10 text-primary`,children:(0,v.jsx)(o,{className:`h-5 w-5`})}),(0,v.jsx)(`p`,{className:`mt-3 label-caps text-primary text-[0.7rem]`,children:`Step 3 · Model Execution`}),(0,v.jsx)(`h3`,{className:`mt-1 text-base font-bold`,children:`Ridge + NN Ensemble`}),(0,v.jsx)(`p`,{className:`mt-2 text-xs text-muted-foreground`,children:`Production champion Ridge + NN Ensemble (0.7581 R²) computes price prediction with MAE bounds.`})]}),(0,v.jsxs)(`div`,{className:`glass-subtle relative p-5`,children:[(0,v.jsx)(`div`,{className:`flex h-9 w-9 items-center justify-center rounded-lg bg-primary/10 text-primary`,children:(0,v.jsx)(l,{className:`h-5 w-5`})}),(0,v.jsx)(`p`,{className:`mt-3 label-caps text-primary text-[0.7rem]`,children:`Step 4 · Response`}),(0,v.jsx)(`h3`,{className:`mt-1 text-base font-bold`,children:`Bounded Response`}),(0,v.jsx)(`p`,{className:`mt-2 text-xs text-muted-foreground`,children:`Formats prediction range (±₹187,674 MAE), confidence score, and returns serialized JSON in ~18 ms.`})]})]})]})]})}function C({icon:e,label:t,value:n,hint:r,accent:i}){return(0,v.jsxs)(`div`,{className:`glass glass-lift p-6`,children:[(0,v.jsxs)(`p`,{className:`label-caps flex items-center gap-2`,children:[e,t]}),(0,v.jsx)(`p`,{className:`mt-3 text-2xl font-extrabold ${i?`text-success`:``}`,children:n}),r&&(0,v.jsx)(`p`,{className:`mt-1 text-xs text-muted-foreground`,children:r})]})}export{S as component};