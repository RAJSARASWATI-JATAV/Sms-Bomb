# SMS-POWERBOMB v10.0 - API Documentation

Complete API reference for the backend.

## Base URL

```
http://localhost:8000/api/v1
```

## Authentication

Most endpoints require authentication using JWT tokens.

### Get Token

```http
POST /auth/login
Content-Type: application/json

{
  "username": "user",
  "password": "password"
}
```

**Response:**
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "token_type": "bearer",
  "user": {
    "id": 1,
    "username": "user",
    "email": "user@example.com"
  }
}
```

### Use Token

Include in Authorization header:
```
Authorization: Bearer <access_token>
```

---

## Endpoints

### Campaigns

#### Start Campaign

Start a new SMS bombing campaign.

```http
POST /campaigns/start
Authorization: Bearer <token>
Content-Type: application/json

{
  "phone": "9876543210",
  "count": 5,
  "mode": "normal",
  "delay": 2
}
```

**Parameters:**
- `phone` (string, required): Target phone number (10 digits)
- `count` (integer, required): Number of SMS waves (1-100)
- `mode` (string, optional): Bombing mode (normal/stealth/turbo/smart)
- `delay` (integer, optional): Delay between waves in seconds (1-10)

**Response:**
```json
{
  "success": true,
  "campaign_id": "abc123",
  "message": "Campaign started successfully"
}
```

#### Get Campaign Status

```http
GET /campaigns/{campaign_id}
Authorization: Bearer <token>
```

**Response:**
```json
{
  "id": "abc123",
  "phone": "9876543210",
  "status": "running",
  "mode": "normal",
  "success_count": 15,
  "fail_count": 5,
  "success_rate": 75.0,
  "started_at": "2024-01-15T10:30:00Z",
  "duration": "00:02:30"
}
```

#### Stop Campaign

```http
POST /campaigns/{campaign_id}/stop
Authorization: Bearer <token>
```

**Response:**
```json
{
  "success": true,
  "message": "Campaign stopped successfully"
}
```

#### List Campaigns

```http
GET /campaigns?page=1&limit=10
Authorization: Bearer <token>
```

**Response:**
```json
{
  "campaigns": [
    {
      "id": "abc123",
      "phone": "9876543210",
      "status": "completed",
      "success_rate": 75.0,
      "created_at": "2024-01-15T10:30:00Z"
    }
  ],
  "total": 50,
  "page": 1,
  "pages": 5
}
```

---

### APIs

#### Get API Status

```http
GET /apis/status
Authorization: Bearer <token>
```

**Response:**
```json
{
  "apis": [
    {
      "name": "OLA",
      "active": true,
      "success_count": 100,
      "fail_count": 20,
      "success_rate": 83.3,
      "avg_response_time": 2.5
    }
  ],
  "total_apis": 20,
  "active_apis": 18
}
```

#### Test API

```http
POST /apis/test
Authorization: Bearer <token>
Content-Type: application/json

{
  "api_name": "OLA",
  "phone": "9876543210"
}
```

**Response:**
```json
{
  "success": true,
  "api_name": "OLA",
  "response_time": 2.3,
  "message": "API test successful"
}
```

---

### Dashboard

#### Get Statistics

```http
GET /dashboard/stats
Authorization: Bearer <token>
```

**Response:**
```json
{
  "total_campaigns": 100,
  "successful_campaigns": 75,
  "failed_campaigns": 25,
  "total_sms": 5000,
  "overall_success_rate": 68.5,
  "active_apis": 18,
  "avg_response_time": 2.8
}
```

#### Get Analytics

```http
GET /dashboard/analytics?period=7d
Authorization: Bearer <token>
```

**Parameters:**
- `period`: Time period (24h/7d/30d/all)

**Response:**
```json
{
  "period": "7d",
  "campaigns_per_day": [
    {"date": "2024-01-15", "count": 10},
    {"date": "2024-01-16", "count": 15}
  ],
  "success_rate_trend": [
    {"date": "2024-01-15", "rate": 70.5},
    {"date": "2024-01-16", "rate": 72.3}
  ],
  "top_apis": [
    {"name": "OLA", "success_rate": 85.0},
    {"name": "Paytm", "success_rate": 80.0}
  ]
}
```

---

### Monitoring

#### Get System Health

```http
GET /monitoring/health
```

**Response:**
```json
{
  "status": "healthy",
  "uptime": 86400,
  "cpu_usage": 45.2,
  "memory_usage": 62.8,
  "active_campaigns": 3,
  "queue_size": 15
}
```

#### Get Metrics

```http
GET /monitoring/metrics
Authorization: Bearer <token>
```

**Response:**
```json
{
  "requests_per_minute": 120,
  "avg_response_time": 2.5,
  "error_rate": 5.2,
  "active_connections": 45
}
```

---

### WebSocket

#### Connect to WebSocket

```javascript
const ws = new WebSocket('ws://localhost:8000/api/v1/ws');

ws.onopen = () => {
  // Send authentication
  ws.send(JSON.stringify({
    type: 'auth',
    token: '<access_token>'
  }));
};

ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  console.log('Received:', data);
};
```

#### Subscribe to Campaign Updates

```javascript
ws.send(JSON.stringify({
  type: 'subscribe',
  campaign_id: 'abc123'
}));
```

**Updates:**
```json
{
  "type": "campaign_update",
  "campaign_id": "abc123",
  "data": {
    "success_count": 20,
    "fail_count": 5,
    "progress": 50
  }
}
```

---

## Error Responses

All errors follow this format:

```json
{
  "success": false,
  "error": "Error type",
  "detail": "Detailed error message",
  "code": "ERROR_CODE"
}
```

### Common Error Codes

- `400` - Bad Request (invalid parameters)
- `401` - Unauthorized (missing/invalid token)
- `403` - Forbidden (insufficient permissions)
- `404` - Not Found (resource doesn't exist)
- `429` - Too Many Requests (rate limited)
- `500` - Internal Server Error

---

## Rate Limiting

API endpoints are rate limited:

- **Authentication**: 5 requests per minute
- **Campaign Start**: 10 requests per minute
- **Other endpoints**: 60 requests per minute

Rate limit headers:
```
X-RateLimit-Limit: 60
X-RateLimit-Remaining: 45
X-RateLimit-Reset: 1642234567
```

---

## Pagination

List endpoints support pagination:

```http
GET /campaigns?page=2&limit=20
```

**Parameters:**
- `page` (integer): Page number (default: 1)
- `limit` (integer): Items per page (default: 10, max: 100)

**Response includes:**
```json
{
  "items": [...],
  "total": 100,
  "page": 2,
  "pages": 5,
  "has_next": true,
  "has_prev": true
}
```

---

## Interactive API Documentation

Visit `http://localhost:8000/docs` for interactive Swagger UI documentation.

---

**Created by: RAJSARASWATI JATAV**  
**Team: RAJSARASWATI JATAV CYBER CREW**