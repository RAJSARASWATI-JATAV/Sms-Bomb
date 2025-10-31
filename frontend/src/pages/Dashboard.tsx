import { useEffect, useState } from 'react'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'
import { Progress } from '@/components/ui/progress'
import { 
  Zap, 
  Target, 
  TrendingUp, 
  Activity, 
  CheckCircle2, 
  XCircle,
  Clock,
  ArrowRight
} from 'lucide-react'
import { Link } from 'react-router-dom'
import { dashboardAPI, type DashboardStats, type Campaign } from '@/lib/api'

export function Dashboard() {
  const [stats, setStats] = useState<DashboardStats | null>(null)
  const [recentCampaigns, setRecentCampaigns] = useState<Campaign[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    loadDashboardData()
  }, [])

  const loadDashboardData = async () => {
    try {
      const [statsRes, campaignsRes] = await Promise.all([
        dashboardAPI.getStats(),
        dashboardAPI.getRecentCampaigns(5)
      ])
      setStats(statsRes.data)
      setRecentCampaigns(campaignsRes.data)
    } catch (error) {
      console.error('Failed to load dashboard data:', error)
    } finally {
      setLoading(false)
    }
  }

  if (loading) {
    return (
      <div className="flex items-center justify-center h-96">
        <div className="w-8 h-8 border-4 border-neon-blue border-t-transparent rounded-full animate-spin" />
      </div>
    )
  }

  const statCards = stats ? [
    {
      title: 'Total Campaigns',
      value: stats.total_campaigns.toLocaleString(),
      change: `${stats.completed_campaigns} completed`,
      icon: Target,
      color: 'text-neon-blue',
      bgColor: 'bg-neon-blue/10'
    },
    {
      title: 'Success Rate',
      value: `${stats.success_rate.toFixed(1)}%`,
      change: stats.active_campaigns > 0 ? `${stats.active_campaigns} active` : 'No active campaigns',
      icon: TrendingUp,
      color: 'text-neon-green',
      bgColor: 'bg-neon-green/10'
    },
    {
      title: 'Active APIs',
      value: `${stats.active_apis}/${stats.total_apis}`,
      change: `${((stats.active_apis / stats.total_apis) * 100).toFixed(1)}%`,
      icon: Activity,
      color: 'text-neon-purple',
      bgColor: 'bg-neon-purple/10'
    },
    {
      title: 'SMS Sent Today',
      value: stats.sms_sent_today.toLocaleString(),
      change: `${stats.total_sms_sent.toLocaleString()} total`,
      icon: Zap,
      color: 'text-neon-orange',
      bgColor: 'bg-neon-orange/10'
    },
  ] : []

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'completed': return 'text-neon-green'
      case 'running': return 'text-neon-blue'
      case 'paused': return 'text-neon-orange'
      case 'failed': return 'text-error'
      default: return 'text-text-secondary'
    }
  }

  const getModeColor = (mode: string) => {
    switch (mode) {
      case 'turbo': return 'bg-neon-orange/20 text-neon-orange'
      case 'stealth': return 'bg-neon-purple/20 text-neon-purple'
      case 'smart': return 'bg-neon-blue/20 text-neon-blue'
      default: return 'bg-neon-green/20 text-neon-green'
    }
  }

  return (
    <div className="space-y-6">
      {/* Page Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="heading-lg text-neon-green">Dashboard</h1>
          <p className="text-text-secondary mt-1">Monitor your SMS campaigns in real-time</p>
        </div>
        <Link to="/campaign">
          <Button className="bg-gradient-to-r from-neon-green to-neon-blue hover:opacity-90 text-dark font-semibold glow-green">
            <Zap className="w-4 h-4 mr-2" />
            New Campaign
          </Button>
        </Link>
      </div>

      {/* Stats Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {statCards.map((stat) => (
          <Card key={stat.title} className="glass border-neon-blue/20 hover:glow-blue transition-all duration-300">
            <CardHeader className="flex flex-row items-center justify-between pb-2">
              <CardTitle className="text-sm font-medium text-text-secondary">
                {stat.title}
              </CardTitle>
              <div className={`${stat.bgColor} p-2 rounded-lg`}>
                <stat.icon className={`w-4 h-4 ${stat.color}`} />
              </div>
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold text-text-primary">{stat.value}</div>
              <p className="text-xs text-neon-green mt-1">
                {stat.change} from last month
              </p>
            </CardContent>
          </Card>
        ))}
      </div>

      {/* Main Content Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Recent Campaigns */}
        <Card className="lg:col-span-2 glass border-neon-blue/20">
          <CardHeader>
            <CardTitle className="text-neon-pink">Recent Campaigns</CardTitle>
            <CardDescription>Your latest SMS bombing operations</CardDescription>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              {recentCampaigns.length > 0 ? (
                recentCampaigns.map((campaign) => (
                  <div
                    key={campaign.id}
                    className="flex items-center justify-between p-4 rounded-lg bg-dark-elevated hover:bg-dark-elevated/80 transition-colors"
                  >
                    <div className="flex items-center gap-4">
                      <div className={`w-10 h-10 rounded-lg flex items-center justify-center ${
                        campaign.status === 'completed' ? 'bg-neon-green/10' :
                        campaign.status === 'running' ? 'bg-neon-blue/10' :
                        campaign.status === 'failed' ? 'bg-error/10' :
                        'bg-neon-orange/10'
                      }`}>
                        {campaign.status === 'completed' && <CheckCircle2 className="w-5 h-5 text-neon-green" />}
                        {campaign.status === 'running' && <Clock className="w-5 h-5 text-neon-blue animate-pulse" />}
                        {campaign.status === 'failed' && <XCircle className="w-5 h-5 text-error" />}
                        {campaign.status === 'paused' && <Clock className="w-5 h-5 text-neon-orange" />}
                      </div>
                      <div>
                        <p className="font-medium text-text-primary">{campaign.name}</p>
                        <p className="text-sm text-text-secondary">{campaign.target_count} targets • {campaign.successful_requests} sent</p>
                      </div>
                    </div>
                    <div className="text-right">
                      <Badge className={getModeColor(campaign.mode)}>
                        {campaign.mode}
                      </Badge>
                      <p className={`text-xs mt-1 ${getStatusColor(campaign.status)}`}>
                        {campaign.status} • {campaign.success_rate.toFixed(1)}%
                      </p>
                    </div>
                  </div>
                ))
              ) : (
                <div className="text-center py-8 text-text-muted">
                  <p>No campaigns yet</p>
                  <Link to="/campaign">
                    <Button variant="link" className="text-neon-blue mt-2">
                      Create your first campaign
                    </Button>
                  </Link>
                </div>
              )}
            </div>
          </CardContent>
        </Card>

        {/* Quick Actions & System Status */}
        <div className="space-y-6">
          {/* Quick Actions */}
          <Card className="glass border-neon-blue/20">
            <CardHeader>
              <CardTitle className="text-neon-blue">Quick Actions</CardTitle>
            </CardHeader>
            <CardContent className="space-y-3">
              <Link to="/campaign">
                <Button className="w-full justify-between" variant="outline">
                  Start Campaign
                  <ArrowRight className="w-4 h-4" />
                </Button>
              </Link>
              <Link to="/analytics">
                <Button className="w-full justify-between" variant="outline">
                  View Analytics
                  <ArrowRight className="w-4 h-4" />
                </Button>
              </Link>
              <Link to="/api-status">
                <Button className="w-full justify-between" variant="outline">
                  Check APIs
                  <ArrowRight className="w-4 h-4" />
                </Button>
              </Link>
            </CardContent>
          </Card>

          {/* System Status */}
          <Card className="glass border-neon-blue/20">
            <CardHeader>
              <CardTitle className="text-neon-purple">System Status</CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              <div>
                <div className="flex justify-between text-sm mb-2">
                  <span className="text-text-secondary">CPU Usage</span>
                  <span className="text-neon-green">34%</span>
                </div>
                <Progress value={34} className="h-2" />
              </div>
              <div>
                <div className="flex justify-between text-sm mb-2">
                  <span className="text-text-secondary">Memory</span>
                  <span className="text-neon-blue">58%</span>
                </div>
                <Progress value={58} className="h-2" />
              </div>
              <div>
                <div className="flex justify-between text-sm mb-2">
                  <span className="text-text-secondary">API Health</span>
                  <span className="text-neon-purple">93%</span>
                </div>
                <Progress value={93} className="h-2" />
              </div>
            </CardContent>
          </Card>
        </div>
      </div>
    </div>
  )
}