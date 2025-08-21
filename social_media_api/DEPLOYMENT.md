# Production Deployment Guide

This guide covers deploying the Django Social Media API to production with proper security, database configuration, and file handling.

## Prerequisites

- Python 3.8+
- PostgreSQL database
- Redis (optional, for caching)
- AWS S3 account (optional, for file storage)

## Environment Configuration

### 1. Create Environment File

Copy the example environment file and configure it:

```bash
cp .env.example .env
```

Edit `.env` with your production values:

```env
# Django Settings
SECRET_KEY=your-very-secure-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# Database Configuration
DATABASE_URL=postgres://username:password@host:port/database_name

# AWS S3 Configuration (optional)
USE_S3=False
AWS_ACCESS_KEY_ID=your-aws-access-key
AWS_SECRET_ACCESS_KEY=your-aws-secret-key
AWS_STORAGE_BUCKET_NAME=your-bucket-name

# Security Settings
SECURE_SSL_REDIRECT=True
```

### 2. Generate Secure Secret Key

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## Database Setup

### PostgreSQL Configuration

1. Install PostgreSQL
2. Create database and user:

```sql
CREATE DATABASE social_media_db;
CREATE USER social_media_user WITH PASSWORD 'secure_password';
GRANT ALL PRIVILEGES ON DATABASE social_media_db TO social_media_user;
```

3. Update your `.env` file with the database URL:

```env
DATABASE_URL=postgres://social_media_user:secure_password@localhost:5432/social_media_db
```

## File Storage Configuration

### Option 1: Local Storage (Default)

Files will be stored locally in the `media/` directory. Ensure the directory is writable:

```bash
mkdir -p media/
chmod 755 media/
```

### Option 2: AWS S3 Storage

1. Create an S3 bucket
2. Configure CORS for your bucket
3. Set environment variables:

```env
USE_S3=True
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
AWS_STORAGE_BUCKET_NAME=your-bucket-name
```

## Security Configuration

The application automatically configures security settings when `DEBUG=False`:

- `SECURE_BROWSER_XSS_FILTER = True`
- `X_FRAME_OPTIONS = 'DENY'`
- `SECURE_CONTENT_TYPE_NOSNIFF = True`
- `SECURE_SSL_REDIRECT = True`
- `SECURE_HSTS_SECONDS = 31536000`
- `SESSION_COOKIE_SECURE = True`
- `CSRF_COOKIE_SECURE = True`

## Installation and Deployment

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Migrations

```bash
python manage.py migrate
```

### 3. Create Superuser

```bash
python manage.py createsuperuser
```

### 4. Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### 5. Deploy

Use the provided deployment script:

```bash
./deploy.sh
```

Or manually start with gunicorn:

```bash
gunicorn social_media_api.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --timeout 120 \
    --access-logfile - \
    --error-logfile -
```

## Web Server Configuration

### Nginx Configuration Example

```nginx
server {
    listen 80;
    server_name yourdomain.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name yourdomain.com;
    
    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;
    
    location /static/ {
        alias /path/to/your/project/staticfiles/;
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
    
    location /media/ {
        alias /path/to/your/project/media/;
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
    
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

## Monitoring and Maintenance

### Health Check Endpoint

The API includes a health check endpoint at `/api/health/` (if implemented).

### Log Management

Configure logging in your web server and application:

```python
# Add to settings.py for production logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django/social_media_api.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
```

### Backup Strategy

1. Database backups:
```bash
pg_dump social_media_db > backup_$(date +%Y%m%d_%H%M%S).sql
```

2. Media files backup:
```bash
tar -czf media_backup_$(date +%Y%m%d_%H%M%S).tar.gz media/
```

## Troubleshooting

### Common Issues

1. **Static files not loading**: Ensure `collectstatic` was run and web server is configured correctly
2. **Database connection errors**: Check database credentials and network connectivity
3. **Permission denied**: Ensure proper file permissions on media and static directories
4. **SSL errors**: Verify SSL certificate paths and permissions

### Debug Mode

For troubleshooting, temporarily enable debug mode in `.env`:

```env
DEBUG=True
```

**Remember to disable debug mode in production!**

## Performance Optimization

1. **Database indexing**: Ensure proper database indexes on frequently queried fields
2. **Caching**: Implement Redis caching for frequently accessed data
3. **CDN**: Use a CDN for static and media files
4. **Database connection pooling**: Configure connection pooling for production databases

## Security Checklist

- [ ] `DEBUG = False`
- [ ] Strong `SECRET_KEY`
- [ ] HTTPS enabled
- [ ] Database credentials secured
- [ ] File upload restrictions
- [ ] Rate limiting implemented
- [ ] Security headers configured
- [ ] Regular security updates
- [ ] Backup strategy in place
- [ ] Monitoring and alerting configured
