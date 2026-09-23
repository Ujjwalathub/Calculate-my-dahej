"""Prediction Service - Equal-Weightage (Phase 4 + Phase 5 resilience)."""
import sys
import joblib
import numpy as np
import pandas as pd
from pathlib import Path
from typing import Dict, List, Tuple, Any, Union
import logging
from app.core.config import settings
from app.schemas.request import DowryData, StartupData
logger = logging.getLogger(__name__)

class PredictionService:
    NUM = ['boy_height','boy_income','boy_father_income','boy_age',
           'girl_height','girl_income','girl_father_income','girl_age',
           'age_difference']
    CAT = ['boy_job','boy_first_marriage','boy_area','boy_skin_colour',
           'boy_caste','boy_religion','boy_physical_disability',
           'boy_job_stability','girl_job','girl_first_marriage','girl_area',
           'girl_skin_colour','girl_caste','girl_religion',
           'girl_physical_disability','intercaste_interreligion']
    BASE = NUM + CAT
    DEF = {'boy_height':5.9,'boy_income':50000,'boy_father_income':45000,
        'boy_age':27,'girl_height':5.4,'girl_income':25000,
        'girl_father_income':40000,'girl_age':23,'age_difference':4,
        'boy_job':'private','boy_first_marriage':'yes','boy_area':'urban',
        'boy_skin_colour':'wheatish','boy_caste':'OBC','boy_religion':'hindu',
        'boy_physical_disability':'no','boy_job_stability':'stable',
        'girl_job':'private','girl_first_marriage':'yes','girl_area':'rural',
        'girl_skin_colour':'wheatish','girl_caste':'OBC',
        'girl_religion':'hindu','girl_physical_disability':'no',
        'intercaste_interreligion':'same_caste_religion'}
    def __init__(self):
        self.model_package=None;self.ensemble_model=None;self.neural_net=None
        self.ridge_model=None;self.constrained_rf=None;self.best_model=None
        self.best_model_name='EqualWeight_Ensemble';self.preprocessor_obj=None
        self.model_info={};self._load_model()
    def _load_model(self):
        """Load models with strict namespace resolution (Phase 5).

        joblib/pickle requires the class definition (UnifiedPreprocessor,
        saved from ``scripts.model``) to be importable under that exact
        module path, so the ``scripts/`` directory is injected into
        ``sys.path`` immediately prior to loading.
        """
        try:
            # 1. Calculate absolute path to the scripts directory
            # __file__ is backend/app/services/prediction_service.py
            backend_dir = Path(__file__).resolve().parent.parent.parent
            scripts_dir = str(backend_dir / "scripts")

            # 2. Inject into sys.path to satisfy joblib namespace resolution
            if scripts_dir not in sys.path:
                sys.path.insert(0, scripts_dir)

            # 3. Safely load (absolute paths via settings)
            model_path=Path(settings.MODEL_PATH);pp=Path(settings.PREPROCESSOR_PATH)
            if not model_path.exists():raise FileNotFoundError(model_path)
            if not pp.exists():raise FileNotFoundError(pp)
            self.model_package=joblib.load(model_path)
            self.preprocessor_obj=joblib.load(pp)
            self.ridge_model=self.model_package.get('xgb_model')
            self.constrained_rf=self.model_package.get('lgb_model')
            self.ensemble_model=self.model_package.get('ensemble_model')
            self.neural_net=self.model_package.get('neural_net')
            self.model_info={'task':self.model_package.get('task','regression'),
                'test_scores':self.model_package.get('test_scores',{}),
                'best_xgb_params':self.model_package.get('best_xgb_params',{}),
                'best_lgb_params':self.model_package.get('best_lgb_params',{})}
            self._select_best_model()
            logger.info("model loaded: "+self.best_model_name)
        except Exception as e:
            logger.error("Failed to load model: "+str(e));raise
    def _select_best_model(self):
        cand={'Ridge_Equal':self.ridge_model,'XGBoost':self.ridge_model,
            'Constrained_RF':self.constrained_rf,'LightGBM':self.constrained_rf,
            'EqualWeight_Ensemble':self.ensemble_model,'Ensemble':self.ensemble_model,
            'Constrained_NN':self.neural_net,'Neural Network':self.neural_net}
        scores=self.model_info.get('test_scores',{})or{}
        ranked=sorted(((k,v) for k,v in scores.items() if isinstance(v,dict) and 'R2' in v),
            key=lambda kv:kv[1]['R2'],reverse=True)
        for n,_ in ranked:
            if cand.get(n) is not None:
                self.best_model_name=n;self.best_model=cand[n];return
        for n in ('EqualWeight_Ensemble','Ridge_Equal','Constrained_NN','Ensemble'):
            if cand.get(n) is not None:
                self.best_model_name=n;self.best_model=cand[n];return
        self.best_model=self.ensemble_model or self.ridge_model or self.neural_net

    def _coerce(self,data):
        if hasattr(data,'model_dump'):return dict(data.model_dump())
        if hasattr(data,'dict'):
            try:return dict(data.dict())
            except Exception:pass
        if isinstance(data,dict):return dict(data)
        try:return dict(data)
        except Exception:return {}

    @staticmethod
    def _n(v,default=''):
        return default if v is None else str(v).strip().lower()
    @staticmethod
    def _ft(v,default):
        try:f=float(v)
        except(TypeError,ValueError):return default
        return round(f/30.48,2) if f>20 else round(f,2)
    def _job(self,v):return 'government' if 'gov' in self._n(v) else 'private'
    def _stab(self,v):
        s=self._n(v)
        if 'very' in s or 'permanent' in s:return 'very_stable'
        if 'unstable' in s or 'contract' in s or 'unemploy' in s:return 'unstable'
        return 'stable'
    def _area(self,v):
        s=self._n(v)
        return 'rural' if('rural' in s or 'village' in s) else 'urban'
    def _skin(self,v):
        s=self._n(v)
        if 'fair' in s:return 'fair'
        if 'dark' in s:return 'dark'
        return 'wheatish'
    def _mar(self,v):
        s=self._n(v)
        if s in('yes','never married','never_married','first','single'):return 'yes'
        if s in('no','divorced','widowed','second'):return 'no'
        return 'yes' if 'never' in s else 'no'
    def _yn(self,v,d='no'):
        s=self._n(v)
        if s in('yes','y','true','1'):return 'yes'
        if s in('no','n','false','0'):return 'no'
        return d
    def _caste(self,v):
        s=self._n(v)
        if s=='general':return 'general'
        if s in('sc','st'):return 'SC'
        return 'OBC'
    def _rel(self,v):
        s=self._n(v)
        if s in('hindu','muslim','christian','sikh','others'):return s
        if 'christ' in s:return 'christian'
        if 'hind' in s:return 'hindu'
        return 'others'
    def _inter(self,v):
        s=self._n(v)
        if 'same' in s:return 'same_caste_religion'
        if 'intercaste' in s or('caste' in s and 'inter' in s):return 'intercaste'
        if 'interreligion' in s or 'religion' in s or 'inter' in s:return 'interreligion'
        return 'same_caste_religion'

    def _part_a(self,data):
        d=self._coerce(data)
        low={str(k).strip().lower():v for k,v in d.items()}
        low.pop('dowry_category',None)
        row=dict(self.DEF)
        def num(*keys,default=0.0):
            for k in keys:
                if k in low and low[k] not in(None,''):
                    try:return float(low[k])
                    except(TypeError,ValueError):continue
            return float(default)
        def cat(*keys,default=''):
            for k in keys:
                if k in low and low[k] not in(None,''):
                    return str(low[k])
            return default
        if 'boy_income' in low or 'boy_job' in low:
            row['boy_height']=self._ft(num('boy_height',default=row['boy_height']),row['boy_height'])
            row['boy_income']=num('boy_income',default=row['boy_income'])
            row['boy_father_income']=num('boy_father_income','family_income_boy','father_income_inr',default=row['boy_father_income'])
            row['boy_age']=num('boy_age',default=row['boy_age'])
            row['girl_height']=self._ft(num('girl_height',default=row['girl_height']),row['girl_height'])
            row['girl_income']=num('girl_income',default=row['girl_income'])
            row['girl_father_income']=num('girl_father_income','family_income_girl',default=row['girl_father_income'])
            row['girl_age']=num('girl_age',default=row['girl_age'])
            row['age_difference']=num('age_difference','age_diff',default=(row['boy_age']-row['girl_age']))
            row['boy_job']=self._job(cat('boy_job',default='private'))
            row['boy_first_marriage']=self._mar(cat('boy_first_marriage',default='yes'))
            row['boy_area']=self._area(cat('boy_area',default='urban'))
            row['boy_skin_colour']=self._skin(cat('boy_skin_colour','boy_skin_tone',default='wheatish'))
            row['boy_caste']=self._caste(cat('boy_caste','caste',default='OBC'))
            row['boy_religion']=self._rel(cat('boy_religion','religion',default='hindu'))
            return row,low,True
        return row,low,False

    def _part_b(self,row,low,handled):
        def num(*keys,default=0.0):
            for k in keys:
                if k in low and low[k] not in(None,''):
                    try:return float(low[k])
                    except(TypeError,ValueError):continue
            return float(default)
        def cat(*keys,default=''):
            for k in keys:
                if k in low and low[k] not in(None,''):
                    return str(low[k])
            return default
        if handled:
            row['boy_physical_disability']=self._yn(cat('boy_physical_disability','physical_disability_boy',default='no'))
            row['boy_job_stability']=self._stab(cat('boy_job_stability','job_stability_boy',default='stable'))
            row['girl_job']=self._job(cat('girl_job',default='private'))
            row['girl_first_marriage']=self._mar(cat('girl_first_marriage',default='yes'))
            row['girl_area']=self._area(cat('girl_area',default='rural'))
            row['girl_skin_colour']=self._skin(cat('girl_skin_colour','girl_skin_tone',default='wheatish'))
            row['girl_caste']=self._caste(cat('girl_caste','caste',default='OBC'))
            row['girl_religion']=self._rel(cat('girl_religion','religion',default='hindu'))
            row['girl_physical_disability']=self._yn(cat('girl_physical_disability','physical_disability_girl',default='no'))
            row['intercaste_interreligion']=self._inter(cat('intercaste_interreligion',default='same_caste_religion'))
            return pd.DataFrame([{k:row[k] for k in self.BASE}])
        if 'monthly_recurring_revenue' in low or 'business_model' in low:
            row['boy_income']=num('monthly_recurring_revenue','income_per_month_inr',default=50000)
            row['girl_income']=num('girl_income','girl_salary',default=25000)
            row['boy_father_income']=num('parent_company_revenue','father_income_inr',default=45000)
            row['girl_father_income']=num('liquid_cash_reserves',default=40000)/20.0
            row['boy_height']=5.4+min(max(num('patents_held',default=12)/78.0,0.0),1.0)
            row['girl_height']=5.7;row['boy_age']=27;row['girl_age']=23;row['age_difference']=4
            row['boy_job']=self._job(cat('business_model',default='private'))
            row['boy_first_marriage']=self._yn(cat('is_first_acquisition',default='yes'),'yes')
            return pd.DataFrame([{k:row[k] for k in self.BASE}])
        row['boy_age']=num('boy_age',default=27);row['girl_age']=num('girl_age',default=23)
        row['boy_income']=num('boy_income','boy_salary','income_per_month_inr',default=row['boy_income'])
        row['girl_income']=num('girl_income','girl_salary',default=row['girl_income'])
        row['boy_father_income']=num('boy_father_income','family_income_boy','father_income_inr',default=row['boy_father_income'])
        row['girl_father_income']=num('girl_father_income','family_income_girl',default=row['girl_father_income'])
        row['boy_height']=self._ft(cat('boy_height',default=row['boy_height']),row['boy_height'])
        row['girl_height']=self._ft(cat('girl_height',default=row['girl_height']),row['girl_height'])
        if 'age_difference' in low or 'age_diff' in low:
            row['age_difference']=num('age_difference','age_diff',default=row['boy_age']-row['girl_age'])
        else:row['age_difference']=row['boy_age']-row['girl_age']
        row['boy_job']=self._job(cat('boy_job','boy_job_type',default='private'))
        row['boy_first_marriage']=self._mar(cat('boy_first_marriage','boy_previous_marriage','is_first_marriage',default='yes'))
        row['boy_area']=self._area(cat('boy_area',default='urban'))
        row['boy_skin_colour']=self._skin(cat('boy_skin_colour','boy_skin_tone',default='wheatish'))
        sc=cat('caste',default='')
        row['boy_caste']=self._caste(cat('boy_caste',default=sc or 'OBC'))
        row['girl_caste']=self._caste(cat('girl_caste',default=sc or 'OBC'))
        sr=cat('religion',default='')
        row['boy_religion']=self._rel(cat('boy_religion',default=sr or 'hindu'))
        row['girl_religion']=self._rel(cat('girl_religion',default=sr or 'hindu'))
        row['boy_physical_disability']=self._yn(cat('boy_physical_disability','physical_disability_boy',default='no'))
        row['girl_physical_disability']=self._yn(cat('girl_physical_disability','physical_disability_girl',default='no'))
        row['boy_job_stability']=self._stab(cat('boy_job_stability','job_stability_boy',default='stable'))
        row['girl_job']=self._job(cat('girl_job','girl_job_type',default='private'))
        row['girl_first_marriage']=self._mar(cat('girl_first_marriage','girl_previous_marriage',default='yes'))
        row['girl_area']=self._area(cat('girl_area',default='rural'))
        row['girl_skin_colour']=self._skin(cat('girl_skin_colour','girl_skin_tone',default='wheatish'))
        row['intercaste_interreligion']=self._inter(cat('intercaste_interreligion',default='same_caste_religion'))
        return pd.DataFrame([{k:row[k] for k in self.BASE}])
    def _prepare_dowry_dataframe(self,data):
        row,low,handled=self._part_a(data)
        return self._part_b(row,low,handled)
    def _prepare_startup_dataframe(self, data: Dict[str, Any]) -> pd.DataFrame:
        """Dynamically map Startup metrics to the 25 Equal-Weightage features.

        Phase 4 (Critical 1): every startup input influences the output row.
        Financial features map directly; patents drive heights; operating
        years drive ages; business model / brand / sector / lawsuits drive
        categorical features deterministically.
        """
        item = {str(k).strip().lower(): v for k, v in (data or {}).items()}

        def yn(v):
            s = str(v).strip().lower()
            return "yes" if s in ("yes", "y", "true", "1") else "no"

        row: Dict[str, Any] = {}

        # 1. Financials (monetary mappings)
        row["boy_income"] = float(item.get("monthly_recurring_revenue", 0)) * 12.0
        row["boy_father_income"] = float(item.get("parent_company_revenue", 0))
        row["girl_father_income"] = float(item.get("liquid_cash_reserves", 0))
        row["girl_income"] = float(item.get("infrastructure_value", 0)) + float(
            item.get("fleet_value") or 0
        )

        # 2. Continuous metrics (patents -> heights, years -> ages)
        try:
            patents = float(item.get("patents_held", 0))
        except (TypeError, ValueError):
            patents = 0.0
        try:
            years = float(item.get("years_in_operation", 0))
        except (TypeError, ValueError):
            years = 0.0
        row["boy_height"] = float(np.clip(5.4 + (patents * 0.05), 5.4, 6.4))
        row["girl_height"] = float(np.clip(5.0 + (patents * 0.03), 5.0, 5.92))
        row["boy_age"] = int(np.clip(24 + years, 18, 60))
        row["girl_age"] = int(np.clip(20 + (years * 0.8), 16, 60))
        row["age_difference"] = float(row["boy_age"] - row["girl_age"])

        # 3. Categoricals - jobs & stability from business model
        bm = str(item.get("business_model", "")).strip()
        is_stable = bm in ("B2B_Enterprise", "Hybrid")
        job_type = "government" if is_stable else "private"
        row["boy_job"] = job_type
        row["girl_job"] = job_type
        row["boy_job_stability"] = "very_stable" if is_stable else "unstable"

        # 4. Binary flags
        row["boy_first_marriage"] = yn(item.get("is_first_acquisition", "yes"))
        row["girl_first_marriage"] = "yes"
        try:
            lawsuits = float(item.get("pending_lawsuits", 0) or 0)
        except (TypeError, ValueError):
            lawsuits = 1.0 if yn(item.get("pending_lawsuits", "no")) == "yes" else 0.0
        row["boy_physical_disability"] = "yes" if lawsuits > 0 else "no"
        row["girl_physical_disability"] = "no"

        # 5. Categoricals - brand reputation to social metrics
        brand = str(item.get("brand_reputation", "")).strip()
        if brand == "Industry_Leader":
            caste, skin = "general", "fair"
        elif brand in ("Established", "Emerging"):
            caste, skin = "OBC", "wheatish"
        else:  # Controversial / unknown
            caste, skin = "SC", "dark"
        row["boy_caste"] = caste
        row["girl_caste"] = caste
        row["boy_skin_colour"] = skin
        row["girl_skin_colour"] = skin

        # 6. Categoricals - sector to religion (deterministic mapping)
        sector_map = {
            "AI_DeepTech": "hindu",
            "SaaS": "christian",
            "Fintech": "sikh",
            "E_commerce": "muslim",
            "Healthcare": "hindu",
            "Other": "others",
        }
        religion = sector_map.get(str(item.get("tech_sector", "")).strip(), "others")
        row["boy_religion"] = religion
        row["girl_religion"] = religion

        # 7. Environmental
        row["boy_area"] = "urban"
        row["girl_area"] = "urban"
        row["intercaste_interreligion"] = (
            "same_caste_religion" if row["boy_religion"] == row["girl_religion"]
            else "interreligion"
        )

        return pd.DataFrame([{k: row[k] for k in self.BASE}])

    def _calculate_prediction_range(self,prediction):
        scores=self.model_info.get('test_scores',{}).get(self.best_model_name,{})
        try:mae=float(scores.get('MAE',187556))
        except(TypeError,ValueError):mae=187556.0
        # Phase 6: clamp lower bound to 0 to prevent negative financial outputs
        lower_bound=max(0.0,float(prediction)-mae)
        upper_bound=float(prediction)+mae
        return int(lower_bound),int(upper_bound)
    def predict_single(self,data):
        try:
            d=self._coerce(data)
            lowk={str(k).strip().lower() for k in d.keys()}
            # Route startup payloads through the dynamic mapping engine so
            # every startup feature influences the valuation (Phase 4).
            if lowk & {'monthly_recurring_revenue','business_model','tech_sector',
                       'brand_reputation','patents_held','infrastructure_value',
                       'fleet_value','liquid_cash_reserves','parent_company_revenue',
                       'years_in_operation','pending_lawsuits','is_first_acquisition'}:
                df=self._prepare_startup_dataframe(d)
            else:
                df=self._prepare_dowry_dataframe(d)
            pre=getattr(self.preprocessor_obj,'preprocessor',None)
            X=pre.transform(df) if pre is not None else self.preprocessor_obj.transform(df)
            pred=self.best_model.predict(X)[0]
            pred=np.clip(pred,settings.MIN_ACQUISITION_PRICE,settings.MAX_ACQUISITION_PRICE)
            lo,hi=self._calculate_prediction_range(pred)
            scores=self.model_info.get('test_scores',{}).get(self.best_model_name,{})
            conf=float(scores.get('R2',0.7582))
            return {'predicted_acquisition_price_inr':int(pred),
                'predicted_dowry_amount_inr':int(pred),
                'confidence_score':round(conf,4),
                'prediction_range':{'lower_bound':lo,'upper_bound':hi}}
        except Exception as e:
            logger.error("Prediction failed: "+str(e));raise
    def predict_batch(self,items):
        preds=[self.predict_single(i) for i in items]
        tot=sum(p['predicted_acquisition_price_inr'] for p in preds)
        avg=tot/len(preds) if preds else 0
        return {'predictions':preds,'total_count':len(preds),'average_acquisition_price':int(avg)}
    def get_model_info(self):
        scores=self.model_info.get('test_scores',{})
        ms=scores.get('EqualWeight_Ensemble') or scores.get('Ridge_Equal') or scores.get(self.best_model_name) or {}
        return {'model_type':'Ridge + NN Ensemble (Equal Weightage)',
            'components':['Ridge Regression','Regularized NN (MLP)','Voting Ensemble'],
            'r2_score':round(float(ms.get('R2',0.7582)),4),
            'mae':int(ms.get('MAE',187556)),'rmse':int(ms.get('RMSE',242918)),
            'training_samples':320000,'features':37}
    def is_loaded(self):return self.best_model is not None and self.preprocessor_obj is not None
    # Alias for spec naming (Phase 5 doc uses _load_models plural).
    def _load_models(self):return self._load_model()
    def predict(self,data):return self.predict_single(data)


# Phase 5: lazy singleton — no eager instantiation at import time.
# The FastAPI lifespan (app/main.py) owns the canonical instance in
# app.state.prediction_service. This module-level accessor is a safe
# fallback for contexts where lifespan has not run (e.g. TestClient
# used without a context manager) and for backward-compatible imports.
_service_cache={"instance":None}
def get_prediction_service():
    """Return the shared PredictionService, loading lazily. Never raises.

    Returns None when model files are missing/corrupt so callers can
    translate that into HTTP 503 instead of crashing at import time.
    """
    inst=_service_cache.get("instance")
    try:
        if inst is not None and inst.is_loaded():return inst
    except Exception:pass
    try:
        inst=PredictionService()
        _service_cache["instance"]=inst
        return inst
    except Exception as e:
        logger.error("Lazy model load failed: "+str(e))
        return None

def __getattr__(name):
    # Backward compat: `from app.services.prediction_service import prediction_service`
    # must not crash at import time when models are absent.
    if name in ("prediction_service","service"):
        return get_prediction_service()
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

