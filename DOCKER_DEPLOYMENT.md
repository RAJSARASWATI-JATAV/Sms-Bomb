# 🐳 SMS-POWERBOMB Docker Deployment Guide

## 📋 Prerequisites

### Required Software
- ✅ Docker Engine 20.10+
- ✅ Docker Compose 2.0+
- ✅ 2GB RAM minimum
- ✅ 5GB disk space

### Installation Links
- **Docker Desktop (Windows/Mac):** https://docs.docker.com/desktop/
- **Docker Engine (Linux):** https://docs.docker.com/engine/install/
- **Docker Compose:** https://docs.docker.com/compose/install/

---

## 🚀 Quick Start

### Option 1: Using Scripts (Recommended)

**Windows:**
```cmd
scripts\docker-start.bat
```

**Linux/Mac:**
```bash
chmod +x scripts/docker-start.sh
./scripts/docker-start.sh
```

### Option 2: Manual Commands

```bash
# Build images
docker-compose build

# Start services
docker-compose up -d

# Check status
docker-compose ps

# View logs
docker-compose logs -f
```

---

## 📦 Services

### Backend API
- **Port:** 8000
- **URL:** http://localhost:8000
- **Docs:** http://localhost:8000/docs
- **Health:** http://localhost:8000/health

### Frontend
- **Port:** 80
- **URL:** http://localhost

### Redis (Optional)
- **Port:** 6379
- **Used for:** Caching, rate limiting

---

## ⚙️ Configuration

### Environment Variables

Copy and edit the production environment file:

```bash
cp docker/.env.production .env
```

**Critical Settings to Change:**

```env
# Security - MUST CHANGE!
SECRET_KEY=your-super-secret-key-here-minimum-32-characters

# CORS - Update with your domains
CORS_ORIGINS=https://yourdomain.com,https://www.yourdomain.com

# Database (for production, use PostgreSQL)
DATABASE_URL=postgresql+asyncpg://user:password@postgres:5432/smsbomb
```

### Generate Secure Secret Key

**Python:**
```python
import secrets
print(secrets.token_urlsafe(32))
```

**OpenSSL:**
```bash
openssl rand -base64 32
```

---

## 🔧 Docker Commands

### Basic Operations

```bash
# Start services
docker-compose up -d

# Stop services
docker-compose stop

# Restart services
docker-compose restart

# Remove containers
docker-compose down

# Remove containers and volumes
docker-compose down -v
```

### Logs and Debugging

```bash
# View all logs
docker-compose logs -f

# View backend logs only
docker-compose logs -f backend

# View frontend logs only
docker-compose logs -f frontend

# Last 100 lines
docker-compose logs --tail=100
```

### Container Management

```bash
# List running containers
docker-compose ps

# Execute command in backend
docker-compose exec backend python -c "print('Hello')"

# Access backend shell
docker-compose exec backend /bin/bash

# Access frontend shell
docker-compose exec frontend /bin/sh
```

### Health Checks

```bash
# Check backend health
curl http://localhost:8000/health

# Check frontend
curl http://localhost/

# Check all container health
docker-compose ps
```

---

## 🗄️ Database Management

### SQLite (Development)

```bash
# Backup database
docker-compose exec backend cp /app/data/smsbomb.db /app/data/backup.db

# Access database
docker-compose exec backend sqlite3 /app/data/smsbomb.db
```

### PostgreSQL (Production)

Add PostgreSQL service to `docker-compose.yml`:

```yaml
services:
  postgres:
    image: postgres:15-alpine
    container_name: smsbomb-postgres
    environment:
      POSTGRES_USER: smsbomb
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_DB: smsbomb
    volumes:
      - postgres-data:/var/lib/postgresql/data
    networks:
      - smsbomb-network
    restart: unless-stopped

volumes:
  postgres-data:
    driver: local
```

Update backend environment:
```env
DATABASE_URL=postgresql+asyncpg://smsbomb:password@postgres:5432/smsbomb
```

---

## 🔒 Security Best Practices

