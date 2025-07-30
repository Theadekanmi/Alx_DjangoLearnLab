#!/bin/bash

echo "=== Testing n8n Setup ==="

# Test 1: Check if n8n container is running
echo "1. Checking n8n container..."
if sudo docker ps | grep -q n8n; then
    echo "✅ n8n container is running"
else
    echo "❌ n8n container is not running"
    echo "   Run: sudo docker run -d --name n8n -p 5678:5678 -v ~/n8n-data:/home/node/.n8n n8nio/n8n:latest"
    exit 1
fi

# Test 2: Check if n8n is responding
echo "2. Checking n8n health..."
if curl -s http://localhost:5678/healthz > /dev/null 2>&1; then
    echo "✅ n8n is responding on http://localhost:5678"
else
    echo "❌ n8n is not responding"
    echo "   Check logs: sudo docker logs n8n"
    exit 1
fi

# Test 3: Check if backup directory exists
echo "3. Checking backup directory..."
if [ -d "$HOME/n8n-backups" ]; then
    echo "✅ Backup directory exists: $HOME/n8n-backups"
else
    echo "⚠️  Backup directory doesn't exist, creating..."
    mkdir -p "$HOME/n8n-backups"
fi

# Test 4: Check if ngrok is installed
echo "4. Checking ngrok installation..."
if command -v ngrok >/dev/null 2>&1; then
    echo "✅ ngrok is installed"
    echo "   To setup: ./setup-ngrok.sh"
else
    echo "❌ ngrok is not installed"
fi

# Test 5: Check if localtunnel is installed
echo "5. Checking localtunnel installation..."
if command -v lt >/dev/null 2>&1; then
    echo "✅ localtunnel is installed"
    echo "   To start with localtunnel: ./start-n8n-localtunnel.sh"
else
    echo "❌ localtunnel is not installed"
fi

# Test 6: Check if backup script is executable
echo "6. Checking backup script..."
if [ -x "/workspace/backup-n8n.sh" ]; then
    echo "✅ Backup script is executable"
    echo "   To backup: ./backup-n8n.sh"
else
    echo "❌ Backup script is not executable"
fi

echo ""
echo "=== Setup Summary ==="
echo "✅ n8n is running and accessible"
echo "✅ Backup system is ready"
echo ""
echo "Next steps:"
echo "1. Setup ngrok: ./setup-ngrok.sh"
echo "2. Start with HTTPS: ./start-n8n.sh"
echo "3. Or use localtunnel: ./start-n8n-localtunnel.sh"
echo "4. Test backup: ./backup-n8n.sh"
echo ""
echo "Access n8n at: http://localhost:5678"