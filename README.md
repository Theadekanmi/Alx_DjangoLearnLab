# n8n Setup with HTTPS and Backup

This setup provides n8n with HTTPS access for webhooks and automatic backups.

## 🚀 Quick Start

### Option 1: Using ngrok (Recommended)
1. **Setup ngrok account:**
   ```bash
   ./setup-ngrok.sh
   ```
   Follow the prompts to create a free ngrok account and add your authtoken.

2. **Start n8n with HTTPS:**
   ```bash
   ./start-n8n.sh
   ```

### Option 2: Using localtunnel (No account needed)
```bash
./start-n8n-localtunnel.sh
```

## 📁 Files Created

- `docker-compose.yml` - n8n Docker configuration
- `start-n8n.sh` - Start n8n with ngrok tunnel
- `start-n8n-localtunnel.sh` - Start n8n with localtunnel
- `stop-n8n.sh` - Stop n8n and tunnel
- `backup-n8n.sh` - Backup n8n data and workflows
- `setup-ngrok.sh` - Setup ngrok account

## 🔧 Current Status

✅ **n8n running:** http://localhost:5678  
✅ **Docker installed and working**  
✅ **Backup system ready**  
✅ **HTTPS tunnel options available**

## 📊 Backup System

### Automatic Backup
```bash
# Run backup manually
./backup-n8n.sh

# Setup automatic backup (daily at 2 AM)
crontab -e
# Add this line:
0 2 * * * /workspace/backup-n8n.sh
```

### Backup Location
- **Data backups:** `~/n8n-backups/`
- **Workflow exports:** JSON files in backup directory
- **Keeps last 10 backups automatically**

## 🌐 HTTPS Access

### For Telegram Webhooks
1. Start n8n with tunnel: `./start-n8n.sh`
2. Copy the HTTPS URL shown
3. Use that URL in your Telegram bot webhook settings
4. Format: `https://your-tunnel-url.ngrok.io/webhook/your-workflow-id`

### URL Storage
- HTTPS URL is saved to: `/tmp/n8n-https-url.txt`
- Check with: `cat /tmp/n8n-https-url.txt`

## 🛠️ Troubleshooting

### n8n not starting
```bash
# Check logs
sudo docker logs n8n

# Restart n8n
sudo docker restart n8n
```

### Tunnel not working
```bash
# Check tunnel logs
cat /tmp/ngrok.log
# or
cat /tmp/localtunnel.log
```

### Backup issues
```bash
# Check backup script
./backup-n8n.sh

# Manual workflow export
curl -u "admin:your_password_here" \
     -X GET "http://localhost:5678/rest/workflows" \
     > workflows_backup.json
```

## 📝 Important Notes

1. **Laptop must be ON** for automations to run
2. **HTTPS URL changes** each time you restart the tunnel
3. **Backup regularly** to avoid losing work
4. **Use strong passwords** for n8n admin access

## 🔄 Daily Usage

1. **Start:** `./start-n8n.sh`
2. **Access:** Use the HTTPS URL for webhooks
3. **Stop:** `./stop-n8n.sh` (or Ctrl+C)
4. **Backup:** `./backup-n8n.sh` (or automatic)

## 🆘 Need 24/7 Access?

For 24/7 automation (when laptop is off), consider:
- **Fly.io** (free tier)
- **Railway.app** (free tier)
- **Render.com** (free tier)

But local setup is perfect for learning and development!