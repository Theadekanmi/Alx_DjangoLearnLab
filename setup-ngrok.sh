#!/bin/bash

echo "=== ngrok Setup ==="
echo "1. Go to: https://dashboard.ngrok.com/signup"
echo "2. Create a free account"
echo "3. Go to: https://dashboard.ngrok.com/get-started/your-authtoken"
echo "4. Copy your authtoken"
echo ""
echo "Enter your ngrok authtoken:"
read -s AUTHTOKEN

if [ -n "$AUTHTOKEN" ]; then
    ngrok config add-authtoken "$AUTHTOKEN"
    echo "✅ ngrok configured successfully!"
    echo "Now you can run: ./start-n8n.sh"
else
    echo "❌ No authtoken provided"
fi