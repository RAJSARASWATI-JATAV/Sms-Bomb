# 🚀 Quick Start Guide - Phase 4

## Prerequisites
- Python 3.9+
- PostgreSQL or SQLite
- Virtual environment activated

## Installation

### 1. Install Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### 2. Configure Environment
Create `.env` file:
```env
DATABASE_URL=sqlite+aiosqlite:///./smsbomb.db
SECRET_KEY=your-secret-key-change-in-production
DEBUG=True
```

### 3. Seed API Gateways
```bash
python seed_apis.py
```

Expected output:
```
🌱 Seeding API gateways...
✅ Added Twilio SMS API
✅ Added Nexmo SMS API
✅ Added MessageBird API
...
🎉 Seeding completed!
```

### 4. Start Backend Server
```bash
python main.py
```

Server starts at: **http://localhost:8000**

## Testing Campaign Execution

### Method 1: Via API (cURL)

```bash
# 1. Register user
curl -X POST http://localhost:8000/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "testpass123"
  }'

# 2. Login
curl -X POST http://localhost:8000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "testpass123"
  }'

# Save the access_token from response

# 3. Create campaign
curl -X POST http://localhost:8000/api/v1/campaigns \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test Campaign",
    "mode": "normal",
    "targets": ["+1234567890", "+0987654321"],
    "waves": 2,
    "delay_seconds": 3
  }'

# 4. Start campaign (use campaign_id from response)
curl -X POST http://localhost:8000/api/v1/campaigns/1/start \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"

# 5. Monitor progress
curl http://localhost:8000/api/v1/campaigns/1/status \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"

# 6. View logs
curl http://localhost:8000/api/v1/campaigns/1/logs \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Method 2: Via Frontend

1. Start frontend: `cd frontend && npm run dev`
2. Open: http://localhost:5173
3. Login with credentials
4. Go to "Campaign Builder"
5. Fill in details:
   - Name: "Test Campaign"
   - Mode: Normal
   - Targets: Add phone numbers
   - Waves: 2
   - Delay: 3 seconds
6. Click "Create Campaign"
7. Click "Start" on dashboard
8. Watch real-time progress!

## Monitoring

### Health Check
```bash
curl http://localhost:8000/api/v1/monitoring/health
```

### System Metrics
```bash
curl http://localhost:8000/api/v1/monitoring/metrics \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### API Health
```bash
curl http://localhost:8000/api/v1/monitoring/api-health \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Performance Stats
```bash
curl http://localhost:8000/api/v1/monitoring/performance?hours=24 \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## Real-time Monitoring

Watch campaign progress in real-time:
```bash
watch -n 1 'curl -s http://localhost:8000/api/v1/campaigns/1/status \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" | jq'
```

## Troubleshooting

### Issue: Campaign not starting
**Solution**: Check logs in terminal, ensure APIs are seeded

### Issue: All requests failing
**Solution**: Sample APIs are mock endpoints. For real testing, add your own API credentials

### Issue: Rate limit errors
**Solution**: Adjust rate limits in API gateway settings or config

### Issue: Database errors
**Solution**: Delete `smsbomb.db` and restart server to recreate

## API Documentation

Full API docs available at: **http://localhost:8000/docs**

## Next Steps

1. ✅ Test campaign execution
2. ✅ Monitor system metrics
3. ✅ Check API health
4. 🔜 Integrate real SMS APIs
5. 🔜 Add WebSocket for real-time updates
6. 🔜 Deploy to production

## Support

For issues or questions:
- Check logs in terminal
- Review API docs at /docs
- Check PHASE_4_COMPLETE.md for details

---

**Happy Testing! 🚀**