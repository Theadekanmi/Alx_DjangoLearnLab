#!/bin/bash

echo "Starting ngrok tunnel for n8n..."
echo "Your n8n should be running on port 5678"

# Start ngrok tunnel
ngrok http 5678

echo ""
echo "✅ ngrok tunnel started!"
echo "Use the HTTPS URL for your Telegram webhooks"
echo "Example: https://abc123.ngrok.io/webhook/your-workflow-id"