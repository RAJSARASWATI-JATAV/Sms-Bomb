import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { useAuth } from '@/contexts/AuthContext'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Button } from '@/components/ui/button'
import { Checkbox } from '@/components/ui/checkbox'
import { Alert, AlertDescription } from '@/components/ui/alert'
import { Zap, Shield, Lock, AlertCircle } from 'lucide-react'

export function Login() {
  const navigate = useNavigate()
  const { login } = useAuth()
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState('')
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault()
    setIsLoading(true)
    setError('')

    try {
      await login(username, password)
      navigate('/')
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Login failed. Please try again.')
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-dark flex items-center justify-center p-4 relative overflow-hidden">
      {/* Animated Background */}
      <div className="absolute inset-0 overflow-hidden">
        <div className="absolute w-96 h-96 bg-neon-blue/10 rounded-full blur-3xl -top-48 -left-48 animate-pulse" />
        <div className="absolute w-96 h-96 bg-neon-pink/10 rounded-full blur-3xl -bottom-48 -right-48 animate-pulse" />
      </div>

      <Card className="w-full max-w-md glass-strong border-neon-blue/30 glow-blue relative z-10">
        <CardHeader className="text-center space-y-4">
          <div className="flex justify-center">
            <div className="w-16 h-16 rounded-xl bg-gradient-to-br from-neon-green to-neon-blue flex items-center justify-center glow-green">
              <Zap className="w-8 h-8 text-dark" />
            </div>
          </div>
          <div>
            <CardTitle className="text-2xl font-bold text-neon-green">SMS-POWERBOMB</CardTitle>
            <p className="text-sm text-neon-blue mt-1">v10.0 Ultimate Edition</p>
          </div>
          <CardDescription className="text-text-secondary">
            Enter your credentials to access the dashboard
          </CardDescription>
        </CardHeader>
        <CardContent>
          <form onSubmit={handleLogin} className="space-y-4">
            {error && (
              <Alert variant="destructive" className="bg-error/10 border-error/30">
                <AlertCircle className="h-4 w-4" />
                <AlertDescription>{error}</AlertDescription>
              </Alert>
            )}

            <div>
              <Label htmlFor="username">Username</Label>
              <Input
                id="username"
                placeholder="Enter your username"
                className="mt-2 bg-dark-elevated border-neon-blue/30"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                required
              />
            </div>

            <div>
              <Label htmlFor="password">Password</Label>
              <Input
                id="password"
                type="password"
                placeholder="Enter your password"
                className="mt-2 bg-dark-elevated border-neon-blue/30"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
            </div>

            <div className="flex items-center justify-between">
              <div className="flex items-center space-x-2">
                <Checkbox id="remember" />
                <label
                  htmlFor="remember"
                  className="text-sm text-text-secondary cursor-pointer"
                >
                  Remember me
                </label>
              </div>
              <Button variant="link" className="text-neon-blue p-0 h-auto">
                Forgot password?
              </Button>
            </div>

            <Button
              type="submit"
              className="w-full bg-gradient-to-r from-neon-green to-neon-blue hover:opacity-90 text-dark font-semibold"
              disabled={isLoading}
            >
              {isLoading ? (
                <>
                  <div className="w-4 h-4 border-2 border-dark border-t-transparent rounded-full animate-spin mr-2" />
                  Logging in...
                </>
              ) : (
                <>
                  <Lock className="w-4 h-4 mr-2" />
                  Login
                </>
              )}
            </Button>
          </form>

          <div className="mt-6 space-y-4">
            <div className="relative">
              <div className="absolute inset-0 flex items-center">
                <div className="w-full border-t border-neon-blue/20" />
              </div>
              <div className="relative flex justify-center text-xs">
                <span className="bg-dark-surface px-2 text-text-muted">
                  Security Features
                </span>
              </div>
            </div>

            <div className="grid grid-cols-2 gap-4 text-center">
              <div className="p-3 rounded-lg bg-dark-elevated border border-neon-blue/20">
                <Shield className="w-5 h-5 text-neon-green mx-auto mb-1" />
                <p className="text-xs text-text-secondary">AES-256</p>
              </div>
              <div className="p-3 rounded-lg bg-dark-elevated border border-neon-blue/20">
                <Lock className="w-5 h-5 text-neon-blue mx-auto mb-1" />
                <p className="text-xs text-text-secondary">2FA Ready</p>
              </div>
            </div>
          </div>

          <div className="mt-6 text-center">
            <p className="text-xs text-text-muted">
              Created by{' '}
              <span className="text-neon-pink font-semibold">RAJSARASWATI JATAV</span>
            </p>
            <p className="text-xs text-text-muted mt-1">Cyber Crew</p>
          </div>
        </CardContent>
      </Card>
    </div>
  )
}