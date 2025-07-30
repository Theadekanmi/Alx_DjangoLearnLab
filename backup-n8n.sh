#!/bin/bash

# n8n Backup Script
# This script backs up your n8n data and exports workflows

BACKUP_DIR="$HOME/n8n-backups"
N8N_DATA_DIR="$HOME/n8n-data"
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_NAME="n8n_backup_$DATE"

echo "Starting n8n backup at $(date)"

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Stop n8n container to ensure data consistency
echo "Stopping n8n container..."
docker-compose -f /workspace/docker-compose.yml stop n8n

# Wait a moment for container to stop
sleep 5

# Backup the entire n8n data directory
echo "Creating backup of n8n data..."
tar -czf "$BACKUP_DIR/${BACKUP_NAME}_data.tar.gz" -C "$HOME" n8n-data

# Start n8n container again
echo "Starting n8n container..."
docker-compose -f /workspace/docker-compose.yml start n8n

# Wait for n8n to be ready
echo "Waiting for n8n to be ready..."
sleep 30

# Export workflows using n8n API (if n8n is running)
if curl -s http://localhost:5678/healthz > /dev/null 2>&1; then
    echo "Exporting workflows..."
    curl -s -u "admin:your_password_here" \
         -X GET \
         "http://localhost:5678/rest/workflows" \
         -H "Content-Type: application/json" \
         > "$BACKUP_DIR/${BACKUP_NAME}_workflows.json" 2>/dev/null
    
    if [ $? -eq 0 ]; then
        echo "Workflows exported successfully"
    else
        echo "Failed to export workflows"
    fi
else
    echo "n8n is not ready, skipping workflow export"
fi

# Clean up old backups (keep last 10)
echo "Cleaning up old backups..."
cd "$BACKUP_DIR"
ls -t *.tar.gz | tail -n +11 | xargs -r rm
ls -t *_workflows.json | tail -n +11 | xargs -r rm

echo "Backup completed: $BACKUP_NAME"
echo "Backup location: $BACKUP_DIR"
echo "Backup files:"
ls -la "$BACKUP_DIR"/*"$DATE"*