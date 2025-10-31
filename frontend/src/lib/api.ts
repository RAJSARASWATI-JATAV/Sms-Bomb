import axios, { type AxiosInstance } from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api/v1';

// Create axios instance
export const api: AxiosInstance = axios.create({
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

// Type definitions
export interface User {
  id: number;
  username: string;
  email: string;
  full_name?: string;
  role: string;
  is_active: boolean;
  created_at: string;
}

export interface Campaign {
  id: number;
  name: string;
  description?: string;
  mode: 'normal' | 'stealth' | 'turbo' | 'smart';
  status: 'pending' | 'running' | 'paused' | 'completed' | 'failed' | 'cancelled';
  targets: string[];
  target_count: number;
  waves: number;
  delay_seconds: number;
  use_proxy: boolean;
  use_vpn: boolean;
  randomize_apis: boolean;
  total_requests: number;
  successful_requests: number;
  failed_requests: number;
  success_rate: number;
  started_at?: string;
  completed_at?: string;
  created_at: string;
}

export interface APIGateway {
  id: number;
  name: string;
  url: string;
  status: 'active' | 'inactive' | 'rate_limited' | 'error';
  is_enabled: boolean;
  total_requests: number;
  successful_requests: number;
  failed_requests: number;
  success_rate: number;
  avg_response_time_ms: number;
  country?: string;
  provider?: string;
}

export interface DashboardStats {
  total_campaigns: number;
  active_campaigns: number;
  completed_campaigns: number;
  success_rate: number;
  total_sms_sent: number;
  sms_sent_today: number;
  active_apis: number;
  total_apis: number;
}

// API methods
export const authAPI = {
  register: (data: { username: string; email: string; password: string; full_name?: string }) =>
    api.post<User>('/auth/register', data),
  
  login: (data: { username: string; password: string }) =>
    api.post<{ access_token: string; refresh_token: string; token_type: string }>('/auth/login', data),
  
  getCurrentUser: () => api.get<User>('/auth/me'),
  
  logout: () => api.post('/auth/logout'),
};

export const campaignAPI = {
  create: (data: Partial<Campaign>) => api.post<Campaign>('/campaigns', data),
  
  getAll: (params?: { skip?: number; limit?: number; status?: string }) =>
    api.get<Campaign[]>('/campaigns', { params }),
  
  getById: (id: number) => api.get<Campaign>(`/campaigns/${id}`),
  
  update: (id: number, data: Partial<Campaign>) =>
    api.patch<Campaign>(`/campaigns/${id}`, data),
  
  delete: (id: number) => api.delete(`/campaigns/${id}`),
  
  start: (id: number) => api.post<Campaign>(`/campaigns/${id}/start`),
  
  pause: (id: number) => api.post<Campaign>(`/campaigns/${id}/pause`),
  
  cancel: (id: number) => api.post<Campaign>(`/campaigns/${id}/cancel`),
  
  getLogs: (id: number, params?: { skip?: number; limit?: number }) =>
    api.get(`/campaigns/${id}/logs`, { params }),
};

export const apiGatewayAPI = {
  getAll: (params?: { skip?: number; limit?: number; status?: string; search?: string }) =>
    api.get<APIGateway[]>('/apis', { params }),
  
  getById: (id: number) => api.get<APIGateway>(`/apis/${id}`),
  
  getStats: () => api.get('/apis/stats/summary'),
};

export const dashboardAPI = {
  getStats: () => api.get<DashboardStats>('/dashboard/stats'),
  
  getRecentCampaigns: (limit?: number) =>
    api.get<Campaign[]>('/dashboard/recent-campaigns', { params: { limit } }),
  
  getActivityChart: (days?: number) =>
    api.get<{ labels: string[]; campaigns: number[]; sms_sent: number[] }>('/dashboard/activity-chart', { params: { days } }),
};