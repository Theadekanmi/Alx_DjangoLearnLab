# HTTPS Deployment Configuration Guide

## Overview
This document provides instructions for configuring HTTPS in various deployment environments for the LibraryProject Django application.

## 1. Nginx Configuration

### Basic Nginx SSL Configuration
```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name yourdomain.com www.yourdomain.com;

    # SSL Certificate Configuration
    ssl_certificate /path/to/your/certificate.crt;
    ssl_certificate_key /path/to/your/private.key;

    # SSL Security Settings
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-RSA-AES256-GCM-SHA512:DHE-RSA-AES256-GCM-SHA512:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES256-GCM-SHA384;
    ssl_prefer_server_ciphers off;
    ssl_session_cache shared:SSL:10m;
    ssl_session_timeout 10m;

    # Security Headers
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;
    add_header X-Frame-Options "DENY" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-XSS-Protection "1; mode=block" always;
    add_header Referrer-Policy "strict-origin-when-cross-origin" always;

    # Django Application
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # Static files
    location /static/ {
        alias /path/to/your/static/files/;
        expires 1y;
        add_header Cache-Control "public, immutable";
    }

    # Media files
    location /media/ {
        alias /path/to/your/media/files/;
        expires 1y;
        add_header Cache-Control "public";
    }
}
```

## 2. Apache Configuration

### Apache SSL Virtual Host
```apache
<VirtualHost *:80>
    ServerName yourdomain.com
    ServerAlias www.yourdomain.com
    Redirect permanent / https://yourdomain.com/
</VirtualHost>

<VirtualHost *:443>
    ServerName yourdomain.com
    ServerAlias www.yourdomain.com

    # SSL Configuration
    SSLEngine on
    SSLCertificateFile /path/to/your/certificate.crt
    SSLCertificateKeyFile /path/to/your/private.key
    SSLCertificateChainFile /path/to/your/chain.crt

    # SSL Security
    SSLProtocol all -SSLv3 -TLSv1 -TLSv1.1
    SSLCipherSuite ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384
    SSLHonorCipherOrder On
    
    # Security Headers
    Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains; preload"
    Header always set X-Frame-Options "DENY"
    Header always set X-Content-Type-Options "nosniff"
    Header always set X-XSS-Protection "1; mode=block"
    Header always set Referrer-Policy "strict-origin-when-cross-origin"

    # Django WSGI
    WSGIDaemonProcess libraryproject python-path=/path/to/LibraryProject
    WSGIProcessGroup libraryproject
    WSGIScriptAlias / /path/to/LibraryProject/LibraryProject/wsgi.py

    <Directory /path/to/LibraryProject/LibraryProject>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>

    # Static files
    Alias /static /path/to/LibraryProject/static
    <Directory /path/to/LibraryProject/static>
        Require all granted
    </Directory>

    # Media files
    Alias /media /path/to/LibraryProject/media
    <Directory /path/to/LibraryProject/media>
        Require all granted
    </Directory>
</VirtualHost>
```

## 3. SSL Certificate Setup

### Option 1: Let's Encrypt (Recommended for production)
```bash
# Install Certbot
sudo apt-get update
sudo apt-get install certbot python3-certbot-nginx

# Obtain SSL certificate
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com

# Auto-renewal setup
sudo crontab -e
# Add: 0 12 * * * /usr/bin/certbot renew --quiet
```

### Option 2: Self-Signed Certificate (Development only)
```bash
# Generate self-signed certificate
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
```

## 4. Django Production Settings

### Environment-Specific Settings
Create a `production_settings.py`:
```python
from .settings import *

# Production-specific overrides
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# Database configuration for production
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'libraryproject_prod',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Static and media files for production
STATIC_ROOT = '/var/www/LibraryProject/static/'
MEDIA_ROOT = '/var/www/LibraryProject/media/'

# Email configuration for error reporting
ADMINS = [('Admin', 'admin@yourdomain.com')]
EMAIL_HOST = 'smtp.yourdomain.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'noreply@yourdomain.com'
EMAIL_HOST_PASSWORD = 'your_email_password'
```

## 5. Security Testing

### Test HTTPS Configuration
```bash
# Test SSL configuration
curl -I https://yourdomain.com

# Check security headers
curl -I https://yourdomain.com | grep -i security

# Test SSL Labs rating
# Visit: https://www.ssllabs.com/ssltest/
```

### Security Header Verification
```python
# Test script to verify headers
import requests

def test_security_headers(url):
    response = requests.get(url)
    headers = response.headers
    
    security_headers = [
        'Strict-Transport-Security',
        'X-Frame-Options',
        'X-Content-Type-Options',
        'X-XSS-Protection',
        'Content-Security-Policy'
    ]
    
    for header in security_headers:
        if header in headers:
            print(f"✅ {header}: {headers[header]}")
        else:
            print(f"❌ {header}: Missing")

# Usage
test_security_headers('https://yourdomain.com')
```

## 6. Monitoring and Maintenance

### Log Monitoring
```bash
# Monitor security logs
tail -f /path/to/LibraryProject/security.log

# Monitor Nginx/Apache logs
tail -f /var/log/nginx/access.log
tail -f /var/log/nginx/error.log
```

### Certificate Renewal
```bash
# Check certificate expiry
openssl x509 -in /path/to/certificate.crt -text -noout | grep "Not After"

# Automated renewal with Let's Encrypt
sudo certbot renew --dry-run
```

## 7. Troubleshooting

### Common Issues
1. **Mixed Content Warnings**: Ensure all resources (CSS, JS, images) use HTTPS
2. **HSTS Issues**: Clear browser HSTS cache if needed
3. **Proxy Configuration**: Verify X-Forwarded-Proto headers are set correctly
4. **Certificate Chain**: Ensure intermediate certificates are properly configured

### Development vs Production
- Use `DEBUG = False` in production
- Disable HTTPS redirects in development if needed
- Use environment variables for sensitive settings
- Implement proper logging and monitoring
