import { createContext, useContext, useState, useEffect, type ReactNode } from 'react';
import { authAPI, type User } from '@/lib/api';
import wsClient from '@/lib/websocket';

interface AuthContextType {
  user: User | null;
  loading: boolean;
  login: (username: string, password: string) => Promise<void>;
  logout: () => void;
  isAuthenticated: boolean;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    checkAuth();
  }, []);

  const checkAuth = async () => {
    const token = localStorage.getItem('access_token');
    if (token) {
      try {
        const response = await authAPI.getCurrentUser();
        setUser(response.data);
        
        // Connect WebSocket
        try {
          await wsClient.connect(token);
          console.log('✅ WebSocket connected on auth check');
        } catch (error) {
          console.error('Failed to connect WebSocket:', error);
        }
      } catch (error) {
        localStorage.removeItem('access_token');
      }
    }
    setLoading(false);
  };

  const login = async (username: string, password: string) => {
    const response = await authAPI.login({ username, password });
    const token = response.data.access_token;
    localStorage.setItem('access_token', token);
    const userResponse = await authAPI.getCurrentUser();
    setUser(userResponse.data);
    
    // Connect WebSocket
    try {
      await wsClient.connect(token);
      console.log('✅ WebSocket connected on login');
    } catch (error) {
      console.error('Failed to connect WebSocket:', error);
    }
  };

  const logout = () => {
    localStorage.removeItem('access_token');
    setUser(null);
    
    // Disconnect WebSocket
    wsClient.disconnect();
    console.log('🔌 WebSocket disconnected on logout');
    
    window.location.href = '/login';
  };

  return (
    <AuthContext.Provider value={{ user, loading, login, logout, isAuthenticated: !!user }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
}