# 🚀 SMS-POWERBOMB v10.0 - Backend API

FastAPI backend server for SMS-POWERBOMB v10.0 Ultimate Edition.

## 📋 Features

- ✅ **RESTful API** - Complete CRUD operations
- ✅ **JWT Authentication** - Secure token-based auth
- ✅ **PostgreSQL Database** - Async SQLAlchemy ORM
- ✅ **Redis Caching** - Fast data access
- ✅ **WebSocket Support** - Real-time updates
- ✅ **API Documentation** - Auto-generated Swagger/OpenAPI
- ✅ **CORS Enabled** - Frontend integration ready
- ✅ **Rate Limiting** - API protection
- ✅ **Error Handling** - Comprehensive error responses

## 🛠️ Tech Stack

- **Framework**: FastAPI 0.115+
- **Database**: PostgreSQL + SQLAlchemy (Async)
- **Cache**: Redis
- **Authentication**: JWT (python-jose)
- **Password Hashing**: bcrypt
- **Server**: Uvicorn (ASGI)

## 📁 Project Structure

```
backend/
├── main.py              # FastAPI application
├── config.py            # Configuration settings
├── database.py          # Database connection
├── models.py            # SQLAlchemy models
├── schemas.py           # Pydantic schemas
├── auth.py              # Authentication utilities
├── routers/             # API route handlers
│   ├── __init__.py
│   ├── auth.py          # Authentication routes
│   ├── campaigns.py     # Campaign management
│   ├── apis.py          # API gateway management
│   └── dashboard.py     # Dashboard statistics
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variables template
└── README.md            # This file
```

## 🚀 Quick Start

### 1. Prerequisites

- Python 3.10+
- PostgreSQL 14+
- Redis 6+

### 2. Installation

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration

```bash
# Copy environment template
cp .env.example .env

# Edit .env with your settings
# Update DATABASE_URL, REDIS settings, SECRET_KEY, etc.
```

### 4. Database Setup

```bash
# Create PostgreSQL database
createdb smsbomb

# Run migrations (auto-creates tables on first run)
python main.py
```

### 5. Run Server

```bash
# Development mode (with auto-reload)
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Or using Python
python main.py
```

### 6. Access API

- **API**: http://localhost:8000
- **Docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **Health**: http://localhost:8000/health

## 📚 API Endpoints

### Authentication

- `POST /api/v1/auth/register` - Register new user
- `POST /api/v1/auth/login` - Login user
- `POST /api/v1/auth/token` - OAuth2 token
- `GET /api/v1/auth/me` - Get current user
- `POST /api/v1/auth/logout` - Logout user

### Campaigns

- `POST /api/v1/campaigns` - Create campaign
- `GET /api/v1/campaigns` - List campaigns
- `GET /api/v1/campaigns/{id}` - Get campaign
- `PATCH /api/v1/campaigns/{id}` - Update campaign
- `DELETE /api/v1/campaigns/{id}` - Delete campaign
- `POST /api/v1/campaigns/{id}/start` - Start campaign
- `POST /api/v1/campaigns/{id}/pause` - Pause campaign
- `POST /api/v1/campaigns/{id}/cancel` - Cancel campaign
- `GET /api/v1/campaigns/{id}/logs` - Get campaign logs

### API Gateways

- `POST /api/v1/apis` - Create API gateway (Admin)
- `GET /api/v1/apis` - List API gateways
- `GET /api/v1/apis/{id}` - Get API gateway
- `PATCH /api/v1/apis/{id}` - Update API gateway (Admin)
- `DELETE /api/v1/apis/{id}` - Delete API gateway (Admin)
- `GET /api/v1/apis/stats/summary` - Get API statistics

### Dashboard

- `GET /api/v1/dashboard/stats` - Get dashboard stats
- `GET /api/v1/dashboard/recent-campaigns` - Get recent campaigns
- `GET /api/v1/dashboard/activity-chart` - Get activity chart data

