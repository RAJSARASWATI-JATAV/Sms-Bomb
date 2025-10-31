#!/usr/bin/env python3
"""
Test script to verify config loads correctly after bug fixes
"""

def test_config():
    """Test that config loads and parses CORS correctly"""
    print("🔧 Testing SMS-POWERBOMB Configuration...")
    print("=" * 60)
    
    try:
        from config import settings
        print("✅ Config module imported successfully")
        
        # Test CORS origins
        print(f"\n📋 CORS Configuration:")
        print(f"  Origins: {settings.cors_origins}")
        print(f"  Type: {type(settings.cors_origins)}")
        
        if isinstance(settings.cors_origins, list):
            print(f"  ✅ CORS origins is a list (correct)")
            print(f"  ✅ Number of origins: {len(settings.cors_origins)}")
            for i, origin in enumerate(settings.cors_origins, 1):
                print(f"    {i}. {origin}")
        else:
            print(f"  ❌ CORS origins is not a list: {type(settings.cors_origins)}")
            return False
        
        # Test CORS methods
        print(f"\n📋 CORS Methods: {settings.cors_methods}")
        if isinstance(settings.cors_methods, list):
            print(f"  ✅ CORS methods is a list")
        
        # Test CORS headers
        print(f"\n📋 CORS Headers: {settings.cors_headers}")
        if isinstance(settings.cors_headers, list):
            print(f"  ✅ CORS headers is a list")
        
        # Test database URL
        print(f"\n📋 Database Configuration:")
        print(f"  URL: {settings.database_url}")
        if "sqlite" in settings.database_url.lower():
            print(f"  ✅ Using SQLite (correct for development)")
        
        # Test other settings
        print(f"\n📋 Application Settings:")
        print(f"  Name: {settings.app_name}")
        print(f"  Version: {settings.app_version}")
        print(f"  Debug: {settings.debug}")
        print(f"  Environment: {settings.environment}")
        
        print(f"\n📋 Server Settings:")
        print(f"  Host: {settings.host}")
        print(f"  Port: {settings.port}")
        
        print("\n" + "=" * 60)
        print("✅ All configuration tests passed!")
        print("=" * 60)
        return True
        
    except Exception as e:
        print(f"\n❌ Configuration test failed!")
        print(f"Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    import sys
    success = test_config()
    sys.exit(0 if success else 1)