### 1. Change Default Secrets
```env
SECRET_KEY=<generate-strong-random-key>
DB_PASSWORD=<strong-database-password>
REDIS_PASSWORD=<redis-password>
```

### 2. Enable HTTPS
Use a reverse proxy like Nginx or Traefik with SSL certificates.

### 3. Restrict CORS
```env
CORS_ORIGINS=https://yourdomain.com
```

### 4. Use Production Database
Switch from SQLite to PostgreSQL for production.

### 5. Enable Rate Limiting
```env
RATE_LIMIT_PER_MINUTE=60
RATE_LIMIT_PER_HOUR=1000
```

### 6. Set Debug to False
```env
DEBUG=False
ENVIRONMENT=production
```

---

## 📊 Monitoring

### Container Stats

```bash
# Real-time stats
docker stats

# Specific container
docker stats smsbomb-backend
```

### Health Checks

```bash
# Check all services
docker-compose ps

# Backend health
curl http://localhost:8000/health

# Frontend health
curl -I http://localhost/
```

### Logs Analysis

```bash
# Error logs only
docker-compose logs | grep ERROR

# Warning logs
docker-compose logs | grep WARN

# Last hour logs
docker-compose logs --since 1h
```

---

## 🔄 Updates and Maintenance

### Update Application

```bash
# Pull latest code
git pull

# Rebuild images
docker-compose build

# Restart with new images
docker-compose up -d

# Remove old images
docker image prune -f
```

### Backup

```bash
# Backup volumes
docker run --rm \
  -v smsbomb_backend-data:/data \
  -v $(pwd):/backup \
  alpine tar czf /backup/backend-data-backup.tar.gz -C /data .

# Backup database
docker-compose exec backend \
  cp /app/data/smsbomb.db /app/data/backup-$(date +%Y%m%d).db
```

### Restore

```bash
# Restore from backup
docker run --rm \
  -v smsbomb_backend-data:/data \
  -v $(pwd):/backup \
  alpine tar xzf /backup/backend-data-backup.tar.gz -C /data
```

---

## 🐛 Troubleshooting

### Container Won't Start

```bash
# Check logs
docker-compose logs backend

# Check if port is in use
netstat -ano | findstr :8000  # Windows
lsof -i :8000                 # Linux/Mac

# Remove and recreate
docker-compose down
docker-compose up -d
```

### Database Connection Issues

```bash
# Check database file permissions
docker-compose exec backend ls -la /app/data/

# Recreate database
docker-compose exec backend python -c "from database import init_db; import asyncio; asyncio.run(init_db())"
```

### Frontend Not Loading

```bash
# Check nginx logs
docker-compose logs frontend

# Rebuild frontend
docker-compose build frontend
docker-compose up -d frontend
```

### Out of Memory

```bash
# Check memory usage
docker stats

# Increase Docker memory limit in Docker Desktop settings
# Or add to docker-compose.yml:
services:
  backend:
    mem_limit: 1g
    mem_reservation: 512m
```

---

## 🌐 Production Deployment

### Using Nginx Reverse Proxy

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://localhost:80;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /api {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### Using Traefik

Add labels to `docker-compose.yml`:

```yaml
services:
  backend:
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.backend.rule=Host(`api.yourdomain.com`)"
      - "traefik.http.routers.backend.entrypoints=websecure"
      - "traefik.http.routers.backend.tls.certresolver=letsencrypt"
```

---

## 📈 Scaling

### Horizontal Scaling

```yaml
services:
  backend:
    deploy:
      replicas: 3
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
```

### Load Balancing

Use Docker Swarm or Kubernetes for production load balancing.

---

## 📞 Support

**Issues?** Check:
1. Docker logs: `docker-compose logs -f`
2. Container status: `docker-compose ps`
3. Health checks: `curl http://localhost:8000/health`

**Creator:** RAJSARASWATI JATAV  
**GitHub:** https://github.com/RAJSARASWATI-JATAV

---

**Version:** 10.0.0  
**Last Updated:** 2024