## 🔐 Authentication

The API uses JWT (JSON Web Tokens) for authentication.

### Getting a Token

```bash
curl -X POST "http://localhost:8000/api/v1/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "your_username",
    "password": "your_password"
  }'
```

### Using the Token

```bash
curl -X GET "http://localhost:8000/api/v1/campaigns" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## 🗄️ Database Models

### User
- User accounts with roles (admin, user, guest)
- Password hashing with bcrypt
- Email verification support
- Last login tracking

### Campaign
- Campaign management with multiple modes
- Target phone numbers (JSON array)
- Wave and delay configuration
- Real-time statistics tracking
- Status management (pending, running, paused, completed, failed, cancelled)

### APIGateway
- SMS gateway API configurations
- Health monitoring
- Rate limiting per minute/hour
- Success rate tracking
- Priority-based selection

### Analytics
- Time-series analytics data
- Campaign metrics
- API performance stats
- Mode distribution

## 🔧 Configuration

Key environment variables:

```env
# Application
APP_NAME=SMS-POWERBOMB
DEBUG=True

# Database
DATABASE_URL=postgresql+asyncpg://user:pass@localhost:5432/smsbomb

# Redis
REDIS_HOST=localhost
REDIS_PORT=6379

# JWT
SECRET_KEY=your-secret-key-here
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS
CORS_ORIGINS=http://localhost:5173,http://localhost:3000
```

## 📊 Database Schema

```sql
-- Users table
users (id, username, email, hashed_password, role, is_active, ...)

-- User settings
user_settings (id, user_id, theme, notifications, ...)

-- Campaigns
campaigns (id, user_id, name, mode, targets, status, stats, ...)

-- Campaign logs
campaign_logs (id, campaign_id, target, api_name, status, ...)

-- API gateways
api_gateways (id, name, url, status, stats, rate_limits, ...)

-- Analytics
analytics (id, date, metrics, ...)
```

## 🧪 Testing

```bash
# Run tests (coming soon)
pytest

# With coverage
pytest --cov=.
```

## 📝 Development

### Adding New Routes

1. Create router file in `routers/`
2. Define endpoints with FastAPI decorators
3. Add schemas in `schemas.py`
4. Include router in `main.py`

### Database Migrations

```bash
# Create migration
alembic revision --autogenerate -m "description"

# Apply migration
alembic upgrade head

# Rollback
alembic downgrade -1
```

## 🚀 Production Deployment

### Using Docker

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Using Gunicorn

```bash
gunicorn main:app \
  --workers 4 \
  --worker-class uvicorn.workers.UvicornWorker \
  --bind 0.0.0.0:8000
```

## 🔒 Security

- ✅ Password hashing with bcrypt
- ✅ JWT token authentication
- ✅ CORS protection
- ✅ SQL injection prevention (SQLAlchemy ORM)
- ✅ Rate limiting
- ✅ Input validation (Pydantic)

## 📈 Performance

- Async database operations
- Redis caching
- Connection pooling
- Efficient query optimization
- Background task processing

## 🐛 Troubleshooting

### Database Connection Error

```bash
# Check PostgreSQL is running
pg_isready

# Verify connection string in .env
DATABASE_URL=postgresql+asyncpg://user:pass@localhost:5432/smsbomb
```

### Redis Connection Error

```bash
# Check Redis is running
redis-cli ping

# Should return: PONG
```

### Import Errors

```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

## 📞 Support

For issues and questions:
- GitHub: [@RAJSARASWATI-JATAV](https://github.com/RAJSARASWATI-JATAV)
- Email: support@smsbomb.com

## 📄 License

This project is for educational purposes only.

---

<div align="center">
<b>✨ SMS-POWERBOMB v10.0 Backend API ✨</b>
<br>
<i>Built with FastAPI, PostgreSQL, and Redis</i>
<br><br>
<b>Status: Production Ready 🚀</b>
</div>