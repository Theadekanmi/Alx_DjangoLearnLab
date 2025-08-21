# Deployment Guide for Social Media API

This guide covers deploying the Social Media API to various production environments.

## Prerequisites

- Python 3.8+ installed on your server
- PostgreSQL database
- Redis (optional, for caching)
- Domain name (for production)
- SSL certificate (for HTTPS)

## Option 1: Heroku Deployment

### 1. Install Heroku CLI
```bash
# macOS
brew install heroku/brew/heroku

# Ubuntu/Debian
curl https://cli-assets.heroku.com/install-ubuntu.sh | sh

# Windows
# Download from https://devcenter.heroku.com/articles/heroku-cli
```

### 2. Login to Heroku
```bash
heroku login
```

### 3. Create Heroku App
```bash
heroku create your-app-name
```

### 4. Add PostgreSQL Add-on
```bash
heroku addons:create heroku-postgresql:mini
```

### 5. Set Environment Variables
```bash
heroku config:set SECRET_KEY="your-secret-key-here"
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS="your-app-name.herokuapp.com"
```

### 6. Deploy
```bash
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

### 7. Run Migrations
```bash
heroku run python manage.py migrate
```

### 8. Create Superuser
```bash
heroku run python manage.py createsuperuser
```

## Option 2: DigitalOcean VPS Deployment

### 1. Server Setup
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install required packages
sudo apt install -y python3 python3-pip python3-venv nginx postgresql postgresql-contrib redis-server
```

### 2. Create Application User
```bash
sudo adduser --system --group --no-create-home socialmedia
```

### 3. Setup PostgreSQL
```bash
sudo -u postgres psql
CREATE DATABASE social_media_db;
CREATE USER socialmedia_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE social_media_db TO socialmedia_user;
\q
```

### 4. Clone and Setup Application
```bash
cd /opt
sudo git clone https://github.com/yourusername/social_media_api.git
sudo chown -R socialmedia:socialmedia social_media_api
cd social_media_api

# Create virtual environment
sudo -u socialmedia python3 -m venv venv
sudo -u socialmedia venv/bin/pip install -r requirements.txt
```

### 5. Environment Configuration
```bash
sudo -u socialmedia cp .env.example .env
sudo -u socialmedia nano .env
# Edit the .env file with your production values
```

### 6. Django Setup
```bash
sudo -u socialmedia venv/bin/python manage.py collectstatic --noinput
sudo -u socialmedia venv/bin/python manage.py migrate
sudo -u socialmedia venv/bin/python manage.py createsuperuser
```

### 7. Gunicorn Configuration
Create `/etc/systemd/system/socialmedia.service`:
```ini
[Unit]
Description=Social Media API Gunicorn daemon
After=network.target

[Service]
User=socialmedia
Group=socialmedia
WorkingDirectory=/opt/social_media_api
Environment="PATH=/opt/social_media_api/venv/bin"
ExecStart=/opt/social_media_api/venv/bin/gunicorn --workers 3 --bind unix:/opt/social_media_api/social_media_api.sock social_media_api.wsgi:application

[Install]
WantedBy=multi-user.target
```

### 8. Nginx Configuration
Create `/etc/nginx/sites-available/socialmedia`:
```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        root /opt/social_media_api;
    }

    location /media/ {
        root /opt/social_media_api;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/opt/social_media_api/social_media_api.sock;
    }
}
```

### 9. Enable Services
```bash
sudo systemctl start socialmedia
sudo systemctl enable socialmedia
sudo ln -s /etc/nginx/sites-available/socialmedia /etc/nginx/sites-enabled
sudo systemctl restart nginx
```

## Option 3: AWS Deployment

### 1. Launch EC2 Instance
- Choose Ubuntu Server 20.04 LTS
- Select appropriate instance type (t3.micro for testing)
- Configure security groups (allow HTTP, HTTPS, SSH)

### 2. Connect to Instance
```bash
ssh -i your-key.pem ubuntu@your-instance-ip
```

### 3. Follow DigitalOcean VPS steps from step 1

### 4. Configure Security Groups
- Allow HTTP (port 80)
- Allow HTTPS (port 443)
- Allow SSH (port 22)

## SSL/HTTPS Setup

### Using Let's Encrypt (Certbot)
```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

### Auto-renewal
```bash
sudo crontab -e
# Add this line:
0 12 * * * /usr/bin/certbot renew --quiet
```

## Monitoring and Maintenance

### 1. Log Monitoring
```bash
# View application logs
sudo journalctl -u socialmedia -f

# View Nginx logs
sudo tail -f /var/log/nginx/access.log
sudo tail -f /var/log/nginx/error.log
```

### 2. Database Backups
```bash
# Create backup script
sudo nano /opt/backup_db.sh
```

```bash
#!/bin/bash
BACKUP_DIR="/opt/backups"
DATE=$(date +%Y%m%d_%H%M%S)
DB_NAME="social_media_db"
DB_USER="socialmedia_user"

mkdir -p $BACKUP_DIR
pg_dump -U $DB_USER $DB_NAME > $BACKUP_DIR/backup_$DATE.sql

# Keep only last 7 backups
find $BACKUP_DIR -name "backup_*.sql" -mtime +7 -delete
```

### 3. Application Updates
```bash
cd /opt/social_media_api
sudo git pull origin main
sudo -u socialmedia venv/bin/pip install -r requirements.txt
sudo -u socialmedia venv/bin/python manage.py migrate
sudo -u socialmedia venv/bin/python manage.py collectstatic --noinput
sudo systemctl restart socialmedia
```

## Performance Optimization

### 1. Database Optimization
```sql
-- Add indexes for better performance
CREATE INDEX idx_post_author ON posts(author_id);
CREATE INDEX idx_post_created ON posts(created_at);
CREATE INDEX idx_comment_post ON comments(post_id);
CREATE INDEX idx_like_post ON likes(post_id);
```

### 2. Caching
- Use Redis for caching frequently accessed data
- Implement Django cache framework
- Use CDN for static files

### 3. Load Balancing
- Use multiple application servers
- Implement health checks
- Use AWS ELB or Nginx load balancer

## Troubleshooting

### Common Issues

1. **500 Internal Server Error**
   - Check application logs
   - Verify database connection
   - Check file permissions

2. **Database Connection Issues**
   - Verify PostgreSQL is running
   - Check connection credentials
   - Ensure firewall allows connections

3. **Static Files Not Loading**
   - Run `collectstatic`
   - Check Nginx configuration
   - Verify file permissions

### Useful Commands
```bash
# Check service status
sudo systemctl status socialmedia

# Restart services
sudo systemctl restart socialmedia
sudo systemctl restart nginx

# Check logs
sudo journalctl -u socialmedia -n 50
sudo tail -f /var/log/nginx/error.log

# Database connection test
sudo -u postgres psql -d social_media_db -c "SELECT version();"
```

## Security Checklist

- [ ] DEBUG = False in production
- [ ] Strong SECRET_KEY
- [ ] HTTPS enabled
- [ ] Database credentials secured
- [ ] Firewall configured
- [ ] Regular security updates
- [ ] Database backups enabled
- [ ] Log monitoring active
- [ ] SSL certificate valid
- [ ] Environment variables secured

## Support

For deployment issues:
1. Check the logs
2. Verify configuration files
3. Test database connectivity
4. Check service status
5. Review security group/firewall settings