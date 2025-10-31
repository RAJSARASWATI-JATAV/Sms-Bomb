import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Label } from '@/components/ui/label'
import { Input } from '@/components/ui/input'
import { Button } from '@/components/ui/button'
import { Switch } from '@/components/ui/switch'
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select'
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs'
import { Settings as SettingsIcon, Shield, Bell, User, Save } from 'lucide-react'

export function Settings() {
  return (
    <div className="space-y-6">
      {/* Page Header */}
      <div>
        <h1 className="heading-lg text-neon-yellow">Settings</h1>
        <p className="text-text-secondary mt-1">Configure your SMS-PowerBomb preferences</p>
      </div>

      <Tabs defaultValue="general" className="space-y-6">
        <TabsList>
          <TabsTrigger value="general">General</TabsTrigger>
          <TabsTrigger value="security">Security</TabsTrigger>
          <TabsTrigger value="notifications">Notifications</TabsTrigger>
          <TabsTrigger value="profile">Profile</TabsTrigger>
        </TabsList>

        <TabsContent value="general">
          <Card className="glass border-neon-blue/20">
            <CardHeader>
              <CardTitle className="flex items-center gap-2 text-neon-blue">
                <SettingsIcon className="w-5 h-5" />
                General Settings
              </CardTitle>
              <CardDescription>Configure basic application settings</CardDescription>
            </CardHeader>
            <CardContent className="space-y-6">
              <div>
                <Label htmlFor="theme">Theme</Label>
                <Select defaultValue="dark">
                  <SelectTrigger id="theme" className="mt-2 bg-dark-elevated">
                    <SelectValue />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="dark">Dark (Cyberpunk)</SelectItem>
                    <SelectItem value="light">Light</SelectItem>
                    <SelectItem value="auto">Auto</SelectItem>
                  </SelectContent>
                </Select>
              </div>

              <div>
                <Label htmlFor="language">Language</Label>
                <Select defaultValue="en">
                  <SelectTrigger id="language" className="mt-2 bg-dark-elevated">
                    <SelectValue />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="en">English</SelectItem>
                    <SelectItem value="hi">Hindi</SelectItem>
                    <SelectItem value="es">Spanish</SelectItem>
                  </SelectContent>
                </Select>
              </div>

              <div className="flex items-center justify-between">
                <div>
                  <Label>Auto-save Campaigns</Label>
                  <p className="text-xs text-text-muted mt-1">
                    Automatically save campaign drafts
                  </p>
                </div>
                <Switch defaultChecked />
              </div>

              <div className="flex items-center justify-between">
                <div>
                  <Label>Show Advanced Options</Label>
                  <p className="text-xs text-text-muted mt-1">
                    Display advanced configuration options
                  </p>
                </div>
                <Switch defaultChecked />
              </div>

              <Button className="bg-gradient-to-r from-neon-blue to-neon-purple hover:opacity-90">
                <Save className="w-4 h-4 mr-2" />
                Save Changes
              </Button>
            </CardContent>
          </Card>
        </TabsContent>

        <TabsContent value="security">
          <Card className="glass border-neon-blue/20">
            <CardHeader>
              <CardTitle className="flex items-center gap-2 text-neon-green">
                <Shield className="w-5 h-5" />
                Security Settings
              </CardTitle>
              <CardDescription>Manage your security preferences</CardDescription>
            </CardHeader>
            <CardContent className="space-y-6">
              <div className="flex items-center justify-between">
                <div>
                  <Label>Two-Factor Authentication</Label>
                  <p className="text-xs text-text-muted mt-1">
                    Add an extra layer of security
                  </p>
                </div>
                <Switch />
              </div>

              <div className="flex items-center justify-between">
                <div>
                  <Label>Enable Proxy Rotation</Label>
                  <p className="text-xs text-text-muted mt-1">
                    Automatically rotate proxies for stealth
                  </p>
                </div>
                <Switch defaultChecked />
              </div>

              <div className="flex items-center justify-between">
                <div>
                  <Label>VPN Integration</Label>
                  <p className="text-xs text-text-muted mt-1">
                    Connect through VPN for anonymity
                  </p>
                </div>
                <Switch defaultChecked />
              </div>

              <div className="flex items-center justify-between">
                <div>
                  <Label>Tor Network</Label>
                  <p className="text-xs text-text-muted mt-1">
                    Route traffic through Tor
                  </p>
                </div>
                <Switch />
              </div>

              <div>
                <Label htmlFor="encryption">Encryption Level</Label>
                <Select defaultValue="aes256">
                  <SelectTrigger id="encryption" className="mt-2 bg-dark-elevated">
                    <SelectValue />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="aes128">AES-128</SelectItem>
                    <SelectItem value="aes256">AES-256 (Recommended)</SelectItem>
                    <SelectItem value="rsa">RSA-2048</SelectItem>
                  </SelectContent>
                </Select>
              </div>

              <Button className="bg-gradient-to-r from-neon-green to-neon-blue hover:opacity-90">
                <Save className="w-4 h-4 mr-2" />
                Save Security Settings
              </Button>
            </CardContent>
          </Card>
        </TabsContent>

        <TabsContent value="notifications">
          <Card className="glass border-neon-blue/20">
            <CardHeader>
              <CardTitle className="flex items-center gap-2 text-neon-orange">
                <Bell className="w-5 h-5" />
                Notification Settings
              </CardTitle>
              <CardDescription>Manage how you receive notifications</CardDescription>
            </CardHeader>
            <CardContent className="space-y-6">
              <div className="flex items-center justify-between">
                <div>
                  <Label>Campaign Completion</Label>
                  <p className="text-xs text-text-muted mt-1">
                    Notify when campaigns finish
                  </p>
                </div>
                <Switch defaultChecked />
              </div>

              <div className="flex items-center justify-between">
                <div>
                  <Label>API Failures</Label>
                  <p className="text-xs text-text-muted mt-1">
                    Alert on API failures
                  </p>
                </div>
                <Switch defaultChecked />
              </div>

              <div className="flex items-center justify-between">
                <div>
                  <Label>Success Milestones</Label>
                  <p className="text-xs text-text-muted mt-1">
                    Notify on success milestones
                  </p>
                </div>
                <Switch defaultChecked />
              </div>

              <div className="flex items-center justify-between">
                <div>
                  <Label>Email Notifications</Label>
                  <p className="text-xs text-text-muted mt-1">
                    Receive updates via email
                  </p>
                </div>
                <Switch />
              </div>

              <div className="flex items-center justify-between">
                <div>
                  <Label>Telegram Notifications</Label>
                  <p className="text-xs text-text-muted mt-1">
                    Get updates on Telegram
                  </p>
                </div>
                <Switch defaultChecked />
              </div>

              <Button className="bg-gradient-to-r from-neon-orange to-neon-pink hover:opacity-90">
                <Save className="w-4 h-4 mr-2" />
                Save Notification Settings
              </Button>
            </CardContent>
          </Card>
        </TabsContent>

        <TabsContent value="profile">
          <Card className="glass border-neon-blue/20">
            <CardHeader>
              <CardTitle className="flex items-center gap-2 text-neon-pink">
                <User className="w-5 h-5" />
                Profile Settings
              </CardTitle>
              <CardDescription>Manage your account information</CardDescription>
            </CardHeader>
            <CardContent className="space-y-6">
              <div>
                <Label htmlFor="username">Username</Label>
                <Input
                  id="username"
                  defaultValue="hacker_elite"
                  className="mt-2 bg-dark-elevated border-neon-blue/30"
                />
              </div>

              <div>
                <Label htmlFor="email">Email</Label>
                <Input
                  id="email"
                  type="email"
                  defaultValue="hacker@smspowerbomb.com"
                  className="mt-2 bg-dark-elevated border-neon-blue/30"
                />
              </div>

              <div>
                <Label htmlFor="telegram">Telegram Username</Label>
                <Input
                  id="telegram"
                  defaultValue="@hacker_elite"
                  className="mt-2 bg-dark-elevated border-neon-blue/30"
                />
              </div>

              <div>
                <Label htmlFor="current-password">Current Password</Label>
                <Input
                  id="current-password"
                  type="password"
                  className="mt-2 bg-dark-elevated border-neon-blue/30"
                />
              </div>

              <div>
                <Label htmlFor="new-password">New Password</Label>
                <Input
                  id="new-password"
                  type="password"
                  className="mt-2 bg-dark-elevated border-neon-blue/30"
                />
              </div>

              <Button className="bg-gradient-to-r from-neon-pink to-neon-purple hover:opacity-90">
                <Save className="w-4 h-4 mr-2" />
                Update Profile
              </Button>
            </CardContent>
          </Card>
        </TabsContent>
      </Tabs>
    </div>
  )
}