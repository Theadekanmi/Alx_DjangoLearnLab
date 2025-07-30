#!/bin/bash

echo "Backing up n8n data..."

# Create backup directory
mkdir -p ~/n8n-backups

# Backup n8n data
tar -czf ~/n8n-backups/n8n_backup_$(date +%Y%m%d_%H%M%S).tar.gz -C ~ n8n-data

echo "✅ Backup created in ~/n8n-backups/"
echo "To restore: tar -xzf ~/n8n-backups/backup_file.tar.gz -C ~"