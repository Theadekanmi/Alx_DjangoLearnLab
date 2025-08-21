#!/bin/bash

# Production Deployment Script for Django Social Media API

echo "🚀 Starting production deployment..."

# Check if .env file exists
if [ ! -f .env ]; then
    echo "❌ .env file not found. Please create one from .env.example"
    exit 1
fi

# Load environment variables
source .env

# Install/upgrade dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Run database migrations
echo "🗄️ Running database migrations..."
python manage.py migrate

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

# Create superuser if needed (uncomment if needed)
# echo "👤 Creating superuser..."
# python manage.py createsuperuser

# Check if running in production
if [ "$DEBUG" = "False" ]; then
    echo "🔒 Production mode detected. Starting with gunicorn..."
    
    # Start gunicorn
    gunicorn social_media_api.wsgi:application \
        --bind 0.0.0.0:8000 \
        --workers 3 \
        --timeout 120 \
        --access-logfile - \
        --error-logfile -
else
    echo "🛠️ Development mode. Starting with Django development server..."
    python manage.py runserver 0.0.0.0:8000
fi