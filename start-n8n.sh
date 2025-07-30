#!/bin/bash

# n8n Startup Script with ngrok tunnel
# This script starts n8n and creates an HTTPS tunnel

echo "Starting n8n with HTTPS tunnel..."

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

echo "n8n is ready! Starting ngrok tunnel..."

# Start ngrok tunnel in background
ngrok http 5678 > /tmp/ngrok.log 2>&1 &
NGROK_PID=$!

echo "ngrok tunnel started with PID: $NGROK_PID"
echo "Waiting for ngrok to be ready..."

# Wait for ngrok to be ready
sleep 10

# Get the ngrok URL
NGROK_URL=$(curl -s http://localhost:4040/api/tunnels | grep -o '"public_url":"[^"]*"' | cut -d'"' -f4)

if [ -n "$NGROK_URL" ]; then
    echo "=========================================="
    echo "🎉 n8n is now accessible via HTTPS!"
    echo "=========================================="
    echo "Local URL: http://localhost:5678"
    echo "HTTPS URL: $NGROK_URL"
    echo "=========================================="
    echo "Use the HTTPS URL for your Telegram webhooks"
    echo "=========================================="
    echo "To stop: ./stop-n8n.sh"
    echo "=========================================="
    
    # Save the URL to a file for easy access
    echo "$NGROK_URL" > /tmp/n8n-https-url.txt
    echo "URL saved to /tmp/n8n-https-url.txt"
else
    echo "Failed to get ngrok URL. Check /tmp/ngrok.log for details"
fi

# Keep the script running
echo "Press Ctrl+C to stop n8n and ngrok"
wait $NGROK_PID