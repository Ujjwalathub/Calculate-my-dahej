import { i as __toESM } from "../_runtime.mjs";
import { a as require_react, i as require_jsx_runtime, n as useQuery, t as useMutation } from "../_libs/react+tanstack__react-query.mjs";
import { n as HeroImage, t as GlassLayout } from "./GlassLayout-lP339Oao.mjs";
import { A as Building, E as ChevronLeft, T as ChevronRight, a as Sparkles, d as Scale, f as RefreshCw, g as Heart, h as Layers, n as User, o as Smile, r as TrendingUp, u as Send, v as Frown } from "../_libs/lucide-react.mjs";
import { _ as Legend, g as Tooltip, h as ResponsiveContainer, l as Area, m as Cell, o as YAxis, p as Pie, r as PieChart, s as XAxis, t as AreaChart } from "../_libs/recharts+[...].mjs";
import { n as glassTooltip } from "./router-BvBGGSaB.mjs";
//#region node_modules/.nitro/vite/services/ssr/assets/predictor-DA1vVwkW.js
var import_react = /* @__PURE__ */ __toESM(require_react());
var import_jsx_runtime = require_jsx_runtime();
var indian_bride_groom_default = "/assets/indian-bride-groom-VwRk2ilA.jpg";
var boy_happy_default = "/assets/boy_happy-BiLS1N1H.jpg";
var boy_sad_default = "/assets/boy_sad-DqJcWKls.jpg";
var girl_happy_default = "/assets/girl_happy-Bkt34BzN.jpg";
var girl_sad_default = "/assets/girl_sad-Cza0DjJ_.jpg";
/**
* API Service for Backend Communication
* Handles all HTTP requests to the FastAPI backend
*/
var API_BASE_URL = {
	"BASE_URL": "/",
	"DEV": false,
	"MODE": "production",
	"PROD": true,
	"SSR": true,
	"TSS_DEV_SERVER": "false",
	"TSS_DEV_SSR_STYLES_BASEPATH": "/",
	"TSS_DEV_SSR_STYLES_ENABLED": "true",
	"TSS_DISABLE_CSRF_MIDDLEWARE_WARNING": "false",
	"TSS_INLINE_CSS_ENABLED": "false",
	"TSS_ROUTER_BASEPATH": "",
	"TSS_SERVER_FN_BASE": "/_serverFn/",
	"VITE_API_URL": "http://localhost:8000"
}["VITE_API_URL"] || "http://localhost:8000";
var APIService = class {
	baseURL;
	constructor(baseURL = API_BASE_URL) {
		this.baseURL = baseURL;
	}
	async request(endpoint, options = {}) {
		const url = `${this.baseURL}${endpoint}`;
		try {
			const response = await fetch(url, {
				...options,
				headers: {
					"Content-Type": "application/json",
					...options.headers
				}
			});
			if (!response.ok) {
				const errorData = await response.json().catch(() => ({}));
				throw new Error(errorData.message || errorData.detail || `HTTP ${response.status}: ${response.statusText}`);
			}
			return await response.json();
		} catch (error) {
			if (error instanceof Error) throw error;
			throw new Error("An unexpected error occurred");
		}
	}
	/**
	* Health check endpoint
	*/
	async health() {
		return this.request("/health");
	}
	/**
	* Get model information
	*/
	async getModelInfo() {
		return this.request("/model/info");
	}
	/**
	* Predict dowry / acquisition price for a single profile.
	* The backend accepts the flat profile object directly (it infers
	* dowry-vs-startup by shape, `payload_type` optional).
	*/
	async predictSingle(data) {
		const body = "payload_type" in data && data.payload_type ? data : {
			payload_type: "dowry",
			...data
		};
		return this.request("/predict", {
			method: "POST",
			body: JSON.stringify(body)
		});
	}
	/**
	* Predict valuations for multiple profiles (batch).
	* The backend `BatchPredictionRequest` expects `{ items: [...] }`
	* (legacy `startups` alias is startup-only) and infers each item's
	* type by shape, so send items WITH the explicit discriminator.
	*/
	async predictBatch(items) {
		if (items.length > 100) throw new Error("Maximum 100 items allowed per batch");
		const tagged = items.map((item) => "payload_type" in item && item.payload_type ? item : {
			payload_type: "dowry",
			...item
		});
		return this.request("/predict/batch", {
			method: "POST",
			body: JSON.stringify({ items: tagged })
		});
	}
	/**
	* Simple ping test
	*/
	async ping() {
		return this.request("/ping");
	}
};
var api = new APIService();
/**
* Hook for making single predictions
*/
function usePrediction() {
	return useMutation({ mutationFn: (data) => api.predictSingle(data) });
}
/**
* Hook for checking API health
*/
function useApiHealth() {
	return useQuery({
		queryKey: ["apiHealth"],
		queryFn: () => api.health(),
		refetchInterval: 3e4,
		retry: 1
	});
}
var inr = (v) => "₹" + Math.round(v).toLocaleString("en-IN", { maximumFractionDigits: 0 });
var lakhOrCrore = (v) => v >= 1e7 ? `₹${(v / 1e7).toFixed(2)} Cr` : `₹${(v / 1e5).toFixed(2)} L`;
var GROOM_PRESETS = [
	{
		name: "Govt Officer (Gazetted/IAS)",
		icon: "🏛️",
		data: {
			boy_age: 28,
			boy_salary: 11e4,
			boy_education: "Post Graduate",
			boy_job_type: "Government",
			job_stability_boy: "Permanent",
			working_abroad: "No",
			family_income_boy: 25e5,
			own_house_boy: "Yes",
			land_ownership_boy: "Medium",
			boy_height: 172,
			boy_skin_tone: "Fair",
			physical_disability_boy: "No",
			boy_previous_marriage: "Never Married",
			boy_area: "City",
			caste: "General"
		}
	},
	{
		name: "NRI Tech Lead (USA/EU)",
		icon: "💻",
		data: {
			boy_age: 29,
			boy_salary: 22e4,
			boy_education: "Post Graduate",
			boy_job_type: "Private",
			job_stability_boy: "Permanent",
			working_abroad: "Yes",
			family_income_boy: 32e5,
			own_house_boy: "Yes",
			land_ownership_boy: "Large",
			boy_height: 176,
			boy_skin_tone: "Wheatish",
			physical_disability_boy: "No",
			boy_previous_marriage: "Never Married",
			boy_area: "City",
			caste: "General"
		}
	},
	{
		name: "Corporate Professional (MNC)",
		icon: "🏢",
		data: {
			boy_age: 27,
			boy_salary: 72e3,
			boy_education: "Graduate",
			boy_job_type: "Private",
			job_stability_boy: "Permanent",
			working_abroad: "No",
			family_income_boy: 18e5,
			own_house_boy: "Yes",
			land_ownership_boy: "Small",
			boy_height: 170,
			boy_skin_tone: "Wheatish",
			physical_disability_boy: "No",
			boy_previous_marriage: "Never Married",
			boy_area: "City",
			caste: "OBC"
		}
	},
	{
		name: "Established Business Family",
		icon: "📈",
		data: {
			boy_age: 28,
			boy_salary: 15e4,
			boy_education: "Graduate",
			boy_job_type: "Business",
			job_stability_boy: "Business",
			working_abroad: "No",
			family_income_boy: 38e5,
			own_house_boy: "Yes",
			land_ownership_boy: "Large",
			boy_height: 172,
			boy_skin_tone: "Medium",
			physical_disability_boy: "No",
			boy_previous_marriage: "Never Married",
			boy_area: "Town",
			caste: "General"
		}
	}
];
var BRIDE_PRESETS = [
	{
		name: "Govt Officer (Gazetted/IAS)",
		icon: "🏛️",
		data: {
			girl_age: 26,
			girl_salary: 95e3,
			girl_education: "Post Graduate",
			girl_job_type: "Government",
			family_income_girl: 24e5,
			land_ownership_girl: "Medium",
			girl_height: 158,
			girl_skin_tone: "Fair",
			physical_disability_girl: "No",
			girl_previous_marriage: "Never Married",
			girl_area: "City",
			caste: "General"
		}
	},
	{
		name: "NRI Tech Lead (USA/EU)",
		icon: "💻",
		data: {
			girl_age: 27,
			girl_salary: 19e4,
			girl_education: "Post Graduate",
			girl_job_type: "Private",
			family_income_girl: 3e6,
			land_ownership_girl: "Medium",
			girl_height: 162,
			girl_skin_tone: "Fair",
			physical_disability_girl: "No",
			girl_previous_marriage: "Never Married",
			girl_area: "City",
			caste: "General"
		}
	},
	{
		name: "Corporate Professional (MNC)",
		icon: "🏢",
		data: {
			girl_age: 24,
			girl_salary: 65e3,
			girl_education: "Graduate",
			girl_job_type: "Private",
			family_income_girl: 13e5,
			land_ownership_girl: "Small",
			girl_height: 155,
			girl_skin_tone: "Wheatish",
			physical_disability_girl: "No",
			girl_previous_marriage: "Never Married",
			girl_area: "City",
			caste: "OBC"
		}
	},
	{
		name: "Established Business Family",
		icon: "📈",
		data: {
			girl_age: 24,
			girl_salary: 11e4,
			girl_education: "Graduate",
			girl_job_type: "Business",
			family_income_girl: 34e5,
			land_ownership_girl: "Large",
			girl_height: 156,
			girl_skin_tone: "Fair",
			physical_disability_girl: "No",
			girl_previous_marriage: "Never Married",
			girl_area: "Town",
			caste: "General"
		}
	}
];
var EDU_OPTIONS = [
	"Illiterate",
	"Primary",
	"Middle",
	"Secondary",
	"Higher Secondary",
	"Graduate",
	"Post Graduate",
	"Doctorate"
];
var BOY_JOB_OPTIONS = [
	"Government",
	"Private",
	"Business",
	"Farmer",
	"Unemployed"
];
var GIRL_JOB_OPTIONS = [
	"Housewife",
	"Private",
	"Government",
	"Business",
	"Student"
];
var JOB_STABILITY_OPTIONS = [
	"Permanent",
	"Business",
	"Contract",
	"Unstable",
	"Unemployed"
];
var LAND_OPTIONS = [
	"None",
	"Small",
	"Medium",
	"Large"
];
var SKIN_TONE_OPTIONS = [
	"Fair",
	"Wheatish",
	"Medium",
	"Dark"
];
var MARITAL_OPTIONS = [
	"Never Married",
	"Divorced",
	"Widowed"
];
var AREA_OPTIONS = [
	"City",
	"Town",
	"Village"
];
var RURAL_URBAN_OPTIONS = [
	"Urban",
	"Semi-Urban",
	"Rural"
];
var CASTE_OPTIONS = [
	"General",
	"OBC",
	"SC",
	"ST",
	"Other"
];
var RELIGION_OPTIONS = [
	"Hindu",
	"Muslim",
	"Sikh",
	"Christian",
	"Other"
];
var COMPATIBILITY_OPTIONS = [
	"Same Caste Same Religion",
	"Intercaste",
	"Interreligion",
	"Both"
];
var TIER_OPTIONS = [
	"Low",
	"Medium",
	"High",
	"Very High"
];
var YES_NO = ["No", "Yes"];
function PredictorPage() {
	const [activeTab, setActiveTab] = (0, import_react.useState)("groom");
	const [boyAge, setBoyAge] = (0, import_react.useState)(27);
	const [boySalary, setBoySalary] = (0, import_react.useState)(68e3);
	const [boyEducation, setBoyEducation] = (0, import_react.useState)("Graduate");
	const [boyJobType, setBoyJobType] = (0, import_react.useState)("Government");
	const [jobStabilityBoy, setJobStabilityBoy] = (0, import_react.useState)("Permanent");
	const [workingAbroad, setWorkingAbroad] = (0, import_react.useState)("No");
	const [familyIncomeBoy, setFamilyIncomeBoy] = (0, import_react.useState)(2e6);
	const [ownHouseBoy, setOwnHouseBoy] = (0, import_react.useState)("Yes");
	const [landOwnershipBoy, setLandOwnershipBoy] = (0, import_react.useState)("Small");
	const [boyHeight, setBoyHeight] = (0, import_react.useState)(170);
	const [boySkinTone, setBoySkinTone] = (0, import_react.useState)("Wheatish");
	const [physicalDisabilityBoy, setPhysicalDisabilityBoy] = (0, import_react.useState)("No");
	const [boyPrevMarriage, setBoyPrevMarriage] = (0, import_react.useState)("Never Married");
	const [boyArea, setBoyArea] = (0, import_react.useState)("City");
	const [girlAge, setGirlAge] = (0, import_react.useState)(23);
	const [girlSalary, setGirlSalary] = (0, import_react.useState)(0);
	const [girlEducation, setGirlEducation] = (0, import_react.useState)("Graduate");
	const [girlJobType, setGirlJobType] = (0, import_react.useState)("Housewife");
	const [familyIncomeGirl, setFamilyIncomeGirl] = (0, import_react.useState)(8e5);
	const [landOwnershipGirl, setLandOwnershipGirl] = (0, import_react.useState)("Small");
	const [girlHeight, setGirlHeight] = (0, import_react.useState)(155);
	const [girlSkinTone, setGirlSkinTone] = (0, import_react.useState)("Wheatish");
	const [physicalDisabilityGirl, setPhysicalDisabilityGirl] = (0, import_react.useState)("No");
	const [girlPrevMarriage, setGirlPrevMarriage] = (0, import_react.useState)("Never Married");
	const [girlArea, setGirlArea] = (0, import_react.useState)("Town");
	const [caste, setCaste] = (0, import_react.useState)("General");
	const [religion, setReligion] = (0, import_react.useState)("Hindu");
	const [intercasteInterreligion, setIntercasteInterreligion] = (0, import_react.useState)("Same Caste Same Religion");
	const [ruralUrban, setRuralUrban] = (0, import_react.useState)("Urban");
	const [valuationTier, setValuationTier] = (0, import_react.useState)("Medium");
	const prediction = usePrediction();
	const { data: healthData } = useApiHealth();
	const [backendResult, setBackendResult] = (0, import_react.useState)(null);
	const executePrediction = (0, import_react.useCallback)(() => {
		const payload = {
			boy_age: boyAge,
			girl_age: girlAge,
			age_difference: Math.max(0, boyAge - girlAge),
			boy_salary: boySalary,
			girl_salary: girlSalary,
			boy_education: boyEducation,
			girl_education: girlEducation,
			boy_job_type: boyJobType,
			girl_job_type: girlJobType,
			job_stability_boy: jobStabilityBoy,
			working_abroad: workingAbroad,
			family_income_boy: familyIncomeBoy,
			family_income_girl: familyIncomeGirl,
			own_house_boy: ownHouseBoy,
			land_ownership_boy: landOwnershipBoy,
			land_ownership_girl: landOwnershipGirl,
			boy_height: boyHeight,
			girl_height: girlHeight,
			boy_skin_tone: boySkinTone,
			girl_skin_tone: girlSkinTone,
			physical_disability_boy: physicalDisabilityBoy,
			physical_disability_girl: physicalDisabilityGirl,
			boy_previous_marriage: boyPrevMarriage,
			girl_previous_marriage: girlPrevMarriage,
			caste,
			religion,
			intercaste_interreligion: intercasteInterreligion,
			rural_urban: ruralUrban,
			boy_area: boyArea,
			girl_area: girlArea
		};
		prediction.mutate(payload, { onSuccess: (res) => {
			const val = res.data.predicted_dowry_amount_inr ?? res.data.predicted_acquisition_price_inr;
			setBackendResult({
				predicted: val,
				lower: res.data.prediction_range.lower_bound,
				upper: res.data.prediction_range.upper_bound,
				confidence: res.data.confidence_score
			});
		} });
	}, [
		boyAge,
		boySalary,
		boyEducation,
		boyJobType,
		jobStabilityBoy,
		workingAbroad,
		familyIncomeBoy,
		ownHouseBoy,
		landOwnershipBoy,
		boyHeight,
		boySkinTone,
		physicalDisabilityBoy,
		boyPrevMarriage,
		boyArea,
		girlAge,
		girlSalary,
		girlEducation,
		girlJobType,
		familyIncomeGirl,
		landOwnershipGirl,
		girlHeight,
		girlSkinTone,
		physicalDisabilityGirl,
		girlPrevMarriage,
		girlArea,
		caste,
		religion,
		intercasteInterreligion,
		ruralUrban,
		valuationTier,
		prediction
	]);
	(0, import_react.useEffect)(() => {
		executePrediction();
	}, []);
	const applyGroomPreset = (presetName) => {
		const preset = GROOM_PRESETS.find((p) => p.name === presetName);
		if (!preset) return;
		const d = preset.data;
		setBoyAge(d.boy_age);
		setBoySalary(d.boy_salary);
		setBoyEducation(d.boy_education);
		setBoyJobType(d.boy_job_type);
		setJobStabilityBoy(d.job_stability_boy);
		setWorkingAbroad(d.working_abroad);
		setFamilyIncomeBoy(d.family_income_boy);
		setOwnHouseBoy(d.own_house_boy);
		setLandOwnershipBoy(d.land_ownership_boy);
		setBoyHeight(d.boy_height);
		setBoySkinTone(d.boy_skin_tone);
		setPhysicalDisabilityBoy(d.physical_disability_boy);
		setBoyPrevMarriage(d.boy_previous_marriage);
		setBoyArea(d.boy_area);
		if (d.caste) setCaste(d.caste);
		prediction.mutate({
			boy_age: d.boy_age,
			girl_age: girlAge,
			age_difference: Math.max(0, d.boy_age - girlAge),
			boy_salary: d.boy_salary,
			girl_salary: girlSalary,
			boy_education: d.boy_education,
			girl_education: girlEducation,
			boy_job_type: d.boy_job_type,
			girl_job_type: girlJobType,
			job_stability_boy: d.job_stability_boy,
			working_abroad: d.working_abroad,
			family_income_boy: d.family_income_boy,
			family_income_girl: familyIncomeGirl,
			own_house_boy: d.own_house_boy,
			land_ownership_boy: d.land_ownership_boy,
			land_ownership_girl: landOwnershipGirl,
			boy_height: d.boy_height,
			girl_height: girlHeight,
			boy_skin_tone: d.boy_skin_tone,
			girl_skin_tone: girlSkinTone,
			physical_disability_boy: d.physical_disability_boy,
			physical_disability_girl: physicalDisabilityGirl,
			boy_previous_marriage: d.boy_previous_marriage,
			girl_previous_marriage: girlPrevMarriage,
			caste: d.caste,
			religion,
			intercaste_interreligion: intercasteInterreligion,
			rural_urban: ruralUrban,
			boy_area: d.boy_area,
			girl_area: girlArea
		}, { onSuccess: (res) => {
			const val = res.data.predicted_dowry_amount_inr ?? res.data.predicted_acquisition_price_inr;
			setBackendResult({
				predicted: val,
				lower: res.data.prediction_range.lower_bound,
				upper: res.data.prediction_range.upper_bound,
				confidence: res.data.confidence_score
			});
		} });
	};
	const applyBridePreset = (presetName) => {
		const preset = BRIDE_PRESETS.find((p) => p.name === presetName);
		if (!preset) return;
		const d = preset.data;
		setGirlAge(d.girl_age);
		setGirlSalary(d.girl_salary);
		setGirlEducation(d.girl_education);
		setGirlJobType(d.girl_job_type);
		setFamilyIncomeGirl(d.family_income_girl);
		setLandOwnershipGirl(d.land_ownership_girl);
		setGirlHeight(d.girl_height);
		setGirlSkinTone(d.girl_skin_tone);
		setPhysicalDisabilityGirl(d.physical_disability_girl);
		setGirlPrevMarriage(d.girl_previous_marriage);
		setGirlArea(d.girl_area);
		if (d.caste) setCaste(d.caste);
		prediction.mutate({
			boy_age: boyAge,
			girl_age: d.girl_age,
			age_difference: Math.max(0, boyAge - d.girl_age),
			boy_salary: boySalary,
			girl_salary: d.girl_salary,
			boy_education: boyEducation,
			girl_education: d.girl_education,
			boy_job_type: boyJobType,
			girl_job_type: d.girl_job_type,
			job_stability_boy: jobStabilityBoy,
			working_abroad: workingAbroad,
			family_income_boy: familyIncomeBoy,
			family_income_girl: d.family_income_girl,
			own_house_boy: ownHouseBoy,
			land_ownership_boy: landOwnershipBoy,
			land_ownership_girl: d.land_ownership_girl,
			boy_height: boyHeight,
			girl_height: d.girl_height,
			boy_skin_tone: boySkinTone,
			girl_skin_tone: d.girl_skin_tone,
			physical_disability_boy: physicalDisabilityBoy,
			physical_disability_girl: d.physical_disability_girl,
			boy_previous_marriage: boyPrevMarriage,
			girl_previous_marriage: d.girl_previous_marriage,
			caste: d.caste,
			religion,
			intercaste_interreligion: intercasteInterreligion,
			rural_urban: ruralUrban,
			boy_area: boyArea,
			girl_area: d.girl_area
		}, { onSuccess: (res) => {
			const val = res.data.predicted_dowry_amount_inr ?? res.data.predicted_acquisition_price_inr;
			setBackendResult({
				predicted: val,
				lower: res.data.prediction_range.lower_bound,
				upper: res.data.prediction_range.upper_bound,
				confidence: res.data.confidence_score
			});
		} });
	};
	const result = (0, import_react.useMemo)(() => {
		const eduScore = {
			Doctorate: 7,
			"Post Graduate": 6,
			Graduate: 5,
			"Higher Secondary": 4,
			Secondary: 3,
			Middle: 2,
			Primary: 1,
			Illiterate: 0
		}[boyEducation] ?? 5;
		const landBoyVal = landOwnershipBoy === "Large" ? 35e4 : landOwnershipBoy === "Medium" ? 2e5 : landOwnershipBoy === "Small" ? 1e5 : 0;
		const houseBoyVal = ownHouseBoy === "Yes" ? 18e4 : 4e4;
		const nriBonus = workingAbroad === "Yes" ? 35e4 : 0;
		const govtBonus = boyJobType === "Government" ? 22e4 : 0;
		const drivers = {
			"Groom Salary & Career": Math.round(boySalary * 5.2 + govtBonus + (jobStabilityBoy === "Permanent" ? 8e4 : 2e4)),
			"Family Assets & Land": Math.round(familyIncomeBoy * .16 + landBoyVal + houseBoyVal),
			"Education & NRI Premium": Math.round(eduScore * 38e3 + nriBonus),
			"Bride Family & Offsets": Math.round(familyIncomeGirl * .12 + (girlSalary > 0 ? -girlSalary * 1.8 : 0) + 12e4),
			"Demographic & Area Context": Math.round((ruralUrban === "Urban" ? 14e4 : ruralUrban === "Semi-Urban" ? 9e4 : 5e4) + (boyArea === "City" ? 11e4 : 6e4))
		};
		if (backendResult) return {
			predicted: backendResult.predicted,
			lower: backendResult.lower,
			upper: backendResult.upper,
			confidence: backendResult.confidence,
			drivers: Object.entries(drivers).map(([name, value]) => ({
				name,
				value: Math.max(2e4, value)
			})),
			rawDrivers: drivers
		};
		const totalDriver = Object.values(drivers).reduce((a, b) => a + b, 0);
		const estimated = Math.round(Math.max(5e4, totalDriver * (valuationTier === "Very High" ? 1.28 : valuationTier === "High" ? 1.12 : valuationTier === "Low" ? .78 : 1)));
		const mae = 187674;
		return {
			predicted: estimated,
			lower: Math.max(5e4, estimated - mae),
			upper: estimated + mae,
			confidence: .7581,
			drivers: Object.entries(drivers).map(([name, value]) => ({
				name,
				value: Math.max(2e4, value)
			})),
			rawDrivers: drivers
		};
	}, [
		backendResult,
		boySalary,
		boyJobType,
		jobStabilityBoy,
		familyIncomeBoy,
		landOwnershipBoy,
		ownHouseBoy,
		boyEducation,
		workingAbroad,
		familyIncomeGirl,
		girlSalary,
		ruralUrban,
		boyArea,
		valuationTier
	]);
	const isHighAlimony = result.predicted >= 105e4;
	const salaryCurve = (0, import_react.useMemo)(() => {
		const points = [
			{
				salaryLabel: "₹30k",
				factor: .5
			},
			{
				salaryLabel: "₹60k",
				factor: .85
			},
			{
				salaryLabel: "₹90k",
				factor: 1.15
			},
			{
				salaryLabel: "₹1.2L",
				factor: 1.45
			},
			{
				salaryLabel: "₹1.8L",
				factor: 1.85
			},
			{
				salaryLabel: "₹2.5L",
				factor: 2.3
			}
		];
		const baseVal = result.predicted;
		return points.map((p) => {
			const pred = Math.round(baseVal * p.factor);
			return {
				step: p.salaryLabel,
				estimate: pred,
				upperBound: Math.round(pred + 187674)
			};
		});
	}, [result.predicted]);
	const chartColors = [
		"var(--chart-1)",
		"var(--chart-2)",
		"var(--chart-3)",
		"var(--chart-4)",
		"var(--chart-5)"
	];
	return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)(GlassLayout, { children: [
		/* @__PURE__ */ (0, import_jsx_runtime.jsx)(HeroImage, {
			src: indian_bride_groom_default,
			alt: "Indian Bride and Groom"
		}),
		/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
			className: "mb-6 flex flex-col md:flex-row md:items-start md:justify-between gap-4",
			children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { children: [
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
					className: "label-caps text-primary",
					children: "Interactive ML Engine · 400,000 Synthetic Records"
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h1", {
					className: "mt-2 text-3xl font-extrabold sm:text-4xl text-foreground",
					children: "Dahej Predictor & Match Parameters"
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
					className: "mt-2 max-w-2xl text-[0.95rem] text-muted-foreground",
					children: "Predict real-time dowry valuations in Indian Rupees (INR) trained on 30+ empirical marriage dataset dimensions with a Production Ridge + Regularized NN ensemble (R² ~0.758, MAE ±₹187,674, equal weightage)."
				})
			] }), healthData && /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
				className: `shrink-0 rounded-xl px-4 py-2.5 text-xs font-semibold shadow-sm transition-all border self-start md:self-auto ${healthData.model_loaded ? "bg-[oklch(0.55_0.135_162/15%)] text-success border-success/30" : "bg-destructive/10 text-destructive border-destructive/20"}`,
				children: [
					/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
						className: "flex items-center gap-2",
						children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", { className: `h-2.5 w-2.5 rounded-full ${healthData.model_loaded ? "bg-success animate-pulse" : "bg-destructive"}` }), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
							className: "font-bold",
							children: healthData.model_loaded ? "✓ Connected to ML Backend (v1.0.0 · Active)" : "⚠ Backend Model Unavailable"
						})]
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
						className: "mt-1 flex items-center justify-between text-[11px] opacity-85 gap-3 font-mono",
						children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", { children: "30 Dataset Features" }), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", { children: "R² ~0.758 · MAE ±₹188k" })]
					}),
					prediction.isPending && /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
						className: "mt-1 text-[10px] text-primary animate-pulse font-medium",
						children: "Computing empirical pipeline..."
					})
				]
			})]
		}),
		/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
			className: "mb-7",
			children: /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("section", {
				className: "glass p-6 sm:p-8",
				children: [
					/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
						className: "flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4 border-b border-border/70 pb-5",
						children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h2", {
							className: "text-xl font-bold text-foreground flex items-center gap-2",
							children: "Dahej Calculator"
						}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
							className: "text-xs text-muted-foreground mt-1",
							children: "Tuned on 400,000 synthetic records under equal-weightage parity. Change inputs and click the button to predict."
						})] }), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
							className: "flex flex-wrap items-center gap-3",
							children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
								className: "flex gap-1 rounded-xl bg-background/40 p-1 border border-border/80",
								children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("button", {
									type: "button",
									onClick: () => setActiveTab("groom"),
									className: `flex items-center gap-1.5 px-3.5 py-2 text-xs font-bold rounded-lg transition-all ${activeTab === "groom" ? "gradient-primary text-primary-foreground shadow-sm" : "text-muted-foreground hover:text-foreground"}`,
									children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(User, { className: "h-3.5 w-3.5" }), "Groom Section"]
								}), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("button", {
									type: "button",
									onClick: () => setActiveTab("bride"),
									className: `flex items-center gap-1.5 px-3.5 py-2 text-xs font-bold rounded-lg transition-all ${activeTab === "bride" ? "gradient-primary text-primary-foreground shadow-sm" : "text-muted-foreground hover:text-foreground"}`,
									children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Heart, { className: "h-3.5 w-3.5" }), "Bride Section"]
								})]
							}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("button", {
								type: "button",
								id: "btn-predict-dowry",
								onClick: executePrediction,
								disabled: prediction.isPending,
								className: "gradient-primary inline-flex items-center justify-center gap-2 rounded-xl px-5 py-2.5 text-xs font-extrabold text-primary-foreground shadow-[0_4px_16px_oklch(0.42_0.20_25/30%)] transition-all hover:scale-[1.03] active:scale-[0.97] disabled:opacity-70 disabled:hover:scale-100 cursor-pointer",
								children: prediction.isPending ? /* @__PURE__ */ (0, import_jsx_runtime.jsxs)(import_jsx_runtime.Fragment, { children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(RefreshCw, { className: "h-4 w-4 animate-spin" }), "Predicting..."] }) : /* @__PURE__ */ (0, import_jsx_runtime.jsxs)(import_jsx_runtime.Fragment, { children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Send, { className: "h-4 w-4" }), "Predict Dowry Valuation"] })
							})]
						})]
					}),
					activeTab === "groom" && /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
						className: "mt-6 grid gap-8 lg:grid-cols-[1fr_390px] xl:grid-cols-[1fr_420px] animate-fadeIn",
						children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
							className: "space-y-6",
							children: [
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)(QuickPresetsBar, {
									title: "Groom",
									presets: GROOM_PRESETS,
									onSelect: applyGroomPreset
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
									className: "grid gap-5 sm:grid-cols-2",
									children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(SliderRow, {
										label: "Groom Age",
										display: `${boyAge} yrs`,
										value: boyAge,
										min: 20,
										max: 38,
										step: 1,
										onChange: setBoyAge
									}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)(SliderRow, {
										label: "Groom Height",
										display: `${boyHeight} cm (${(boyHeight / 30.48).toFixed(1)} ft)`,
										value: boyHeight,
										min: 155,
										max: 190,
										step: 1,
										onChange: setBoyHeight
									})]
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)(SliderRow, {
									label: "Groom Monthly Salary",
									display: inr(boySalary) + "/mo",
									value: boySalary,
									min: 0,
									max: 25e4,
									step: 2500,
									onChange: setBoySalary
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)(SliderRow, {
									label: "Groom Family Annual Income",
									display: inr(familyIncomeBoy) + "/yr",
									value: familyIncomeBoy,
									min: 15e4,
									max: 4e6,
									step: 25e3,
									onChange: setFamilyIncomeBoy
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
									className: "grid gap-5 sm:grid-cols-2",
									children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(SelectRow, {
										label: "Groom Education",
										value: boyEducation,
										options: EDU_OPTIONS,
										onChange: setBoyEducation
									}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)(SelectRow, {
										label: "Groom Profession (Job Type)",
										value: boyJobType,
										options: BOY_JOB_OPTIONS,
										onChange: setBoyJobType
									})]
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
									className: "grid gap-5 sm:grid-cols-2",
									children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(SelectRow, {
										label: "Job Stability",
										value: jobStabilityBoy,
										options: JOB_STABILITY_OPTIONS,
										onChange: setJobStabilityBoy
									}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)(Segmented, {
										label: "Working Abroad (NRI)",
										options: YES_NO.map((v) => ({
											label: v,
											value: v
										})),
										value: workingAbroad,
										onChange: setWorkingAbroad
									})]
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
									className: "grid gap-5 sm:grid-cols-2",
									children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Segmented, {
										label: "Owns House",
										options: YES_NO.map((v) => ({
											label: v,
											value: v
										})),
										value: ownHouseBoy,
										onChange: setOwnHouseBoy
									}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)(SelectRow, {
										label: "Groom Land Ownership",
										value: landOwnershipBoy,
										options: LAND_OPTIONS,
										onChange: setLandOwnershipBoy
									})]
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
									className: "grid gap-5 sm:grid-cols-3",
									children: [
										/* @__PURE__ */ (0, import_jsx_runtime.jsx)(SelectRow, {
											label: "Skin Tone",
											value: boySkinTone,
											options: SKIN_TONE_OPTIONS,
											onChange: setBoySkinTone
										}),
										/* @__PURE__ */ (0, import_jsx_runtime.jsx)(SelectRow, {
											label: "Living Area",
											value: boyArea,
											options: AREA_OPTIONS,
											onChange: setBoyArea
										}),
										/* @__PURE__ */ (0, import_jsx_runtime.jsx)(SelectRow, {
											label: "Marital Status",
											value: boyPrevMarriage,
											options: MARITAL_OPTIONS,
											onChange: setBoyPrevMarriage
										})
									]
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Segmented, {
									label: "Physical Disability",
									options: YES_NO.map((v) => ({
										label: v,
										value: v
									})),
									value: physicalDisabilityBoy,
									onChange: setPhysicalDisabilityBoy
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)(DemographicsBlock, {
									caste,
									setCaste,
									religion,
									setReligion,
									intercasteInterreligion,
									setIntercasteInterreligion,
									ruralUrban,
									setRuralUrban,
									valuationTier,
									setValuationTier
								})
							]
						}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)(ReactionPortraitCard, {
							defaultView: "bride",
							result,
							isHighAlimony
						})]
					}),
					activeTab === "bride" && /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
						className: "mt-6 grid gap-8 lg:grid-cols-[1fr_390px] xl:grid-cols-[1fr_420px] animate-fadeIn",
						children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
							className: "space-y-6",
							children: [
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)(QuickPresetsBar, {
									title: "Bride",
									presets: BRIDE_PRESETS,
									onSelect: applyBridePreset
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
									className: "grid gap-5 sm:grid-cols-2",
									children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(SliderRow, {
										label: "Bride Age",
										display: `${girlAge} yrs`,
										value: girlAge,
										min: 16,
										max: 32,
										step: 1,
										onChange: setGirlAge
									}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)(SliderRow, {
										label: "Bride Height",
										display: `${girlHeight} cm (${(girlHeight / 30.48).toFixed(1)} ft)`,
										value: girlHeight,
										min: 145,
										max: 175,
										step: 1,
										onChange: setGirlHeight
									})]
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)(SliderRow, {
									label: "Bride Monthly Salary",
									display: inr(girlSalary) + "/mo",
									value: girlSalary,
									min: 0,
									max: 25e4,
									step: 2500,
									onChange: setGirlSalary
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)(SliderRow, {
									label: "Bride Family Annual Income",
									display: inr(familyIncomeGirl) + "/yr",
									value: familyIncomeGirl,
									min: 1e5,
									max: 25e5,
									step: 25e3,
									onChange: setFamilyIncomeGirl
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
									className: "grid gap-5 sm:grid-cols-2",
									children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(SelectRow, {
										label: "Bride Education",
										value: girlEducation,
										options: EDU_OPTIONS,
										onChange: setGirlEducation
									}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)(SelectRow, {
										label: "Bride Profession (Job Type)",
										value: girlJobType,
										options: GIRL_JOB_OPTIONS,
										onChange: setGirlJobType
									})]
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
									className: "grid gap-5 sm:grid-cols-2",
									children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(SelectRow, {
										label: "Bride Land Ownership",
										value: landOwnershipGirl,
										options: LAND_OPTIONS,
										onChange: setLandOwnershipGirl
									}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)(SelectRow, {
										label: "Skin Tone",
										value: girlSkinTone,
										options: SKIN_TONE_OPTIONS,
										onChange: setGirlSkinTone
									})]
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
									className: "grid gap-5 sm:grid-cols-2",
									children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(SelectRow, {
										label: "Bride Living Area",
										value: girlArea,
										options: AREA_OPTIONS,
										onChange: setGirlArea
									}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)(SelectRow, {
										label: "Marital Status",
										value: girlPrevMarriage,
										options: MARITAL_OPTIONS,
										onChange: setGirlPrevMarriage
									})]
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Segmented, {
									label: "Physical Disability",
									options: YES_NO.map((v) => ({
										label: v,
										value: v
									})),
									value: physicalDisabilityGirl,
									onChange: setPhysicalDisabilityGirl
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)(DemographicsBlock, {
									caste,
									setCaste,
									religion,
									setReligion,
									intercasteInterreligion,
									setIntercasteInterreligion,
									ruralUrban,
									setRuralUrban,
									valuationTier,
									setValuationTier
								})
							]
						}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)(ReactionPortraitCard, {
							defaultView: "groom",
							result,
							isHighAlimony
						})]
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
						className: "mt-8 pt-5 border-t border-border/70 flex flex-col sm:flex-row items-center justify-between gap-3",
						children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
							className: "flex items-center gap-2 text-xs text-muted-foreground",
							children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", { className: "h-2 w-2 rounded-full bg-success" }), "Ridge + Regularized NN Ensemble (R² ~0.758)"]
						}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("button", {
							type: "button",
							onClick: executePrediction,
							disabled: prediction.isPending,
							className: "gradient-primary w-full sm:w-auto inline-flex items-center justify-center gap-2 rounded-xl px-6 py-3 text-sm font-extrabold text-primary-foreground shadow-[0_4px_20px_oklch(0.42_0.20_25/30%)] transition-all hover:scale-[1.02] active:scale-[0.98] cursor-pointer disabled:opacity-60",
							children: prediction.isPending ? /* @__PURE__ */ (0, import_jsx_runtime.jsxs)(import_jsx_runtime.Fragment, { children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(RefreshCw, { className: "h-4 w-4 animate-spin" }), "Calculating with Ridge + NN..."] }) : /* @__PURE__ */ (0, import_jsx_runtime.jsxs)(import_jsx_runtime.Fragment, { children: [
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Send, { className: "h-4 w-4" }),
								"Predict Dowry Valuation (",
								inr(result.predicted),
								")"
							] })
						})]
					})
				]
			})
		}),
		/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
			className: "mb-7 space-y-5",
			children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
				className: "grid gap-5 lg:grid-cols-3",
				children: [
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)(MetricCard, {
						label: "Projected Dowry Valuation",
						value: inr(result.predicted),
						hint: `${lakhOrCrore(result.predicted)} · ${backendResult ? "Ridge + NN Ensemble" : "Equal-weightage ML (R² ~0.758)"}`,
						accent: true,
						loading: prediction.isPending
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)(MetricCard, {
						label: "Lower Bound Estimate",
						value: inr(result.lower),
						hint: "Equal-weightage MAE bound (±₹187,674)",
						loading: prediction.isPending
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)(MetricCard, {
						label: "Upper Bound Estimate",
						value: inr(result.upper),
						hint: "Optimistic tier benchmark (MAE bound)",
						loading: prediction.isPending
					})
				]
			}), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
				className: "rounded-2xl glass glass-lift p-5 sm:p-6 border border-border/80",
				children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
					className: "flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3 border-b border-border/60 pb-3.5",
					children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
						className: "flex items-center gap-2.5",
						children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
							className: "flex h-8 w-8 items-center justify-center rounded-xl bg-primary/10 text-primary",
							children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(Scale, { className: "h-4 w-4" })
						}), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h3", {
							className: "text-sm font-bold text-foreground",
							children: "Valuation Breakdown & Key Metrics"
						}), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("p", {
							className: "text-[11px] text-muted-foreground",
							children: ["Computed parameter breakdown for projected valuation ", inr(result.predicted)]
						})] })]
					}), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("span", {
						className: "rounded-full bg-primary/10 px-3 py-1 text-xs font-bold text-primary self-start sm:self-auto",
						children: ["Benchmark Tier: ", valuationTier]
					})]
				}), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
					className: "mt-4 grid grid-cols-2 gap-3 sm:grid-cols-4 lg:grid-cols-6",
					children: [
						/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
							className: "glass-subtle rounded-xl p-3 border border-border/60",
							children: [
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
									className: "text-[10px] font-bold text-muted-foreground uppercase block",
									children: "Groom Salary Base"
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("p", {
									className: "mt-1 text-sm font-black text-foreground",
									children: [inr(boySalary), "/mo"]
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("span", {
									className: "text-[10px] text-primary font-semibold",
									children: [
										"~",
										(result.predicted / (boySalary || 1)).toFixed(1),
										"x monthly salary"
									]
								})
							]
						}),
						/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
							className: "glass-subtle rounded-xl p-3 border border-border/60",
							children: [
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
									className: "text-[10px] font-bold text-muted-foreground uppercase block",
									children: "Groom Family Assets"
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("p", {
									className: "mt-1 text-sm font-black text-foreground",
									children: [inr(familyIncomeBoy), "/yr"]
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("span", {
									className: "text-[10px] text-muted-foreground",
									children: [
										"Land: ",
										landOwnershipBoy,
										" · House: ",
										ownHouseBoy
									]
								})
							]
						}),
						/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
							className: "glass-subtle rounded-xl p-3 border border-border/60",
							children: [
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
									className: "text-[10px] font-bold text-muted-foreground uppercase block",
									children: "Career Stability"
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
									className: "mt-1 text-sm font-black text-foreground",
									children: boyJobType
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("span", {
									className: "text-[10px] text-success font-semibold",
									children: [
										jobStabilityBoy,
										" · NRI: ",
										workingAbroad
									]
								})
							]
						}),
						/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
							className: "glass-subtle rounded-xl p-3 border border-border/60",
							children: [
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
									className: "text-[10px] font-bold text-muted-foreground uppercase block",
									children: "Bride Financial Cushion"
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
									className: "mt-1 text-sm font-black text-foreground",
									children: girlSalary > 0 ? inr(girlSalary) + "/mo" : "Independent Household"
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("span", {
									className: "text-[10px] text-muted-foreground",
									children: [
										"Fam: ",
										inr(familyIncomeGirl),
										"/yr"
									]
								})
							]
						}),
						/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
							className: "glass-subtle rounded-xl p-3 border border-border/60",
							children: [
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
									className: "text-[10px] font-bold text-muted-foreground uppercase block",
									children: "Alimony Security Cover"
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
									className: `mt-1 text-sm font-black ${isHighAlimony ? "text-success" : "text-amber-500"}`,
									children: isHighAlimony ? "Robust Shield (100%+)" : "Moderate / Low Shield"
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
									className: "text-[10px] text-muted-foreground",
									children: isHighAlimony ? "Groom protected" : "Defensive deficit"
								})
							]
						}),
						/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
							className: "glass-subtle rounded-xl p-3 border border-border/60",
							children: [
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
									className: "text-[10px] font-bold text-muted-foreground uppercase block",
									children: "Confidence Range"
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
									className: "mt-1 text-sm font-black text-primary",
									children: "±₹187,674 MAE"
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
									className: "text-[10px] text-muted-foreground",
									children: "R² ~0.758 · 37 Dimensions"
								})
							]
						})
					]
				})]
			})]
		}),
		/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
			className: "mb-7 grid gap-5 lg:grid-cols-2",
			children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("section", {
				className: "glass glass-lift p-6 sm:p-7",
				children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
					className: "flex items-center justify-between",
					children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h2", {
						className: "text-base font-bold text-foreground",
						children: "Valuation Driver Weight Distribution"
					}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
						className: "mt-0.5 text-xs text-muted-foreground",
						children: "Relative contribution of parity-weighted parameters to the predicted dowry."
					})] }), /* @__PURE__ */ (0, import_jsx_runtime.jsx)(Layers, { className: "h-5 w-5 text-primary opacity-70" })]
				}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
					className: "mt-3 h-[270px]",
					children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(ResponsiveContainer, {
						width: "100%",
						height: "100%",
						children: /* @__PURE__ */ (0, import_jsx_runtime.jsxs)(PieChart, { children: [
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Pie, {
								data: result.drivers,
								dataKey: "value",
								nameKey: "name",
								innerRadius: "52%",
								outerRadius: "80%",
								paddingAngle: 4,
								stroke: "var(--background)",
								children: result.drivers.map((_, i) => /* @__PURE__ */ (0, import_jsx_runtime.jsx)(Cell, { fill: chartColors[i % chartColors.length] }, i))
							}),
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Tooltip, {
								formatter: (v) => inr(v),
								contentStyle: glassTooltip
							}),
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Legend, { wrapperStyle: { fontSize: 11 } })
						] })
					})
				})]
			}), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("section", {
				className: "glass glass-lift p-6 sm:p-7",
				children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
					className: "flex items-center justify-between",
					children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h2", {
						className: "text-base font-bold text-foreground",
						children: "Groom Salary vs Dowry Scaling Curve"
					}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
						className: "mt-0.5 text-xs text-muted-foreground",
						children: "Projected valuation curve as groom monthly income scales."
					})] }), /* @__PURE__ */ (0, import_jsx_runtime.jsx)(TrendingUp, { className: "h-5 w-5 text-primary opacity-70" })]
				}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
					className: "mt-3 h-[270px]",
					children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(ResponsiveContainer, {
						width: "100%",
						height: "100%",
						children: /* @__PURE__ */ (0, import_jsx_runtime.jsxs)(AreaChart, {
							data: salaryCurve,
							children: [
								/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("defs", { children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("linearGradient", {
									id: "dowryFill",
									x1: "0",
									y1: "0",
									x2: "0",
									y2: "1",
									children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("stop", {
										offset: "0%",
										stopColor: "var(--chart-1)",
										stopOpacity: .5
									}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("stop", {
										offset: "100%",
										stopColor: "var(--chart-1)",
										stopOpacity: .05
									})]
								}), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("linearGradient", {
									id: "boundFill",
									x1: "0",
									y1: "0",
									x2: "0",
									y2: "1",
									children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("stop", {
										offset: "0%",
										stopColor: "var(--chart-3)",
										stopOpacity: .35
									}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("stop", {
										offset: "100%",
										stopColor: "var(--chart-3)",
										stopOpacity: .05
									})]
								})] }),
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)(XAxis, {
									dataKey: "step",
									stroke: "var(--muted-foreground)",
									fontSize: 12
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)(YAxis, {
									stroke: "var(--muted-foreground)",
									fontSize: 11,
									tickFormatter: (v) => `${(v / 1e5).toFixed(1)}L`
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Tooltip, {
									formatter: (v) => inr(v),
									contentStyle: glassTooltip
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Area, {
									type: "monotone",
									name: "Upper Bound",
									dataKey: "upperBound",
									stroke: "var(--chart-3)",
									fill: "url(#boundFill)",
									strokeWidth: 1.5,
									strokeDasharray: "4 4"
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Area, {
									type: "monotone",
									name: "Predicted Dowry",
									dataKey: "estimate",
									stroke: "var(--chart-1)",
									fill: "url(#dowryFill)",
									strokeWidth: 2.5
								})
							]
						})
					})
				})]
			})]
		})
	] });
}
function MetricCard({ label, value, hint, accent, loading }) {
	return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
		className: "glass glass-lift p-6",
		children: [
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
				className: "label-caps",
				children: label
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
				className: `mt-3 text-3xl font-extrabold tracking-tight ${accent ? "text-primary" : ""} ${loading ? "animate-pulse" : ""}`,
				children: value
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("p", {
				className: "mt-2 flex items-center gap-2 text-xs sm:text-sm text-muted-foreground",
				children: [accent && /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
					className: "rounded-full bg-[oklch(0.55_0.135_162/15%)] px-2.5 py-0.5 text-[0.7rem] font-bold tracking-wide text-success uppercase",
					children: "75.81% R² · Parity-Stable"
				}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", { children: hint })]
			})
		]
	});
}
function SliderRow({ label, display, value, min, max, step, onChange }) {
	return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
		className: "mb-2 flex items-baseline justify-between gap-3",
		children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
			className: "label-caps text-foreground",
			children: label
		}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
			className: "text-sm font-bold text-primary",
			children: display
		})]
	}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("input", {
		type: "range",
		"aria-label": label,
		min,
		max,
		step,
		value,
		onChange: (e) => onChange(Number(e.target.value)),
		className: "h-1.5 w-full cursor-pointer appearance-none rounded-full bg-[oklch(0.878_0.019_251)] accent-[var(--primary)]"
	})] });
}
function SelectRow({ label, value, options, onChange }) {
	return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("label", {
		className: "label-caps text-foreground block mb-1.5",
		children: label
	}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("select", {
		value,
		onChange: (e) => onChange(e.target.value),
		className: "w-full rounded-xl border border-border glass-subtle px-3 py-2.5 text-xs font-semibold text-foreground focus:outline-none focus:ring-2 focus:ring-primary/40",
		children: options.map((opt) => /* @__PURE__ */ (0, import_jsx_runtime.jsx)("option", {
			value: opt,
			className: "bg-background text-foreground",
			children: opt
		}, opt))
	})] });
}
function Segmented({ label, options, value, onChange }) {
	return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
		className: "label-caps text-foreground",
		children: label
	}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
		className: "glass-subtle mt-1.5 flex flex-wrap gap-1 p-1 border border-border/60 rounded-xl",
		children: options.map((o) => /* @__PURE__ */ (0, import_jsx_runtime.jsx)("button", {
			type: "button",
			onClick: () => onChange(o.value),
			className: `flex-1 min-w-[60px] rounded-[9px] px-2.5 py-1.5 text-xs font-bold transition-all ${value === o.value ? "gradient-primary text-primary-foreground shadow-sm" : "text-muted-foreground hover:bg-primary/10 hover:text-primary"}`,
			children: o.label
		}, o.value))
	})] });
}
function QuickPresetsBar({ title, presets, onSelect }) {
	return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
		className: "p-4 rounded-2xl glass-subtle border border-border/80 shadow-xs mb-2",
		children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
			className: "flex items-center justify-between gap-2 mb-3",
			children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("span", {
				className: "text-xs font-bold text-foreground flex items-center gap-1.5",
				children: [
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Sparkles, { className: "h-3.5 w-3.5 text-primary" }),
					"Quick Profile Presets (",
					title,
					"):"
				]
			}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
				className: "text-[11px] text-muted-foreground font-medium hidden sm:inline",
				children: "1-click load empirical archetype"
			})]
		}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
			className: "grid grid-cols-2 sm:grid-cols-4 gap-2.5",
			children: presets.map((p) => /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("button", {
				type: "button",
				onClick: () => onSelect(p.name),
				className: "glass-lift hover:bg-primary/15 hover:border-primary/50 rounded-xl p-3 text-left transition-all border border-border flex flex-col items-start gap-1.5 cursor-pointer group",
				children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
					className: "text-xl group-hover:scale-110 transition-transform",
					children: p.icon
				}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
					className: "text-xs font-bold text-foreground group-hover:text-primary leading-tight",
					children: p.name
				})]
			}, p.name))
		})]
	});
}
function DemographicsBlock({ caste, setCaste, religion, setReligion, intercasteInterreligion, setIntercasteInterreligion, ruralUrban, setRuralUrban, valuationTier, setValuationTier }) {
	return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
		className: "rounded-2xl border border-border/80 glass-subtle p-5 space-y-5",
		children: [
			/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
				className: "flex items-center justify-between pb-3 border-b border-border/60",
				children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
					className: "flex items-center gap-2",
					children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Building, { className: "h-4 w-4 text-primary" }), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("h3", {
						className: "text-sm font-bold text-foreground",
						children: "Demographics & Cultural Setting"
					})]
				}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
					className: "text-[11px] text-muted-foreground font-medium",
					children: "Key empirical dataset predictors"
				})]
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
				className: "grid gap-5 sm:grid-cols-2",
				children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(SelectRow, {
					label: "Social Caste",
					value: caste,
					options: CASTE_OPTIONS,
					onChange: setCaste
				}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)(SelectRow, {
					label: "Religion",
					value: religion,
					options: RELIGION_OPTIONS,
					onChange: setReligion
				})]
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)(SelectRow, {
				label: "Intercaste / Interreligion Status",
				value: intercasteInterreligion,
				options: COMPATIBILITY_OPTIONS,
				onChange: setIntercasteInterreligion
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
				className: "grid gap-5 sm:grid-cols-2",
				children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(SelectRow, {
					label: "Demographic Setting",
					value: ruralUrban,
					options: RURAL_URBAN_OPTIONS,
					onChange: setRuralUrban
				}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)(SelectRow, {
					label: "Target Benchmark Category",
					value: valuationTier,
					options: TIER_OPTIONS,
					onChange: setValuationTier
				})]
			})
		]
	});
}
function ReactionPortraitCard({ defaultView, result, isHighAlimony }) {
	const [currentView, setCurrentView] = (0, import_react.useState)(defaultView);
	(0, import_react.useEffect)(() => {
		setCurrentView(defaultView);
	}, [defaultView]);
	const isBride = currentView === "bride";
	const imageSrc = isBride ? isHighAlimony ? girl_sad_default : girl_happy_default : isHighAlimony ? boy_happy_default : boy_sad_default;
	const title = isBride ? "Bride Emotional Reaction" : "Groom Emotional Reaction";
	const statusBadge = isBride ? isHighAlimony ? "Bride: Distressed & Sad (High Dowry)" : "Bride: Delighted & Happy (Affordable)" : isHighAlimony ? "Groom: Happy & Secured 😄" : "Groom: Sad & Worried 😢";
	const narrative = isBride ? isHighAlimony ? `High dowry demand of ${inr(result.predicted)}! The bride and her family feel severe financial strain under these demanding expectations.` : `Fair and reasonable dowry of ${inr(result.predicted)}! The bride is relieved, joyful, and fully enthusiastic about this match.` : isHighAlimony ? `High security valuation of ${inr(result.predicted)}! The groom feels financially protected, respected, and confident in his future safety cushion.` : `Low safety margin of ${inr(result.predicted)}! The groom feels anxious about prospective legal alimony exposure and asset balance.`;
	return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
		className: "rounded-3xl glass p-5 sm:p-6 flex flex-col border border-border/80 shadow-lg self-start sticky top-20 transition-all duration-300 w-full",
		children: [
			/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
				className: "flex items-center justify-between pb-3.5 mb-3.5 border-b border-border/60",
				children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("span", {
					className: "text-xs font-bold text-foreground flex items-center gap-1.5",
					children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Sparkles, { className: "h-3.5 w-3.5 text-primary" }), "Reaction Portrait"]
				}), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
					className: "flex items-center gap-1 bg-background/50 p-1 rounded-xl border border-border/70",
					children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("button", {
						type: "button",
						onClick: () => setCurrentView("bride"),
						className: `px-2.5 py-1 text-[11px] font-bold rounded-lg transition-all cursor-pointer ${isBride ? "gradient-primary text-primary-foreground shadow-xs" : "text-muted-foreground hover:text-foreground"}`,
						children: "👰 Bride"
					}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("button", {
						type: "button",
						onClick: () => setCurrentView("groom"),
						className: `px-2.5 py-1 text-[11px] font-bold rounded-lg transition-all cursor-pointer ${!isBride ? "gradient-primary text-primary-foreground shadow-xs" : "text-muted-foreground hover:text-foreground"}`,
						children: "🤵 Groom"
					})]
				})]
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
				className: "relative w-full h-[340px] sm:h-[370px] rounded-2xl overflow-hidden shadow-md border-2 border-border/60 group",
				children: [
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)("img", {
						src: imageSrc,
						alt: title,
						className: "w-full h-full object-cover object-top transition-all duration-500 group-hover:scale-105"
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)("button", {
						type: "button",
						onClick: () => setCurrentView(isBride ? "groom" : "bride"),
						className: "absolute left-2.5 top-1/2 -translate-y-1/2 h-8 w-8 rounded-full bg-background/80 hover:bg-background text-foreground backdrop-blur-md flex items-center justify-center shadow-md border border-border/60 transition-transform active:scale-90 cursor-pointer",
						title: "Slide to other portrait",
						"aria-label": "Slide portrait",
						children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(ChevronLeft, { className: "h-4 w-4" })
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)("button", {
						type: "button",
						onClick: () => setCurrentView(isBride ? "groom" : "bride"),
						className: "absolute right-2.5 top-1/2 -translate-y-1/2 h-8 w-8 rounded-full bg-background/80 hover:bg-background text-foreground backdrop-blur-md flex items-center justify-center shadow-md border border-border/60 transition-transform active:scale-90 cursor-pointer",
						title: "Slide to other portrait",
						"aria-label": "Slide portrait",
						children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(ChevronRight, { className: "h-4 w-4" })
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
						className: `absolute bottom-3 left-3 right-3 rounded-xl px-3.5 py-2.5 text-xs font-black backdrop-blur-md flex items-center justify-center gap-1.5 shadow-md border transition-all ${isBride && isHighAlimony || !isBride && !isHighAlimony ? "bg-destructive/90 text-destructive-foreground border-destructive/50" : "bg-success/90 text-success-foreground border-success/50"}`,
						children: [isBride && isHighAlimony || !isBride && !isHighAlimony ? /* @__PURE__ */ (0, import_jsx_runtime.jsx)(Frown, { className: "h-4 w-4 shrink-0" }) : /* @__PURE__ */ (0, import_jsx_runtime.jsx)(Smile, { className: "h-4 w-4 shrink-0" }), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
							className: "truncate",
							children: statusBadge
						})]
					})
				]
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
				className: "mt-4",
				children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
					className: "flex items-center justify-between",
					children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h4", {
						className: "text-sm font-bold text-foreground flex items-center gap-1.5",
						children: title
					}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
						className: "text-[11px] font-semibold text-muted-foreground",
						children: "Slide to toggle ↔"
					})]
				}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
					className: "mt-1.5 text-xs text-muted-foreground leading-relaxed",
					children: narrative
				})]
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
				className: "mt-4 p-3 rounded-xl bg-background/40 border border-border/70 space-y-2",
				children: [
					/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
						className: "flex items-center justify-between text-[11px] font-bold",
						children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("span", {
							className: "text-muted-foreground flex items-center gap-1",
							children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Scale, { className: "h-3 w-3 text-primary" }), "Empirical Threshold:"]
						}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
							className: isHighAlimony ? "text-destructive font-black" : "text-success font-black",
							children: isHighAlimony ? "Above Median (₹10.5L+)" : "Below Median (Affordable)"
						})]
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
						className: "w-full bg-border/50 h-2 rounded-full overflow-hidden",
						children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
							className: `h-full rounded-full transition-all duration-500 ${isHighAlimony ? "bg-destructive" : "bg-success"}`,
							style: { width: `${Math.min(100, Math.max(10, result.predicted / 25e5 * 100))}%` }
						})
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
						className: "flex justify-between text-[10px] text-muted-foreground font-mono",
						children: [
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", { children: "₹1L (Low)" }),
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", { children: "₹10.5L Median" }),
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", { children: "₹25L+ (Peak)" })
						]
					})
				]
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
				className: "mt-4 w-full pt-3.5 border-t border-border/60 flex items-center justify-between",
				children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
					className: "text-[11px] text-muted-foreground block font-medium",
					children: "Current Valuation"
				}), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("span", {
					className: "text-[11px] text-muted-foreground/80 font-mono",
					children: [
						inr(result.lower),
						" – ",
						inr(result.upper)
					]
				})] }), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
					className: "text-lg font-black text-primary font-mono tracking-tight",
					children: inr(result.predicted)
				})]
			})
		]
	});
}
//#endregion
export { PredictorPage as component };
