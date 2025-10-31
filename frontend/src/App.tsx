import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import { AuthProvider } from '@/contexts/AuthContext'
import { Layout } from '@/components/layout/Layout'
import { Dashboard } from '@/pages/Dashboard'
import { CampaignBuilder } from '@/pages/CampaignBuilder'
import { Analytics } from '@/pages/Analytics'
import { ApiStatus } from '@/pages/ApiStatus'
import { Settings } from '@/pages/Settings'
import { Login } from '@/pages/Login'

function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/" element={<Layout />}>
            <Route index element={<Dashboard />} />
            <Route path="campaign" element={<CampaignBuilder />} />
            <Route path="analytics" element={<Analytics />} />
            <Route path="api-status" element={<ApiStatus />} />
            <Route path="settings" element={<Settings />} />
            <Route path="*" element={<Navigate to="/" replace />} />
          </Route>
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  )
}

export default App