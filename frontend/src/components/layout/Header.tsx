import { Bell, User, LogOut } from 'lucide-react'
import { Button } from '@/components/ui/button'
import { Badge } from '@/components/ui/badge'

export function Header() {
  return (
    <header className="h-16 border-b border-neon-blue/20 bg-dark-surface flex items-center justify-between px-6">
      <div className="flex items-center gap-4">
        <div>
          <h2 className="text-lg font-semibold text-text-primary">Welcome Back, Hacker</h2>
          <p className="text-sm text-text-secondary">Ready to dominate the SMS world?</p>
        </div>
      </div>

      <div className="flex items-center gap-4">
        {/* Status Badge */}
        <Badge variant="outline" className="border-neon-green text-neon-green">
          <span className="w-2 h-2 bg-neon-green rounded-full mr-2 animate-pulse" />
          System Online
        </Badge>

        {/* Notifications */}
        <Button variant="ghost" size="icon" className="relative hover:bg-dark-elevated">
          <Bell className="w-5 h-5 text-text-secondary" />
          <span className="absolute top-1 right-1 w-2 h-2 bg-neon-pink rounded-full" />
        </Button>

        {/* User Menu */}
        <div className="flex items-center gap-3 pl-4 border-l border-neon-blue/20">
          <Button variant="ghost" size="icon" className="hover:bg-dark-elevated">
            <User className="w-5 h-5 text-text-secondary" />
          </Button>
          <Button variant="ghost" size="icon" className="hover:bg-dark-elevated hover:text-neon-pink">
            <LogOut className="w-5 h-5 text-text-secondary" />
          </Button>
        </div>
      </div>
    </header>
  )
}