"""
Request Schemas

Pydantic models for validating incoming API requests.
Phase 4 - Data Mapping & Payload Validation:
- Strict ConfigDict(extra='forbid') on all payloads
- Discriminated unions via payload_type Literal
- Enumerations synchronized with frontend
- All fields required (no silent defaults)
"""

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    BeforeValidator,
    field_validator,
    model_validator,
)
from typing import Annotated, List, Literal, Optional, Union
from enum import Enum


class BusinessModel(str, Enum):
    """Business model categories (synchronized with frontend)."""
    B2B_ENTERPRISE = "B2B_Enterprise"
    B2C_CONSUMER = "B2C_Consumer"
    HYBRID = "Hybrid"


class BrandReputation(str, Enum):
    """Brand reputation levels (synchronized with frontend)."""
    INDUSTRY_LEADER = "Industry_Leader"
    ESTABLISHED = "Established"
    EMERGING = "Emerging"
    CONTROVERSIAL = "Controversial"


class TechSector(str, Enum):
    """Technology sector categories (synchronized with frontend)."""
    AI_DEEPTECH = "AI_DeepTech"
    SAAS = "SaaS"
    E_COMMERCE = "E_commerce"
    FINTECH = "Fintech"
    HEALTHCARE = "Healthcare"
    OTHER = "Other"


class YesNo(str, Enum):
    """Yes/No responses."""
    YES = "yes"
    NO = "no"


