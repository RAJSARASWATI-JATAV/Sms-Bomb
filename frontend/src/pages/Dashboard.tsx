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

export function Dashboard() {
  const stats = [
    {
      title: 'Total Campaigns',
      value: '1,247',
      change: '+12.5%',
      icon: Target,
      color: 'text-neon-blue',
      bgColor: 'bg-neon-blue/10'
    },
    {
      title: 'Success Rate',
      value: '96.8%',
      change: '+2.3%',
      icon: TrendingUp,
      color: 'text-neon-green',
      bgColor: 'bg-neon-green/10'
    },
    {
      title: 'Active APIs',
      value: '187/200',
      change: '93.5%',
      icon: Activity,
      color: 'text-neon-purple',
      bgColor: 'bg-neon-purple/10'
    },
    {
      title: 'SMS Sent Today',
      value: '45,892',
      change: '+18.2%',
      icon: Zap,
      color: 'text-neon-orange',
      bgColor: 'bg-neon-orange/10'
    },
  ]

  const recentCampaigns = [
    { id: 1, target: '+91 98765 43210', status: 'success', sms: 156, time: '2 mins ago' },
    { id: 2, target: '+91 87654 32109', status: 'running', sms: 89, time: '5 mins ago' },
    { id: 3, target: '+91 76543 21098', status: 'success', sms: 203, time: '12 mins ago' },
    { id: 4, target: '+91 65432 10987', status: 'failed', sms: 45, time: '18 mins ago' },
  ]

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
        {stats.map((stat) => (
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
              {recentCampaigns.map((campaign) => (
                <div
                  key={campaign.id}
                  className="flex items-center justify-between p-4 rounded-lg bg-dark-elevated hover:bg-dark-elevated/80 transition-colors"
                >
                  <div className="flex items-center gap-4">
                    <div className={`w-10 h-10 rounded-lg flex items-center justify-center ${
                      campaign.status === 'success' ? 'bg-neon-green/10' :
                      campaign.status === 'running' ? 'bg-neon-blue/10' :
                      'bg-error/10'
                    }`}>
                      {campaign.status === 'success' && <CheckCircle2 className="w-5 h-5 text-neon-green" />}
                      {campaign.status === 'running' && <Clock className="w-5 h-5 text-neon-blue animate-pulse" />}
                      {campaign.status === 'failed' && <XCircle className="w-5 h-5 text-error" />}
                    </div>
                    <div>
                      <p className="font-medium text-text-primary">{campaign.target}</p>
                      <p className="text-sm text-text-secondary">{campaign.sms} SMS sent</p>
                    </div>
                  </div>
                  <div className="text-right">
                    <Badge variant={
                      campaign.status === 'success' ? 'default' :
                      campaign.status === 'running' ? 'secondary' :
                      'destructive'
                    }>
                      {campaign.status}
                    </Badge>
                    <p className="text-xs text-text-muted mt-1">{campaign.time}</p>
                  </div>
                </div>
              ))}
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