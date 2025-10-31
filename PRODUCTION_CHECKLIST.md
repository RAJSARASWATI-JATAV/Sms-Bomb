# 🚀 SMS-POWERBOMB Production Deployment Checklist

## ✅ Pre-Deployment Checklist

### 1. Security Configuration

#### Environment Variables
- [ ] Change `SECRET_KEY` to a strong random string (min 32 characters)
- [ ] Set `DEBUG=False`
- [ ] Set `ENVIRONMENT=production`
- [ ] Update `CORS_ORIGINS` with production domains only
- [ ] Set strong database password
- [ ] Configure Redis password (if using)

#### Generate Secure Keys
```python
import secrets
print("SECRET_KEY:", secrets.token_urlsafe(32))
print("DB_PASSWORD:", secrets.token_urlsafe(24))
print("REDIS_PASSWORD:", secrets.token_urlsafe(16))
```

---

### 2. Database Configuration

#### Switch to PostgreSQL
- [ ] Install PostgreSQL
- [ ] Create production database
- [ ] Update `DATABASE_URL` in .env
- [ ] Run migrations
- [ ] Test database connection

**PostgreSQL Setup:**
```sql
CREATE DATABASE smsbomb;
CREATE USER smsbomb WITH PASSWORD 'your-secure-password';
GRANT ALL PRIVILEGES ON DATABASE smsbomb TO smsbomb;
```

**Update .env:**
```env
DATABASE_URL=postgresql+asyncpg://smsbomb:password@localhost:5432/smsbomb
```

---

### 3. CORS Configuration

#### Update Allowed Origins
```env
# Development (REMOVE IN PRODUCTION)
# CORS_ORIGINS=http://localhost:5173,http://localhost:3000

# Production (USE THIS)
CORS_ORIGINS=https://yourdomain.com,https://www.yourdomain.com,https://api.yourdomain.com
```

---

### 4. SSL/HTTPS Setup

#### Option 1: Let's Encrypt (Recommended)
```bash
# Install Certbot
sudo apt-get install certbot python3-certbot-nginx

# Get certificate
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

#### Option 2: Cloudflare
- [ ] Add domain to Cloudflare
- [ ] Enable SSL/TLS encryption
- [ ] Set SSL mode to "Full (strict)"
- [ ] Enable "Always Use HTTPS"

---

### 5. Rate Limiting

#### Configure Limits
```env
RATE_LIMIT_PER_MINUTE=60
RATE_LIMIT_PER_HOUR=1000
```

#### Add IP-based Rate Limiting
Consider using Nginx rate limiting:
```nginx
limit_req_zone $binary_remote_addr zone=api:10m rate=10r/s;

