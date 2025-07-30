#!/bin/bash

echo "=== Starting ngrok tunnel ==="
echo "This will create an HTTPS URL for your n8n webhooks"
echo ""

# Check if n8n is running
if ! sudo docker ps | grep -q n8n; then
    echo "❌ n8n is not running!"
    echo "Start n8n first, then run this script again"
    exit 1
fi

echo "✅ n8n is running on port 5678"
echo "Starting ngrok tunnel..."
echo ""

# Start ngrok
ngrok http 5678

echo ""
echo "✅ ngrok tunnel started!"
echo "Use the HTTPS URL above for your Telegram webhooks"