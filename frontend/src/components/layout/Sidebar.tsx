import { NavLink } from 'react-router-dom'
import { 
  LayoutDashboard, 
  Target, 
  BarChart3, 
  Activity, 
  Settings,
  Zap
} from 'lucide-react'
import { cn } from '@/lib/utils'

const navigation = [
  { name: 'Dashboard', href: '/', icon: LayoutDashboard },
  { name: 'Campaign Builder', href: '/campaign', icon: Target },
  { name: 'Analytics', href: '/analytics', icon: BarChart3 },
  { name: 'API Status', href: '/api-status', icon: Activity },
  { name: 'Settings', href: '/settings', icon: Settings },
]

export function Sidebar() {
  return (
    <div className="w-64 bg-dark-surface border-r border-neon-blue/20 flex flex-col">
      {/* Logo */}
      <div className="p-6 border-b border-neon-blue/20">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-lg bg-gradient-to-br from-neon-green to-neon-blue flex items-center justify-center glow-green">
            <Zap className="w-6 h-6 text-dark" />
          </div>
          <div>
            <h1 className="text-xl font-bold text-neon-green">SMS-POWERBOMB</h1>
            <p className="text-xs text-text-secondary">v10.0 Ultimate</p>
          </div>
        </div>
      </div>

      {/* Navigation */}
      <nav className="flex-1 p-4 space-y-2">
        {navigation.map((item) => (
          <NavLink
            key={item.name}
            to={item.href}
            end={item.href === '/'}
            className={({ isActive }) =>
              cn(
                'flex items-center gap-3 px-4 py-3 rounded-lg transition-all duration-200',
                'hover:bg-dark-elevated hover:glow-blue',
                isActive
                  ? 'bg-dark-elevated text-neon-blue glow-blue'
                  : 'text-text-secondary hover:text-neon-blue'
              )
            }
          >
            <item.icon className="w-5 h-5" />
            <span className="font-medium">{item.name}</span>
          </NavLink>
        ))}
      </nav>

      {/* Footer */}
      <div className="p-4 border-t border-neon-blue/20">
        <div className="glass rounded-lg p-4">
          <p className="text-xs text-text-secondary mb-2">Created by</p>
          <p className="text-sm font-semibold text-neon-pink">RAJSARASWATI JATAV</p>
          <p className="text-xs text-text-muted mt-1">Cyber Crew</p>
        </div>
      </div>
    </div>
  )
}