location /api {
    limit_req zone=api burst=20 nodelay;
    proxy_pass http://backend:8000;
}
```

---

### 6. Logging Configuration

#### Set Up Log Rotation
```env
LOG_LEVEL=INFO
LOG_FILE=/var/log/smsbomb/app.log
```

#### Configure logrotate
```bash
# /etc/logrotate.d/smsbomb
/var/log/smsbomb/*.log {
    daily
    rotate 14
    compress
    delaycompress
    notifempty
    create 0640 www-data www-data
    sharedscripts
}
```

---

### 7. Monitoring Setup

#### Health Checks
- [ ] Set up uptime monitoring (UptimeRobot, Pingdom)
- [ ] Configure health check endpoint
- [ ] Set up alerts for downtime

#### Application Monitoring
- [ ] Install Sentry for error tracking
- [ ] Set up Prometheus metrics (optional)
- [ ] Configure Grafana dashboards (optional)

**Sentry Setup:**
```env
SENTRY_DSN=https://your-sentry-dsn@sentry.io/project-id
```

---

### 8. Backup Strategy

#### Database Backups
```bash
# Daily backup script
#!/bin/bash
DATE=$(date +%Y%m%d)
pg_dump -U smsbomb smsbomb > /backups/smsbomb-$DATE.sql
find /backups -name "smsbomb-*.sql" -mtime +7 -delete
```

#### Automated Backups
- [ ] Set up daily database backups
- [ ] Configure backup retention (7-30 days)
- [ ] Test backup restoration
- [ ] Store backups off-site (S3, Backblaze)

---

### 9. Performance Optimization

#### Backend
- [ ] Enable Redis caching
- [ ] Configure connection pooling
- [ ] Set up CDN for static files
- [ ] Enable gzip compression

#### Frontend
- [ ] Minify and compress assets
- [ ] Enable browser caching
- [ ] Use CDN for static assets
- [ ] Optimize images

#### Nginx Configuration
```nginx
# Enable gzip
gzip on;
gzip_types text/plain text/css application/json application/javascript;

# Browser caching
location ~* \.(jpg|jpeg|png|gif|ico|css|js)$ {
    expires 1y;
    add_header Cache-Control "public, immutable";
}
```

---

### 10. Security Hardening

#### Firewall Rules
```bash
# Allow only necessary ports
sudo ufw allow 22/tcp   # SSH
sudo ufw allow 80/tcp   # HTTP
sudo ufw allow 443/tcp  # HTTPS
sudo ufw enable
```

#### Fail2Ban
```bash
# Install fail2ban
sudo apt-get install fail2ban

# Configure for nginx
sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
```

#### Security Headers
```nginx
add_header X-Frame-Options "SAMEORIGIN" always;
add_header X-Content-Type-Options "nosniff" always;
add_header X-XSS-Protection "1; mode=block" always;
add_header Referrer-Policy "no-referrer-when-downgrade" always;
add_header Content-Security-Policy "default-src 'self' http: https: data: blob: 'unsafe-inline'" always;
```

---

### 11. Docker Production Setup

#### Docker Compose Production
```yaml
version: '3.8'

services:
  backend:
    restart: always
    deploy:
      resources:
        limits:
          cpus: '1.0'
          memory: 1G
        reservations:
          cpus: '0.5'
          memory: 512M
```

#### Health Checks
- [ ] Configure container health checks
- [ ] Set up automatic restart policies
- [ ] Monitor container resource usage

---

### 12. Testing

#### Pre-Deployment Tests
- [ ] Run all unit tests
- [ ] Run integration tests
- [ ] Test API endpoints
- [ ] Test WebSocket connections
- [ ] Load testing (Apache Bench, k6)
- [ ] Security scan (OWASP ZAP)

#### Load Testing Example
```bash
# Apache Bench
ab -n 1000 -c 10 http://yourdomain.com/api/v1/health

# k6
k6 run --vus 10 --duration 30s load-test.js
```

---

### 13. DNS Configuration

#### DNS Records
- [ ] A record: `yourdomain.com` → Server IP
- [ ] A record: `www.yourdomain.com` → Server IP
- [ ] A record: `api.yourdomain.com` → Server IP
- [ ] CNAME: `www` → `yourdomain.com`

#### Verify DNS
```bash
dig yourdomain.com
nslookup yourdomain.com
```

---

### 14. Deployment Process

#### Step-by-Step Deployment

1. **Backup Current System**
   ```bash
   # Backup database
   pg_dump -U smsbomb smsbomb > backup-pre-deploy.sql
   
   # Backup code
   tar -czf code-backup.tar.gz /var/www/smsbomb
   ```

2. **Pull Latest Code**
   ```bash
   git pull origin main
   ```

3. **Update Dependencies**
   ```bash
   # Backend
   cd backend
   pip install -r requirements.txt
   
   # Frontend
   cd frontend
   npm install
   npm run build
   ```

4. **Run Migrations**
   ```bash
   cd backend
   alembic upgrade head
   ```

5. **Restart Services**
   ```bash
   # Docker
   docker-compose down
   docker-compose up -d
   
   # Or systemd
   sudo systemctl restart smsbomb-backend
   sudo systemctl restart smsbomb-frontend
   ```

6. **Verify Deployment**
   ```bash
   # Check health
   curl https://yourdomain.com/api/v1/health
   
   # Check logs
   docker-compose logs -f
   ```

---

### 15. Post-Deployment

#### Monitoring
- [ ] Check application logs
- [ ] Monitor error rates
- [ ] Check response times
- [ ] Verify all endpoints working
- [ ] Test user authentication
- [ ] Test WebSocket connections

#### Rollback Plan
```bash
# If deployment fails, rollback:
git checkout previous-commit
docker-compose down
docker-compose up -d

# Restore database if needed
psql -U smsbomb smsbomb < backup-pre-deploy.sql
```

---

## 📊 Production Metrics to Monitor

### Application Metrics
- [ ] Request rate (requests/second)
- [ ] Response time (average, p95, p99)
- [ ] Error rate (4xx, 5xx)
- [ ] Active connections
- [ ] Database query time

### System Metrics
- [ ] CPU usage
- [ ] Memory usage
- [ ] Disk usage
- [ ] Network I/O
- [ ] Database connections

### Business Metrics
- [ ] Active users
- [ ] API calls per user
- [ ] Campaign success rate
- [ ] System uptime

---

## 🚨 Incident Response Plan

### Critical Issues
1. **Service Down**
   - Check logs: `docker-compose logs -f`
   - Restart services: `docker-compose restart`
   - Check health: `curl /health`

2. **Database Issues**
   - Check connections
   - Verify credentials
   - Check disk space
   - Restore from backup if needed

3. **High Load**
   - Scale horizontally
   - Enable caching
   - Optimize queries
   - Add rate limiting

---

## ✅ Final Checklist

Before going live:
- [ ] All security configurations applied
- [ ] SSL/HTTPS enabled
- [ ] Database switched to PostgreSQL
- [ ] Backups configured and tested
- [ ] Monitoring and alerts set up
- [ ] Load testing completed
- [ ] Security scan passed
- [ ] Documentation updated
- [ ] Team trained on deployment process
- [ ] Rollback plan documented
- [ ] Emergency contacts listed
- [ ] Incident response plan ready

---

## 📞 Emergency Contacts

**Technical Lead:** [Name] - [Phone] - [Email]  
**DevOps:** [Name] - [Phone] - [Email]  
**On-Call:** [Rotation Schedule]

---

## 📚 Additional Resources

- [Docker Documentation](https://docs.docker.com/)
- [FastAPI Deployment](https://fastapi.tiangolo.com/deployment/)
- [PostgreSQL Best Practices](https://wiki.postgresql.org/wiki/Don%27t_Do_This)
- [Nginx Configuration](https://nginx.org/en/docs/)
- [Let's Encrypt](https://letsencrypt.org/)

---

**Creator:** RAJSARASWATI JATAV  
**Version:** 10.0.0  
**Last Updated:** 2024