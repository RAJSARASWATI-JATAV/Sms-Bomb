# 🚀 Backend Quick Start Guide

## Step 1: Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

## Step 2: Run the Server

```bash
python main.py
```

Or with uvicorn:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Step 3: Access the API

- **API Root**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

## Step 4: Test the API

### Register a User

```bash
curl -X POST "http://localhost:8000/api/v1/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "admin",
    "email": "admin@smsbomb.com",
    "password": "admin123",
    "full_name": "Admin User"
  }'
```

### Login

```bash
curl -X POST "http://localhost:8000/api/v1/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "admin",
    "password": "admin123"
  }'
```

### Create a Campaign

```bash
curl -X POST "http://localhost:8000/api/v1/campaigns" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test Campaign",
    "mode": "normal",
    "targets": ["+1234567890"],
    "waves": 1,
    "delay_seconds": 5
  }'
```

## 🎉 That's it!

Your backend is now running and ready to connect with the frontend!

**Next Steps:**
1. Update frontend API base URL to `http://localhost:8000`
2. Test authentication flow
3. Create campaigns from the web dashboard
4. Monitor API status

---

**Note**: The backend uses SQLite by default for easy setup. For production, configure PostgreSQL in `.env` file.