import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Input } from '@/components/ui/input'
import { Button } from '@/components/ui/button'
import { Progress } from '@/components/ui/progress'
import { CheckCircle2, XCircle, Clock, Search, RefreshCw } from 'lucide-react'
import { useState } from 'react'

const apiData = [
  { name: 'OLA', status: 'active', success: 156, failed: 12, rate: 92.8, responseTime: 1.2 },
  { name: 'Paytm', status: 'active', success: 203, failed: 8, rate: 96.2, responseTime: 0.9 },
  { name: 'Flipkart', status: 'active', success: 189, failed: 15, rate: 92.6, responseTime: 1.5 },
  { name: 'Amazon', status: 'inactive', success: 45, failed: 67, rate: 40.2, responseTime: 3.2 },
  { name: 'Zomato', status: 'active', success: 178, failed: 9, rate: 95.2, responseTime: 1.1 },
  { name: 'Swiggy', status: 'active', success: 167, failed: 11, rate: 93.8, responseTime: 1.3 },
  { name: 'PhonePe', status: 'active', success: 198, failed: 7, rate: 96.6, responseTime: 0.8 },
  { name: 'MakeMyTrip', status: 'checking', success: 0, failed: 0, rate: 0, responseTime: 0 },
  { name: 'Myntra', status: 'active', success: 145, failed: 13, rate: 91.8, responseTime: 1.4 },
  { name: 'BigBasket', status: 'active', success: 134, failed: 16, rate: 89.3, responseTime: 1.6 },
]

export function ApiStatus() {
  const [searchTerm, setSearchTerm] = useState('')

  const filteredApis = apiData.filter(api =>
    api.name.toLowerCase().includes(searchTerm.toLowerCase())
  )

  const activeCount = apiData.filter(api => api.status === 'active').length
  const inactiveCount = apiData.filter(api => api.status === 'inactive').length
  const avgSuccessRate = (apiData.reduce((acc, api) => acc + api.rate, 0) / apiData.length).toFixed(1)

  return (
    <div className="space-y-6">
      {/* Page Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="heading-lg text-neon-purple">API Status</h1>
          <p className="text-text-secondary mt-1">Monitor health and performance of all SMS gateways</p>
        </div>
        <Button variant="outline" className="gap-2">
          <RefreshCw className="w-4 h-4" />
          Refresh All
        </Button>
      </div>

      {/* Stats Overview */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
        <Card className="glass border-neon-blue/20">
          <CardHeader className="pb-2">
            <CardTitle className="text-sm font-medium text-text-secondary">Total APIs</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold text-text-primary">{apiData.length}</div>
            <p className="text-xs text-neon-blue mt-1">Configured gateways</p>
          </CardContent>
        </Card>

        <Card className="glass border-neon-green/20">
          <CardHeader className="pb-2">
            <CardTitle className="text-sm font-medium text-text-secondary">Active</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold text-neon-green">{activeCount}</div>
            <p className="text-xs text-text-secondary mt-1">{((activeCount / apiData.length) * 100).toFixed(0)}% operational</p>
          </CardContent>
        </Card>

        <Card className="glass border-error/20">
          <CardHeader className="pb-2">
            <CardTitle className="text-sm font-medium text-text-secondary">Inactive</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold text-error">{inactiveCount}</div>
            <p className="text-xs text-text-secondary mt-1">Need attention</p>
          </CardContent>
        </Card>

        <Card className="glass border-neon-orange/20">
          <CardHeader className="pb-2">
            <CardTitle className="text-sm font-medium text-text-secondary">Avg Success</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold text-neon-orange">{avgSuccessRate}%</div>
            <p className="text-xs text-text-secondary mt-1">Overall performance</p>
          </CardContent>
        </Card>
      </div>

      {/* Search and Filter */}
      <Card className="glass border-neon-blue/20">
        <CardHeader>
          <CardTitle className="text-neon-blue">API Gateway List</CardTitle>
          <CardDescription>Real-time status of all SMS APIs</CardDescription>
        </CardHeader>
        <CardContent>
          <div className="mb-6">
            <div className="relative">
              <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 w-4 h-4 text-text-muted" />
              <Input
                placeholder="Search APIs..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="pl-10 bg-dark-elevated border-neon-blue/30"
              />
            </div>
          </div>

          <div className="space-y-3">
            {filteredApis.map((api) => (
              <div
                key={api.name}
                className="p-4 rounded-lg bg-dark-elevated hover:bg-dark-elevated/80 transition-colors border border-neon-blue/10"
              >
                <div className="flex items-center justify-between mb-3">
                  <div className="flex items-center gap-3">
                    <div className={`w-10 h-10 rounded-lg flex items-center justify-center ${
                      api.status === 'active' ? 'bg-neon-green/10' :
                      api.status === 'checking' ? 'bg-neon-blue/10' :
                      'bg-error/10'
                    }`}>
                      {api.status === 'active' && <CheckCircle2 className="w-5 h-5 text-neon-green" />}
                      {api.status === 'checking' && <Clock className="w-5 h-5 text-neon-blue animate-pulse" />}
                      {api.status === 'inactive' && <XCircle className="w-5 h-5 text-error" />}
                    </div>
                    <div>
                      <h3 className="font-semibold text-text-primary">{api.name}</h3>
                      <p className="text-xs text-text-muted">
                        Response: {api.responseTime}s
                      </p>
                    </div>
                  </div>
                  <Badge variant={
                    api.status === 'active' ? 'default' :
                    api.status === 'checking' ? 'secondary' :
                    'destructive'
                  }>
                    {api.status}
                  </Badge>
                </div>

                <div className="grid grid-cols-3 gap-4 mb-3">
                  <div>
                    <p className="text-xs text-text-muted">Success</p>
                    <p className="text-sm font-semibold text-neon-green">{api.success}</p>
                  </div>
                  <div>
                    <p className="text-xs text-text-muted">Failed</p>
                    <p className="text-sm font-semibold text-error">{api.failed}</p>
                  </div>
                  <div>
                    <p className="text-xs text-text-muted">Success Rate</p>
                    <p className="text-sm font-semibold text-neon-blue">{api.rate}%</p>
                  </div>
                </div>

                <div>
                  <div className="flex justify-between text-xs mb-1">
                    <span className="text-text-muted">Performance</span>
                    <span className="text-neon-blue">{api.rate}%</span>
                  </div>
                  <Progress value={api.rate} className="h-2" />
                </div>
              </div>
            ))}
          </div>
        </CardContent>
      </Card>
    </div>
  )
}