#!/bin/bash

# n8n Startup Script with localtunnel
# This script starts n8n and creates an HTTPS tunnel using localtunnel

echo "Starting n8n with HTTPS tunnel (localtunnel)..."

# Check if n8n container is running
if ! sudo docker ps | grep -q n8n; then
    echo "Starting n8n container..."
    sudo docker run -d --name n8n -p 5678:5678 -v ~/n8n-data:/home/node/.n8n n8nio/n8n:latest
    echo "Waiting for n8n to start..."
    sleep 30
else
    echo "n8n container is already running"
fi

# Wait for n8n to be ready
echo "Checking if n8n is ready..."
until curl -s http://localhost:5678/healthz > /dev/null 2>&1; do
    echo "Waiting for n8n to be ready..."
    sleep 5
done

echo "n8n is ready! Starting localtunnel..."

# Start localtunnel in background
lt --port 5678 --subdomain n8n-yourname > /tmp/localtunnel.log 2>&1 &
LT_PID=$!

echo "localtunnel started with PID: $LT_PID"
echo "Waiting for tunnel to be ready..."

# Wait for localtunnel to be ready
sleep 10

# Get the localtunnel URL from the log
LT_URL=$(grep -o 'https://[^[:space:]]*' /tmp/localtunnel.log | head -1)

if [ -n "$LT_URL" ]; then
    echo "=========================================="
    echo "🎉 n8n is now accessible via HTTPS!"
    echo "=========================================="
    echo "Local URL: http://localhost:5678"
    echo "HTTPS URL: $LT_URL"
    echo "=========================================="
    echo "Use the HTTPS URL for your Telegram webhooks"
    echo "=========================================="
    echo "To stop: ./stop-n8n.sh"
    echo "=========================================="
    
    # Save the URL to a file for easy access
    echo "$LT_URL" > /tmp/n8n-https-url.txt
    echo "URL saved to /tmp/n8n-https-url.txt"
else
    echo "Failed to get localtunnel URL. Check /tmp/localtunnel.log for details"
    echo "You can also check the localtunnel output manually"
fi

# Keep the script running
echo "Press Ctrl+C to stop n8n and localtunnel"
wait $LT_PID