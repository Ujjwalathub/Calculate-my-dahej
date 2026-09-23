"""
API Endpoint Tests

Tests for all API endpoints using pytest.
"""

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestHealthEndpoints:
    """Test health check and info endpoints."""
    
    def test_ping(self):
        """Test simple ping endpoint."""
        response = client.get("/ping")
        assert response.status_code == 200
        assert response.json() == {"status": "pong"}
    
    def test_health_check(self):
        """Test health check endpoint."""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert "status" in data
        assert "model_loaded" in data
        assert "version" in data
    
    def test_root(self):
        """Test root endpoint."""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert "version" in data
        assert "endpoints" in data


class TestModelEndpoints:
    """Test model-related endpoints."""
    
    def test_model_info(self):
        """Test model information endpoint."""
        response = client.get("/model/info")
        assert response.status_code == 200
        data = response.json()
        assert "model_type" in data
        assert "r2_score" in data
        assert "mae" in data
        assert data["model_type"] == "Ridge + NN Ensemble (Equal Weightage)"
        assert data["features"] == 37
        assert data["training_samples"] == 320000


class TestPredictionEndpoints:
    """Test prediction endpoints."""
    
    def get_sample_startup_data(self):
        """Get sample startup data for testing."""
        return {
            "monthly_recurring_revenue": 150000,
            "patents_held": 12,
            "infrastructure_value": 5000000,
            "fleet_value": 2000000,
            "liquid_cash_reserves": 800000,
            "parent_company_revenue": 120000,
            "business_model": "B2B_Enterprise",
            "brand_reputation": "Industry_Leader",
            "tech_sector": "AI_DeepTech",
            "pending_lawsuits": "no",
            "years_in_operation": 5.8,
            "is_first_acquisition": "yes"
        }
    
    def test_single_prediction_success(self):
        """Test successful single prediction."""
        data = self.get_sample_startup_data()
        response = client.post("/predict", json=data)
        
        assert response.status_code == 200
        result = response.json()
        assert result["success"] is True
        assert "data" in result
        assert "predicted_acquisition_price_inr" in result["data"]
        assert "confidence_score" in result["data"]
        assert "prediction_range" in result["data"]
    
    def test_single_prediction_invalid_revenue(self):
        """Test prediction with invalid revenue."""
        data = self.get_sample_startup_data()
        data["monthly_recurring_revenue"] = 1000  # Too low
        
        response = client.post("/predict", json=data)
        assert response.status_code == 422
    
    def test_single_prediction_missing_field(self):
        """Phase 4 strictness: missing required fields are rejected (422)."""
        data = self.get_sample_startup_data()
        del data["patents_held"]
        
        response = client.post("/predict", json=data)
        assert response.status_code == 422
    
    def test_batch_prediction_success(self):
        """Test successful batch prediction."""
        startups = [self.get_sample_startup_data() for _ in range(3)]
        data = {"startups": startups}
        
        response = client.post("/predict/batch", json=data)
        
        assert response.status_code == 200
        result = response.json()
        assert result["success"] is True
        assert "data" in result
        assert result["data"]["total_count"] == 3
        assert len(result["data"]["predictions"]) == 3
    
    def test_batch_prediction_empty_list(self):
        """Test batch prediction with empty list."""
        data = {"startups": []}
        response = client.post("/predict/batch", json=data)
        assert response.status_code == 422
    
    def test_batch_prediction_too_many(self):
        """Test batch prediction with too many startups."""
        startups = [self.get_sample_startup_data() for _ in range(101)]
        data = {"startups": startups}
        
        response = client.post("/predict/batch", json=data)
        assert response.status_code == 400


class TestValidation:
    """Test input validation."""
    
    def test_equal_weightage_metadata(self):
        """Equal-weightage production metadata contract."""
        r = client.get("/model/info").json()
        assert r["features"] == 37
        assert r["training_samples"] == 320000
        assert abs(r["r2_score"] - 0.7581) < 0.01

    def test_invalid_business_model(self):
        """Test with invalid business model."""
        data = {
            "monthly_recurring_revenue": 150000,
            "patents_held": 12,
            "infrastructure_value": 5000000,
            "fleet_value": 2000000,
            "liquid_cash_reserves": 800000,
            "parent_company_revenue": 120000,
            "business_model": "InvalidModel",  # Invalid
            "brand_reputation": "Industry_Leader",
            "tech_sector": "AI_DeepTech",
            "pending_lawsuits": "no",
            "years_in_operation": 5.8,
            "is_first_acquisition": "yes"
        }
        
        response = client.post("/predict", json=data)
        assert response.status_code == 422
    
    def test_invalid_years_range(self):
        """Test with years out of valid range."""
        data = {
            "monthly_recurring_revenue": 150000,
            "patents_held": 12,
            "infrastructure_value": 5000000,
            "fleet_value": 2000000,
            "liquid_cash_reserves": 800000,
            "parent_company_revenue": 120000,
            "business_model": "B2B_Enterprise",
            "brand_reputation": "Industry_Leader",
            "tech_sector": "AI_DeepTech",
            "pending_lawsuits": "no",
            "years_in_operation": 150.0,  # Out of range (>100 per Phase 4)
            "is_first_acquisition": "yes"
        }
        
        response = client.post("/predict", json=data)
        assert response.status_code == 422


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
