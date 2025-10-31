import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Button } from '@/components/ui/button'
import { Textarea } from '@/components/ui/textarea'
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select'
import { Slider } from '@/components/ui/slider'
import { Switch } from '@/components/ui/switch'
import { Badge } from '@/components/ui/badge'
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs'
import { Alert, AlertDescription } from '@/components/ui/alert'
import { 
  Target, 
  Zap, 
  Shield, 
  Rocket, 
  Brain,
  Upload,
  Play,
  Pause,
  AlertCircle,
  CheckCircle2
} from 'lucide-react'
import { campaignAPI } from '@/lib/api'

export function CampaignBuilder() {
  const navigate = useNavigate()
  const [mode, setMode] = useState<'normal' | 'stealth' | 'turbo' | 'smart'>('normal')
  const [waves, setWaves] = useState([50])
  const [delay, setDelay] = useState([2])
  const [campaignName, setCampaignName] = useState('')
  const [description, setDescription] = useState('')
  const [phoneNumber, setPhoneNumber] = useState('')
  const [bulkTargets, setBulkTargets] = useState('')
  const [useProxy, setUseProxy] = useState(false)
  const [useVPN, setUseVPN] = useState(false)
  const [randomizeAPIs, setRandomizeAPIs] = useState(true)
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState('')
  const [success, setSuccess] = useState(false)

  const handleLaunch = async () => {
    setError('')
    setSuccess(false)
    setIsLoading(true)

    try {
      // Validate inputs
      if (!campaignName.trim()) {
        throw new Error('Campaign name is required')
      }

      const targets = phoneNumber ? [phoneNumber] : bulkTargets.split('\n').filter(t => t.trim())
      
      if (targets.length === 0) {
        throw new Error('At least one target phone number is required')
      }

      // Create campaign
      const response = await campaignAPI.create({
        name: campaignName,
        description: description || undefined,
        mode,
        targets,
        waves: waves[0],
        delay_seconds: delay[0],
        use_proxy: useProxy,
        use_vpn: useVPN,
        randomize_apis: randomizeAPIs
      })

      setSuccess(true)
      
      // Redirect to dashboard after 2 seconds
      setTimeout(() => {
        navigate('/')
      }, 2000)
    } catch (err: any) {
      setError(err.response?.data?.detail || err.message || 'Failed to create campaign')
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div className="space-y-6">
      {/* Page Header */}
      <div>
        <h1 className="heading-lg text-neon-pink">Campaign Builder</h1>
        <p className="text-text-secondary mt-1">Create and launch your SMS bombing campaign</p>
      </div>

      {/* Status Messages */}
      {error && (
        <Alert variant="destructive" className="bg-error/10 border-error/30">
          <AlertCircle className="h-4 w-4" />
          <AlertDescription>{error}</AlertDescription>
        </Alert>
      )}

      {success && (
        <Alert className="bg-neon-green/10 border-neon-green/30">
          <CheckCircle2 className="h-4 w-4 text-neon-green" />
          <AlertDescription className="text-neon-green">
            Campaign created successfully! Redirecting to dashboard...
          </AlertDescription>
        </Alert>
      )}

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Main Configuration */}
        <div className="lg:col-span-2 space-y-6">
          {/* Target Configuration */}
          <Card className="glass border-neon-blue/20">
            <CardHeader>
              <CardTitle className="flex items-center gap-2 text-neon-blue">
                <Target className="w-5 h-5" />
                Target Configuration
              </CardTitle>
              <CardDescription>Enter target phone number(s)</CardDescription>
            </CardHeader>
            <CardContent>
              <Tabs defaultValue="single">
                <TabsList className="grid w-full grid-cols-2">
                  <TabsTrigger value="single">Single Target</TabsTrigger>
                  <TabsTrigger value="bulk">Bulk Upload</TabsTrigger>
                </TabsList>
                <TabsContent value="single" className="space-y-4">
                  <div>
                    <Label htmlFor="phone">Phone Number</Label>
                    <Input
                      id="phone"
                      placeholder="+1234567890"
                      className="mt-2 bg-dark-elevated border-neon-blue/30"
                      value={phoneNumber}
                      onChange={(e) => setPhoneNumber(e.target.value)}
                    />
                    <p className="text-xs text-text-muted mt-1">
                      Enter phone number with country code
                    </p>
                  </div>
                </TabsContent>
                <TabsContent value="bulk" className="space-y-4">
                  <div>
                    <Label htmlFor="bulk">Bulk Phone Numbers</Label>
                    <Textarea
                      id="bulk"
                      placeholder="Enter one phone number per line&#10;+1234567890&#10;+0987654321"
                      className="mt-2 bg-dark-elevated border-neon-blue/30 min-h-[150px]"
                      value={bulkTargets}
                      onChange={(e) => setBulkTargets(e.target.value)}
                    />
                    <p className="text-xs text-text-muted mt-1">
                      Enter one phone number per line (max 1000)
                    </p>
                  </div>
                </TabsContent>
              </Tabs>
            </CardContent>
          </Card>

          {/* Campaign Details */}
          <Card className="glass border-neon-blue/20">
            <CardHeader>
              <CardTitle className="text-neon-purple">Campaign Details</CardTitle>
              <CardDescription>Basic campaign information</CardDescription>
            </CardHeader>
            <CardContent className="space-y-4">
              <div>
                <Label htmlFor="campaign-name">Campaign Name *</Label>
                <Input
                  id="campaign-name"
                  placeholder="My Campaign"
                  className="mt-2 bg-dark-elevated border-neon-blue/30"
                  value={campaignName}
                  onChange={(e) => setCampaignName(e.target.value)}
                  required
                />
              </div>
              <div>
                <Label htmlFor="campaign-description">Description (Optional)</Label>
                <Textarea
                  id="campaign-description"
                  placeholder="Campaign description..."
                  className="mt-2 bg-dark-elevated border-neon-blue/30"
                  value={description}
                  onChange={(e) => setDescription(e.target.value)}
                />
              </div>
            </CardContent>
          </Card>

          {/* Mode Selection */}
          <Card className="glass border-neon-blue/20">
            <CardHeader>
              <CardTitle className="flex items-center gap-2 text-neon-green">
                <Zap className="w-5 h-5" />
                Bombing Mode
              </CardTitle>
              <CardDescription>Select your attack strategy</CardDescription>
            </CardHeader>
            <CardContent>
              <div className="grid grid-cols-2 gap-4">
                <button
                  onClick={() => setMode('normal')}
                  className={`p-4 rounded-lg border-2 transition-all ${
                    mode === 'normal'
                      ? 'border-neon-blue bg-neon-blue/10 glow-blue'
                      : 'border-neon-blue/20 hover:border-neon-blue/50'
                  }`}
                >
                  <Zap className="w-8 h-8 text-neon-blue mb-2" />
                  <h3 className="font-semibold text-text-primary">Normal Mode</h3>
                  <p className="text-xs text-text-secondary mt-1">
                    Balanced speed with AI optimization
                  </p>
                </button>

                <button
                  onClick={() => setMode('stealth')}
                  className={`p-4 rounded-lg border-2 transition-all ${
                    mode === 'stealth'
                      ? 'border-neon-purple bg-neon-purple/10 glow-blue'
                      : 'border-neon-blue/20 hover:border-neon-blue/50'
                  }`}
                >
                  <Shield className="w-8 h-8 text-neon-purple mb-2" />
                  <h3 className="font-semibold text-text-primary">Stealth Mode</h3>
                  <p className="text-xs text-text-secondary mt-1">
                    Randomized patterns, slower
                  </p>
                </button>

                <button
                  onClick={() => setMode('turbo')}
                  className={`p-4 rounded-lg border-2 transition-all ${
                    mode === 'turbo'
                      ? 'border-neon-orange bg-neon-orange/10 glow-blue'
                      : 'border-neon-blue/20 hover:border-neon-blue/50'
                  }`}
                >
                  <Rocket className="w-8 h-8 text-neon-orange mb-2" />
                  <h3 className="font-semibold text-text-primary">Turbo Mode</h3>
                  <p className="text-xs text-text-secondary mt-1">
                    Maximum speed bombing
                  </p>
                </button>

                <button
                  onClick={() => setMode('smart')}
                  className={`p-4 rounded-lg border-2 transition-all ${
                    mode === 'smart'
                      ? 'border-neon-pink bg-neon-pink/10 glow-blue'
                      : 'border-neon-blue/20 hover:border-neon-blue/50'
                  }`}
                >
                  <Brain className="w-8 h-8 text-neon-pink mb-2" />
                  <h3 className="font-semibold text-text-primary">Smart Mode</h3>
                  <p className="text-xs text-text-secondary mt-1">
                    AI decides best strategy
                  </p>
                </button>
              </div>
            </CardContent>
          </Card>

          {/* Advanced Settings */}
          <Card className="glass border-neon-blue/20">
            <CardHeader>
              <CardTitle className="text-neon-purple">Advanced Settings</CardTitle>
            </CardHeader>
            <CardContent className="space-y-6">
              <div>
                <Label>Number of Waves: {waves[0]}</Label>
                <Slider
                  value={waves}
                  onValueChange={setWaves}
                  max={100}
                  min={1}
                  step={1}
                  className="mt-2"
                />
                <p className="text-xs text-text-muted mt-1">
                  Total SMS waves to send
                </p>
              </div>

              <div>
                <Label>Delay Between Waves: {delay[0]}s</Label>
                <Slider
                  value={delay}
                  onValueChange={setDelay}
                  max={10}
                  min={1}
                  step={1}
                  className="mt-2"
                />
                <p className="text-xs text-text-muted mt-1">
                  Seconds between each wave
                </p>
              </div>

              <div className="flex items-center justify-between">
                <div>
                  <Label>Enable Proxy Rotation</Label>
                  <p className="text-xs text-text-muted mt-1">
                    Use multiple proxies for stealth
                  </p>
                </div>
                <Switch checked={useProxy} onCheckedChange={setUseProxy} />
              </div>

              <div className="flex items-center justify-between">
                <div>
                  <Label>VPN Protection</Label>
                  <p className="text-xs text-text-muted mt-1">
                    Route through VPN servers
                  </p>
                </div>
                <Switch checked={useVPN} onCheckedChange={setUseVPN} />
              </div>

              <div className="flex items-center justify-between">
                <div>
                  <Label>Randomize API Selection</Label>
                  <p className="text-xs text-text-muted mt-1">
                    Random API gateway selection
                  </p>
                </div>
                <Switch checked={randomizeAPIs} onCheckedChange={setRandomizeAPIs} />
              </div>
            </CardContent>
          </Card>
        </div>

        {/* Preview & Launch */}
        <div className="space-y-6">
          {/* Campaign Preview */}
          <Card className="glass border-neon-blue/20">
            <CardHeader>
              <CardTitle className="text-neon-yellow">Campaign Preview</CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              <div className="flex justify-between">
                <span className="text-text-secondary">Mode:</span>
                <Badge variant="outline" className="border-neon-blue text-neon-blue">
                  {mode.toUpperCase()}
                </Badge>
              </div>
              <div className="flex justify-between">
                <span className="text-text-secondary">Waves:</span>
                <span className="text-text-primary font-semibold">{waves[0]}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-text-secondary">Delay:</span>
                <span className="text-text-primary font-semibold">{delay[0]}s</span>
              </div>
              <div className="flex justify-between">
                <span className="text-text-secondary">Est. Duration:</span>
                <span className="text-text-primary font-semibold">
                  {Math.ceil((waves[0] * delay[0]) / 60)} mins
                </span>
              </div>
              <div className="flex justify-between">
                <span className="text-text-secondary">Total SMS:</span>
                <span className="text-neon-green font-semibold">~{waves[0] * 15}</span>
              </div>
            </CardContent>
          </Card>

          {/* Launch Controls */}
          <Card className="glass border-neon-pink/20 glow-pink">
            <CardHeader>
              <CardTitle className="text-neon-pink">Launch Campaign</CardTitle>
            </CardHeader>
            <CardContent className="space-y-3">
              <Button 
                className="w-full bg-gradient-to-r from-neon-pink to-neon-orange hover:opacity-90 text-dark font-semibold"
                onClick={handleLaunch}
                disabled={isLoading || success}
              >
                {isLoading ? (
                  <>
                    <div className="w-4 h-4 border-2 border-dark border-t-transparent rounded-full animate-spin mr-2" />
                    Creating...
                  </>
                ) : (
                  <>
                    <Play className="w-4 h-4 mr-2" />
                    Create Campaign
                  </>
                )}
              </Button>
              <Button 
                variant="outline" 
                className="w-full"
                onClick={() => navigate('/')}
                disabled={isLoading}
              >
                <Pause className="w-4 h-4 mr-2" />
                Cancel
              </Button>
            </CardContent>
          </Card>

          {/* Warning */}
          <Card className="glass border-error/20">
            <CardHeader>
              <CardTitle className="text-error text-sm">⚠️ Warning</CardTitle>
            </CardHeader>
            <CardContent>
              <p className="text-xs text-text-secondary">
                This tool is for educational purposes only. Always get consent before use. 
                Misuse may result in legal consequences.
              </p>
            </CardContent>
          </Card>
        </div>
      </div>
    </div>
  )
}