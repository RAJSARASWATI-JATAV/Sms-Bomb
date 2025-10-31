import { useEffect, useState } from 'react'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Input } from '@/components/ui/input'
import { Button } from '@/components/ui/button'
import { Progress } from '@/components/ui/progress'
import { CheckCircle2, XCircle, Clock, Search, RefreshCw } from 'lucide-react'
import { apiGatewayAPI, type APIGateway } from '@/lib/api'

export function ApiStatus() {
  const [searchTerm, setSearchTerm] = useState('')
  const [apis, setApis] = useState<APIGateway[]>([])
  const [loading, setLoading] = useState(true)
  const [refreshing, setRefreshing] = useState(false)

  useEffect(() => {
    loadApis()
  }, [])

  const loadApis = async () => {
    try {
      const response = await apiGatewayAPI.getAll({ limit: 100 })
      setApis(response.data)
    } catch (error) {
      console.error('Failed to load APIs:', error)
    } finally {
      setLoading(false)
      setRefreshing(false)
    }
  }

  const handleRefresh = () => {
    setRefreshing(true)
    loadApis()
  }

  const filteredApis = apis.filter(api =>
    api.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
    api.provider?.toLowerCase().includes(searchTerm.toLowerCase()) ||
    api.country?.toLowerCase().includes(searchTerm.toLowerCase())
  )

  const activeCount = apis.filter(api => api.status === 'active' && api.is_enabled).length
  const inactiveCount = apis.filter(api => api.status !== 'active' || !api.is_enabled).length
  const avgSuccessRate = apis.length > 0 
    ? (apis.reduce((acc, api) => acc + api.success_rate, 0) / apis.length).toFixed(1)
    : '0.0'

  if (loading) {
    return (
      <div className="flex items-center justify-center h-96">
        <div className="w-8 h-8 border-4 border-neon-blue border-t-transparent rounded-full animate-spin" />
      </div>
    )
  }

  return (
    <div className="space-y-6">
      {/* Page Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="heading-lg text-neon-purple">API Status</h1>
          <p className="text-text-secondary mt-1">Monitor health and performance of all SMS gateways</p>
        </div>
        <Button 
          variant="outline" 
          className="gap-2"
          onClick={handleRefresh}
          disabled={refreshing}
        >
          <RefreshCw className={`w-4 h-4 ${refreshing ? 'animate-spin' : ''}`} />
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
            <div className="text-2xl font-bold text-text-primary">{apis.length}</div>
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