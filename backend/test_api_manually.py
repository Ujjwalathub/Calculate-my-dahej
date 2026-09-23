"""
Manual API Testing Script

Quick script to test all API endpoints without starting the server separately.
"""

import requests
import json
from time import sleep

BASE_URL = "http://localhost:8000"


def print_section(title):
    """Print a formatted section header."""
    print("\n" + "=" * 80)
    print(f" {title}")
    print("=" * 80)


def test_health():
    """Test health check endpoint."""
    print_section("Testing Health Check")
    
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False


def test_model_info():
    """Test model info endpoint."""
    print_section("Testing Model Info")
    
    try:
        response = requests.get(f"{BASE_URL}/model/info")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False


def test_single_prediction():
    """Test single prediction endpoint."""
    print_section("Testing Single Prediction")
    
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
        "years_in_operation": 5.8,
        "is_first_acquisition": "yes"
    }
    
    try:
        print(f"Request Data: {json.dumps(data, indent=2)}")
        response = requests.post(f"{BASE_URL}/predict", json=data)
        print(f"\nStatus Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 200:
            result = response.json()
            price = result['data']['predicted_acquisition_price_inr']
            print(f"\n💰 Predicted Acquisition Price: ₹{price:,}")
            return True
        return False
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False


def test_batch_prediction():
    """Test batch prediction endpoint."""
    print_section("Testing Batch Prediction")
    
    data = {
        "startups": [
            {
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
            },
            {
                "monthly_recurring_revenue": 80000,
                "patents_held": 5,
                "infrastructure_value": 2000000,
                "fleet_value": None,
                "liquid_cash_reserves": 300000,
                "parent_company_revenue": 60000,
                "business_model": "B2C_Consumer",
                "brand_reputation": "Established",
                "tech_sector": "SaaS",
                "pending_lawsuits": "no",
                "years_in_operation": 5.9,
                "is_first_acquisition": "yes"
            }
        ]
    }
    
    try:
        print(f"Sending {len(data['startups'])} startups for prediction...")
        response = requests.post(f"{BASE_URL}/predict/batch", json=data)
        print(f"\nStatus Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 200:
            result = response.json()
            print(f"\n📊 Total Predictions: {result['data']['total_count']}")
            print(f"💰 Average Price: ₹{result['data']['average_acquisition_price']:,}")
            return True
        return False
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False


def test_validation_error():
    """Test validation error handling."""
    print_section("Testing Validation (Invalid Input)")
    
    data = {
        "monthly_recurring_revenue": 1000,  # Too low
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
    
    try:
        response = requests.post(f"{BASE_URL}/predict", json=data)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 422:
            print("\n✓ Validation error caught successfully!")
            return True
        return False
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False


def main():
    """Run all tests."""
    print("\n" + "=" * 80)
    print(" STARTUP ACQUISITION VALUATION API - MANUAL TEST SUITE")
    print("=" * 80)
    print("\nMake sure the API server is running:")
    print("  python run.py")
    print("\nOr:")
    print("  uvicorn app.main:app --reload")
    print("\nWaiting for server to be ready...")
    sleep(2)
    
    results = {
        "Health Check": test_health(),
        "Model Info": test_model_info(),
        "Single Prediction": test_single_prediction(),
        "Batch Prediction": test_batch_prediction(),
        "Validation Error": test_validation_error()
    }
    
    # Summary
    print_section("TEST SUMMARY")
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    for test_name, result in results.items():
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{test_name:30s} {status}")
    
    print(f"\nTotal: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All tests passed! Your API is working perfectly!")
    else:
        print("\n⚠️  Some tests failed. Check the output above for details.")
    
    print("=" * 80 + "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Tests interrupted by user")
    except requests.exceptions.ConnectionError:
        print("\n\n❌ ERROR: Could not connect to API server!")
        print("Make sure the server is running:")
        print("  python run.py")
        print("\nOr:")
        print("  uvicorn app.main:app --reload")