class DowryData(BaseModel):
    """Schema for the 25 raw equal-weightage dowry features (Phase 4 strict)."""

    model_config = ConfigDict(extra="forbid")

    payload_type: Literal["dowry"] = Field(default="dowry")
    boy_height: float = Field(..., ge=2.0, le=250.0)
    boy_income: float = Field(..., ge=0, le=100000000)
    boy_job: str = Field(...)
    boy_first_marriage: str = Field(...)
    boy_father_income: float = Field(..., ge=0, le=100000000)
    boy_area: str = Field(...)
    boy_skin_colour: str = Field(...)
    boy_caste: str = Field(...)
    boy_religion: str = Field(...)
    boy_age: int = Field(..., ge=18, le=60)
    boy_physical_disability: str = Field(...)
    boy_job_stability: str = Field(...)
    girl_height: float = Field(..., ge=2.0, le=250.0)
    girl_income: float = Field(..., ge=0, le=100000000)
    girl_job: str = Field(...)
    girl_first_marriage: str = Field(...)
    girl_father_income: float = Field(..., ge=0, le=100000000)
    girl_area: str = Field(...)
    girl_skin_colour: str = Field(...)
    girl_caste: str = Field(...)
    girl_religion: str = Field(...)
    girl_age: int = Field(..., ge=16, le=60)
    girl_physical_disability: str = Field(...)
    age_difference: Optional[float] = Field(default=None)
    intercaste_interreligion: str = Field(...)
    # Legacy frontend aliases (accepted, mapped to canonicals above).
    girl_salary: Optional[float] = Field(default=None, exclude=True)
    boy_job_type: Optional[str] = Field(default=None, exclude=True)
    girl_job_type: Optional[str] = Field(default=None, exclude=True)
    job_stability_boy: Optional[str] = Field(default=None, exclude=True)
    family_income_boy: Optional[float] = Field(default=None, exclude=True)
    family_income_girl: Optional[float] = Field(default=None, exclude=True)
    boy_skin_tone: Optional[str] = Field(default=None, exclude=True)
    girl_skin_tone: Optional[str] = Field(default=None, exclude=True)
    physical_disability_boy: Optional[str] = Field(default=None, exclude=True)
    physical_disability_girl: Optional[str] = Field(default=None, exclude=True)
    boy_previous_marriage: Optional[str] = Field(default=None, exclude=True)
    girl_previous_marriage: Optional[str] = Field(default=None, exclude=True)
    caste: Optional[str] = Field(default=None, exclude=True)
    religion: Optional[str] = Field(default=None, exclude=True)
    # Purely informational legacy fields (ignored for the model).
    boy_education: Optional[str] = Field(default=None, exclude=True)
    girl_education: Optional[str] = Field(default=None, exclude=True)
    working_abroad: Optional[str] = Field(default=None, exclude=True)
    own_house_boy: Optional[str] = Field(default=None, exclude=True)
    land_ownership_boy: Optional[str] = Field(default=None, exclude=True)
    land_ownership_girl: Optional[str] = Field(default=None, exclude=True)
    rural_urban: Optional[str] = Field(default=None, exclude=True)
    age_diff: Optional[float] = Field(default=None, exclude=True)

    @model_validator(mode="before")
    @classmethod
    def _map_legacy(cls, data):
        if not isinstance(data, dict):
            return data
        d = dict(data)
        pairs = {
            "boy_salary": "boy_income",
            "boy_job_type": "boy_job",
            "boy_previous_marriage": "boy_first_marriage",
            "family_income_boy": "boy_father_income",
            "boy_skin_tone": "boy_skin_colour",
            "physical_disability_boy": "boy_physical_disability",
            "job_stability_boy": "boy_job_stability",
            "girl_salary": "girl_income",
            "girl_job_type": "girl_job",
            "girl_previous_marriage": "girl_first_marriage",
            "family_income_girl": "girl_father_income",
            "girl_skin_tone": "girl_skin_colour",
            "physical_disability_girl": "girl_physical_disability",
            "age_diff": "age_difference",
        }
        for leg, can in pairs.items():
            if can not in d and leg in d and d[leg] is not None:
                d[can] = d[leg]
        # Phase 6 / frontend integration: drop the legacy source keys after
        # mapping. DowryData uses extra='forbid', so leaving e.g. 'boy_salary'
        # alongside the mapped 'boy_income' raises extra_forbidden and the
        # frontend (which sends legacy field names) can never get a prediction.
        for leg in pairs:
            d.pop(leg, None)
        # Frontend-only informational keys that are NOT model fields must also
        # be stripped (they are not declared on DowryData -> extra='forbid').
        for extra_key in ("dowry_category", "rural_urban"):
            d.pop(extra_key, None)
        if "caste" in d and d["caste"] is not None:
            d.setdefault("boy_caste", d["caste"])
            d.setdefault("girl_caste", d["caste"])
        if "religion" in d and d["religion"] is not None:
            d.setdefault("boy_religion", d["religion"])
            d.setdefault("girl_religion", d["religion"])
        return d

    @model_validator(mode="after")
    def _derive_age(self):
        if self.age_difference is None:
            self.age_difference = float(self.boy_age - self.girl_age)
        return self


