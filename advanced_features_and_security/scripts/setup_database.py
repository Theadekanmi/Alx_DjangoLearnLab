#!/usr/bin/env python
"""
Script to set up the database with migrations for the custom user model.
Run this after creating the project structure.
"""

import os
import sys
import django
from django.core.management import execute_from_command_line

# Add the project directory to Python path
sys.path.append('/path/to/advanced_features_and_security')

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'advanced_features_and_security.settings')
django.setup()

def setup_database():
    """
    Create migrations and apply them to set up the database.
    """
    print("Creating migrations for the custom user model...")
    execute_from_command_line(['manage.py', 'makemigrations', 'accounts'])
    
    print("Applying migrations...")
    execute_from_command_line(['manage.py', 'migrate'])
    
    print("Database setup complete!")
    print("You can now create a superuser with: python manage.py createsuperuser")

if __name__ == '__main__':
    setup_database()
