import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs'
import { Button } from '@/components/ui/button'
import { 
  BarChart, 
  Bar, 
  LineChart, 
  Line, 
  PieChart, 
  Pie, 
  Cell,
  XAxis, 
  YAxis, 
  CartesianGrid, 
  Tooltip, 
  Legend,
  ResponsiveContainer
} from 'recharts'
import { Download, TrendingUp, Target, Zap } from 'lucide-react'

const successRateData = [
  { name: 'Mon', rate: 92 },
  { name: 'Tue', rate: 95 },
  { name: 'Wed', rate: 88 },
  { name: 'Thu', rate: 97 },
  { name: 'Fri', rate: 94 },
  { name: 'Sat', rate: 96 },
  { name: 'Sun', rate: 93 },
]

const campaignData = [
  { name: 'Jan', campaigns: 120 },
  { name: 'Feb', campaigns: 145 },
  { name: 'Mar', campaigns: 167 },
  { name: 'Apr', campaigns: 189 },
  { name: 'May', campaigns: 203 },
  { name: 'Jun', campaigns: 234 },
]

const modeDistribution = [
  { name: 'Normal', value: 45, color: '#00d9ff' },
  { name: 'Stealth', value: 25, color: '#b537f2' },
  { name: 'Turbo', value: 20, color: '#ff9500' },
  { name: 'Smart', value: 10, color: '#ff006e' },
]

export function Analytics() {
  return (
    <div className="space-y-6">
      {/* Page Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="heading-lg text-neon-orange">Analytics</h1>
          <p className="text-text-secondary mt-1">Comprehensive campaign insights and statistics</p>
        </div>
        <Button variant="outline" className="gap-2">
          <Download className="w-4 h-4" />
          Export Report
        </Button>
      </div>

      {/* Stats Overview */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
        {[
          { title: 'Total Campaigns', value: '1,247', icon: Target, color: 'text-neon-blue' },
          { title: 'Avg Success Rate', value: '94.2%', icon: TrendingUp, color: 'text-neon-green' },
          { title: 'Total SMS Sent', value: '892K', icon: Zap, color: 'text-neon-orange' },
          { title: 'Active Today', value: '34', icon: Target, color: 'text-neon-pink' },
        ].map((stat) => (
          <Card key={stat.title} className="glass border-neon-blue/20">
            <CardHeader className="flex flex-row items-center justify-between pb-2">
              <CardTitle className="text-sm font-medium text-text-secondary">
                {stat.title}
              </CardTitle>
              <stat.icon className={`w-4 h-4 ${stat.color}`} />
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold text-text-primary">{stat.value}</div>
            </CardContent>
          </Card>
        ))}
      </div>

      {/* Charts */}
      <Tabs defaultValue="success" className="space-y-6">
        <TabsList>
          <TabsTrigger value="success">Success Rate</TabsTrigger>
          <TabsTrigger value="campaigns">Campaigns</TabsTrigger>
          <TabsTrigger value="modes">Mode Distribution</TabsTrigger>
        </TabsList>

        <TabsContent value="success">
          <Card className="glass border-neon-blue/20">
            <CardHeader>
              <CardTitle className="text-neon-green">Success Rate Trend</CardTitle>
              <CardDescription>Weekly success rate percentage</CardDescription>
            </CardHeader>
            <CardContent>
              <div className="h-80">
                <ResponsiveContainer width="100%" height="100%">
                  <LineChart data={successRateData}>
                    <CartesianGrid strokeDasharray="3 3" stroke="#1a1f3a" />
                    <XAxis dataKey="name" stroke="#b8c1ec" />
                    <YAxis stroke="#b8c1ec" />
                    <Tooltip 
                      contentStyle={{ 
                        backgroundColor: '#1a1f3a', 
                        border: '1px solid #00d9ff',
                        borderRadius: '8px'
                      }}
                    />
                    <Line 
                      type="monotone" 
                      dataKey="rate" 
                      stroke="#00ff41" 
                      strokeWidth={3}
                      dot={{ fill: '#00ff41', r: 6 }}
                    />
                  </LineChart>
                </ResponsiveContainer>
              </div>
            </CardContent>
          </Card>
        </TabsContent>

        <TabsContent value="campaigns">
          <Card className="glass border-neon-blue/20">
            <CardHeader>
              <CardTitle className="text-neon-blue">Campaign Volume</CardTitle>
              <CardDescription>Monthly campaign statistics</CardDescription>
            </CardHeader>
            <CardContent>
              <div className="h-80">
                <ResponsiveContainer width="100%" height="100%">
                  <BarChart data={campaignData}>
                    <CartesianGrid strokeDasharray="3 3" stroke="#1a1f3a" />
                    <XAxis dataKey="name" stroke="#b8c1ec" />
                    <YAxis stroke="#b8c1ec" />
                    <Tooltip 
                      contentStyle={{ 
                        backgroundColor: '#1a1f3a', 
                        border: '1px solid #00d9ff',
                        borderRadius: '8px'
                      }}
                    />
                    <Bar dataKey="campaigns" fill="#00d9ff" radius={[8, 8, 0, 0]} />
                  </BarChart>
                </ResponsiveContainer>
              </div>
            </CardContent>
          </Card>
        </TabsContent>

        <TabsContent value="modes">
          <Card className="glass border-neon-blue/20">
            <CardHeader>
              <CardTitle className="text-neon-purple">Mode Distribution</CardTitle>
              <CardDescription>Usage by bombing mode</CardDescription>
            </CardHeader>
            <CardContent>
              <div className="h-80">
                <ResponsiveContainer width="100%" height="100%">
                  <PieChart>
                    <Pie
                      data={modeDistribution}
                      cx="50%"
                      cy="50%"
                      labelLine={false}
                      label={({ name, percent }) => `${name} ${(percent * 100).toFixed(0)}%`}
                      outerRadius={120}
                      fill="#8884d8"
                      dataKey="value"
                    >
                      {modeDistribution.map((entry, index) => (
                        <Cell key={`cell-${index}`} fill={entry.color} />
                      ))}
                    </Pie>
                    <Tooltip 
                      contentStyle={{ 
                        backgroundColor: '#1a1f3a', 
                        border: '1px solid #00d9ff',
                        borderRadius: '8px'
                      }}
                    />
                  </PieChart>
                </ResponsiveContainer>
              </div>
            </CardContent>
          </Card>
        </TabsContent>
      </Tabs>
    </div>
  )
}