class StartupData(BaseModel):
    """
    Startup acquisition schema (Phase 4 - strict validation).
    All fields required except fleet_value; unknown fields rejected.
    Backward-compatible: payload_type defaults to 'startup' and enum/case
    variants are coerced so existing frontend/test payloads keep working.
    """
    model_config = ConfigDict(extra="forbid")

    payload_type: Literal["startup"] = Field(
        default="startup", description="Discriminator for startup payloads"
    )
    monthly_recurring_revenue: float = Field(..., ge=15000, le=500000)
    patents_held: int = Field(..., ge=1, le=78)
    infrastructure_value: float = Field(..., ge=10000, le=100000000)
    fleet_value: Optional[float] = Field(default=None, ge=0, le=20000000)
    liquid_cash_reserves: float = Field(..., ge=20000, le=100000000)
    parent_company_revenue: float = Field(..., ge=25000, le=300000)
    # HIGH 4 fix: realistic operating history (was impossible 5.6-6.2 window).
    years_in_operation: float = Field(..., ge=0.0, le=100.0)
    business_model: BusinessModel = Field(...)
    brand_reputation: BrandReputation = Field(...)
    tech_sector: TechSector = Field(...)
    pending_lawsuits: YesNo = Field(...)
    is_first_acquisition: YesNo = Field(...)

    @field_validator(
        "business_model", "brand_reputation", "tech_sector",
        "pending_lawsuits", "is_first_acquisition", mode="before",
    )
    @classmethod
    def _coerce_enums(cls, v):
        # Accept lowercase / legacy variants sent by current clients.
        if isinstance(v, str):
            s = v.strip()
            lowered = s.lower()
            aliases = {
                # business models
                "b2b_enterprise": "B2B_Enterprise",
                "b2b": "B2B_Enterprise",
                "b2c_consumer": "B2C_Consumer",
                "b2c": "B2C_Consumer",
                "hybrid": "Hybrid",
                # brand reputation
                "industry_leader": "Industry_Leader",
                "established": "Established",
                "emerging": "Emerging",
                "controversial": "Controversial",
                # tech sectors
                "ai_deeptech": "AI_DeepTech",
                "ai": "AI_DeepTech",
                "saas": "SaaS",
                "e_commerce": "E_commerce",
                "ecommerce": "E_commerce",
                "fintech": "Fintech",
                "healthcare": "Healthcare",
                "other": "Other",
                # yes/no
                "yes": "yes",
                "y": "yes",
                "true": "yes",
                "1": "yes",
                "no": "no",
                "n": "no",
                "false": "no",
                "0": "no",
            }
            if s in (
                "B2B_Enterprise", "B2C_Consumer", "Hybrid",
                "Industry_Leader", "Established", "Emerging", "Controversial",
                "AI_DeepTech", "SaaS", "E_commerce", "Fintech",
                "Healthcare", "Other", "yes", "no",
            ):
                return s
            if lowered in aliases:
                return aliases[lowered]
        return v


# Critical 2: discriminated union for secure O(1) payload routing.
# Strict variant (PredictItem / PredictionRequest / batch items) requires an
# explicit payload_type discriminator. InferredPredictItem additionally
# accepts legacy payloads without the discriminator for /predict compat.
def _infer_startup(v):
    if isinstance(v, dict) and "payload_type" not in v:
        return {**v, "payload_type": "startup"}
    return v


def _infer_dowry(v):
    if isinstance(v, dict) and "payload_type" not in v:
        return {**v, "payload_type": "dowry"}
    return v


InferredStartup = Annotated[StartupData, BeforeValidator(_infer_startup)]
InferredDowry = Annotated[DowryData, BeforeValidator(_infer_dowry)]

# Union-first form: try startup shape, fall back to dowry shape.
# Field-level discrimination inside each member still rejects {} with 422.
InferredPredictItem = Union[InferredStartup, InferredDowry]

# Strict discriminated union used by PredictionRequest / batch items.
# Requires the explicit payload_type discriminator (spec section 2.3).
PredictItem = Annotated[
    Union[StartupData, DowryData], Field(discriminator="payload_type")
]


class PredictionRequest(BaseModel):
    """Single prediction request wrapper (discriminated payload)."""

    model_config = ConfigDict(extra="forbid")
    data: PredictItem = Field(..., description="Single profile payload")


class BatchPredictionRequest(BaseModel):
    """
    Schema for batch prediction requests (Phase 4 strict + backward compatible).
    Accepts the discriminated `items` list; keeps the legacy `startups` alias.
    Items use the inferred (non-discriminated) union so legacy clients that
    omit `payload_type` — e.g. the frontend sending {"items": [...]} — are
    routed by shape instead of rejected with union_tag_not_found.
    """

    model_config = ConfigDict(extra="forbid")
    items: Optional[List[InferredPredictItem]] = Field(
        default=None,
        description="List of profiles for batch prediction (max 100)",
    )
    startups: Optional[List[StartupData]] = Field(
        default=None,
        description="Legacy alias for startups batch",
    )

    @model_validator(mode="after")
    def _non_empty(self):
        if not (self.items or self.startups):
            raise ValueError("Batch must contain at least 1 item")
        return self
