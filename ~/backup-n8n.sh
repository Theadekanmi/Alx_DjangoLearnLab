#!/bin/bash

echo "=== n8n Backup ==="
echo "Creating backup..."

# Create backup directory
mkdir -p ~/n8n-backups

# Get current date
DATE=$(date +%Y%m%d_%H%M%S)

# Backup n8n data
echo "Backing up n8n data..."
tar -czf ~/n8n-backups/n8n_backup_$DATE.tar.gz -C ~ n8n-data

echo "✅ Backup created: ~/n8n-backups/n8n_backup_$DATE.tar.gz"
echo "To restore: tar -xzf ~/n8n-backups/n8n_backup_$DATE.tar.gz -C ~"