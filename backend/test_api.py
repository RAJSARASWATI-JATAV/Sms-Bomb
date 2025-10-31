"""
Simple test script to verify the API is working
Run this after starting the server
"""
import requests
import json

BASE_URL = "http://localhost:8000"

def test_health():
    """Test health endpoint"""
    print("🔍 Testing health endpoint...")
    response = requests.get(f"{BASE_URL}/health")
    print(f"✅ Status: {response.status_code}")
    print(f"📄 Response: {response.json()}\n")
    return response.status_code == 200

def test_register():
    """Test user registration"""
    print("🔍 Testing user registration...")
    data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpass123",
        "full_name": "Test User"
    }
    response = requests.post(f"{BASE_URL}/api/v1/auth/register", json=data)
    print(f"✅ Status: {response.status_code}")
    if response.status_code in [200, 201]:
        print(f"📄 Response: {response.json()}\n")
        return True
    elif response.status_code == 400:
        print(f"⚠️  User already exists\n")
        return True
    else:
        print(f"❌ Error: {response.text}\n")
        return False

def test_login():
    """Test user login"""
    print("🔍 Testing user login...")
    data = {
        "username": "testuser",
        "password": "testpass123"
    }
    response = requests.post(f"{BASE_URL}/api/v1/auth/login", json=data)
    print(f"✅ Status: {response.status_code}")
    if response.status_code == 200:
        result = response.json()
        print(f"📄 Got access token\n")
        return result.get("access_token")
    else:
        print(f"❌ Error: {response.text}\n")
        return None

def test_dashboard(token):
    """Test dashboard stats"""
    print("🔍 Testing dashboard stats...")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/api/v1/dashboard/stats", headers=headers)
    print(f"✅ Status: {response.status_code}")
    if response.status_code == 200:
        print(f"📄 Response: {json.dumps(response.json(), indent=2)}\n")
        return True
    else:
        print(f"❌ Error: {response.text}\n")
        return False

def main():
    print("=" * 60)
    print("🚀 SMS-POWERBOMB Backend API Test")
    print("=" * 60 + "\n")
    
    # Test health
    if not test_health():
        print("❌ Health check failed. Is the server running?")
        return
    
    # Test registration
    test_register()
    
    # Test login
    token = test_login()
    if not token:
        print("❌ Login failed. Cannot continue tests.")
        return
    
    # Test dashboard
    test_dashboard(token)
    
    print("=" * 60)
    print("✅ All tests completed!")
    print("=" * 60)

if __name__ == "__main__":
    try:
        main()
    except requests.exceptions.ConnectionError:
        print("\n❌ Cannot connect to server. Please start the server first:")
        print("   python main.py")
    except Exception as e:
        print(f"\n❌ Error: {e}")