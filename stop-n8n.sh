#!/bin/bash

# Stop n8n and ngrok script

echo "Stopping n8n and ngrok..."

# Stop ngrok
echo "Stopping ngrok..."
pkill -f ngrok

# Stop n8n container
echo "Stopping n8n container..."
sudo docker stop n8n

echo "n8n and ngrok stopped successfully!"
echo "To start again: ./start-n8n.sh"