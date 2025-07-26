#!/usr/bin/env python
"""
Security testing script for Django application
"""
import os
import django
from django.test import TestCase, Client
from django.contrib.auth.models import User, Group
from django.urls import reverse

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from bookshelf.models import Book, Author
from bookshelf.forms import BookForm, BookSearchForm

def test_xss_protection():
    """Test XSS protection in forms"""
    print("Ì¥ç Testing XSS protection...")
    
    # Test malicious input
    malicious_inputs = [
        "<script>alert('XSS')</script>",
        "javascript:alert('XSS')",
        "<img src=x onerror=alert('XSS')>",
        "';DROP TABLE books;--"
    ]
    
    for malicious_input in malicious_inputs:
        form = BookSearchForm({'search': malicious_input})
        if form.is_valid():
            print(f"‚ùå XSS test failed: {malicious_input}")
        else:
            print(f"‚úÖ XSS blocked: {malicious_input}")

def test_csrf_protection():
    """Test CSRF protection"""
    print("Ì¥ç Testing CSRF protection...")
    client = Client(enforce_csrf_checks=True)
    
    # Try to create a book without CSRF token
    response = client.post('/books/create/', {
        'title': 'Test Book',
        'author': 1,
        'publication_year': 2023
    })
    
    if response.status_code == 403:
        print("‚úÖ CSRF protection working")
    else:
        print("‚ùå CSRF protection failed")

def run_security_tests():
    """Run all security tests"""
    print("Ìª°Ô∏è  Running Security Tests")
    print("=" * 50)
    
    test_xss_protection()
    test_csrf_protection()
    
    print("=" * 50)
    print("ÌøÅ Security testing completed")

if __name__ == "__main__":
    run_security_tests()
