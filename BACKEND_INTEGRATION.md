# 🔗 Frontend-Backend Integration Guide

## 📋 Overview

This guide explains how to connect the SMS-POWERBOMB frontend with the newly created backend API.

## 🚀 Quick Start

### 1. Start Backend Server

```bash
cd backend
pip install -r requirements.txt
python main.py
```

Backend will run at: **http://localhost:8000**

### 2. Start Frontend Server

```bash
cd frontend
npm run dev
```

Frontend will run at: **http://localhost:5173**

## 🔧 Frontend Configuration

### Create API Client

Create `frontend/src/lib/api.ts`:

```typescript
import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api/v1';

// Create axios instance
export const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add auth token to requests
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Handle auth errors
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('access_token');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

// API methods
export const authAPI = {
  register: (data: any) => api.post('/auth/register', data),
  login: (data: any) => api.post('/auth/login', data),
  getCurrentUser: () => api.get('/auth/me'),
  logout: () => api.post('/auth/logout'),
};

export const campaignAPI = {
  create: (data: any) => api.post('/campaigns', data),
  getAll: (params?: any) => api.get('/campaigns', { params }),
  getById: (id: number) => api.get(`/campaigns/${id}`),
  update: (id: number, data: any) => api.patch(`/campaigns/${id}`, data),
  delete: (id: number) => api.delete(`/campaigns/${id}`),
  start: (id: number) => api.post(`/campaigns/${id}/start`),
  pause: (id: number) => api.post(`/campaigns/${id}/pause`),
  cancel: (id: number) => api.post(`/campaigns/${id}/cancel`),
  getLogs: (id: number, params?: any) => api.get(`/campaigns/${id}/logs`, { params }),
};

export const apiGatewayAPI = {
  getAll: (params?: any) => api.get('/apis', { params }),
  getById: (id: number) => api.get(`/apis/${id}`),
  getStats: () => api.get('/apis/stats/summary'),
};

export const dashboardAPI = {
  getStats: () => api.get('/dashboard/stats'),
  getRecentCampaigns: (limit?: number) => api.get('/dashboard/recent-campaigns', { params: { limit } }),
  getActivityChart: (days?: number) => api.get('/dashboard/activity-chart', { params: { days } }),
};
```

### Update Login Page

Update `frontend/src/pages/Login.tsx`:

```typescript
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { authAPI } from '@/lib/api';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';

export function Login() {
  const navigate = useNavigate();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      const response = await authAPI.login({ username, password });
      localStorage.setItem('access_token', response.data.access_token);
      navigate('/');
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Login failed');
    } finally {
      setLoading(false);
    }
  };

  return (
    // ... your login UI with form submission
  );
}
```

### Update Dashboard Page

Update `frontend/src/pages/Dashboard.tsx`:

```typescript
import { useEffect, useState } from 'react';
import { dashboardAPI } from '@/lib/api';

export function Dashboard() {
  const [stats, setStats] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadStats();
  }, []);

  const loadStats = async () => {
    try {
      const response = await dashboardAPI.getStats();
      setStats(response.data);
    } catch (error) {
      console.error('Failed to load stats:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) return <div>Loading...</div>;

  return (
    // ... render stats from API
  );
}
```

## 📡 API Endpoints Reference

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/auth/register` | Register new user |
| POST | `/api/v1/auth/login` | Login user |
| GET | `/api/v1/auth/me` | Get current user |
| POST | `/api/v1/auth/logout` | Logout user |

### Campaigns

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/campaigns` | Create campaign |
| GET | `/api/v1/campaigns` | List campaigns |
| GET | `/api/v1/campaigns/{id}` | Get campaign |
| PATCH | `/api/v1/campaigns/{id}` | Update campaign |
| DELETE | `/api/v1/campaigns/{id}` | Delete campaign |
| POST | `/api/v1/campaigns/{id}/start` | Start campaign |
| POST | `/api/v1/campaigns/{id}/pause` | Pause campaign |
| POST | `/api/v1/campaigns/{id}/cancel` | Cancel campaign |
| GET | `/api/v1/campaigns/{id}/logs` | Get logs |

### API Gateways

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/apis` | List API gateways |
| GET | `/api/v1/apis/{id}` | Get API gateway |
| GET | `/api/v1/apis/stats/summary` | Get API stats |

### Dashboard

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/dashboard/stats` | Get dashboard stats |
| GET | `/api/v1/dashboard/recent-campaigns` | Get recent campaigns |
| GET | `/api/v1/dashboard/activity-chart` | Get activity chart |

## 🔐 Authentication Flow

1. **User logs in** → Frontend sends credentials to `/api/v1/auth/login`
2. **Backend validates** → Returns JWT access token
3. **Frontend stores token** → Saves in localStorage
4. **Subsequent requests** → Include token in Authorization header
5. **Token expires** → Redirect to login page

## 📊 Data Flow Example

### Creating a Campaign

```typescript
// 1. User fills campaign form in frontend
const campaignData = {
  name: "Test Campaign",
  mode: "normal",
  targets: ["+1234567890", "+0987654321"],
  waves: 3,
  delay_seconds: 5,
  use_proxy: false,
  use_vpn: false,
  randomize_apis: true
};

// 2. Frontend sends to backend
const response = await campaignAPI.create(campaignData);

// 3. Backend creates campaign in database
// 4. Backend returns campaign with ID and status
const campaign = response.data;

// 5. Frontend updates UI with new campaign
console.log(`Campaign ${campaign.id} created with status: ${campaign.status}`);

// 6. User starts campaign
await campaignAPI.start(campaign.id);

// 7. Backend updates status to "running"
// 8. Frontend polls for updates or uses WebSocket
```

## 🔄 Real-time Updates (Future)

For real-time campaign updates, implement WebSocket connection:

```typescript
const ws = new WebSocket('ws://localhost:8000/ws');

ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  // Update UI with real-time data
};
```

## 🧪 Testing the Integration

### 1. Test Backend

```bash
cd backend
python test_api.py
```

### 2. Test Frontend

```bash
cd frontend
npm run dev
```

### 3. Manual Testing

1. Open http://localhost:5173
2. Register a new user
3. Login with credentials
4. Create a test campaign
5. View dashboard statistics
6. Check API status page

## 🐛 Troubleshooting

### CORS Errors

If you see CORS errors, verify backend `.env`:

```env
CORS_ORIGINS=http://localhost:5173,http://localhost:3000
```

### Authentication Errors

- Check token is stored in localStorage
- Verify token format: `Bearer <token>`
- Check token expiration (default 30 minutes)

### Connection Refused

- Ensure backend is running on port 8000
- Check firewall settings
- Verify API_BASE_URL in frontend

## 📝 Environment Variables

### Backend (.env)

```env
DATABASE_URL=sqlite+aiosqlite:///./smsbomb.db
SECRET_KEY=your-secret-key
CORS_ORIGINS=http://localhost:5173
```

### Frontend (.env)

```env
VITE_API_BASE_URL=http://localhost:8000/api/v1
```

## 🚀 Next Steps

1. ✅ Backend API is ready
2. ⏳ Update frontend to use real API
3. ⏳ Implement WebSocket for real-time updates
4. ⏳ Add error handling and loading states
5. ⏳ Implement campaign execution logic
6. ⏳ Add API gateway health monitoring
7. ⏳ Deploy to production

---

<div align="center">
<b>✨ Frontend + Backend Integration Complete ✨</b>
<br>
<i>Ready to connect and test!</i>
</div>