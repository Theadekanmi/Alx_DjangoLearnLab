#!/usr/bin/env python
"""
Simple test script to verify API endpoints are working.
Run this after starting the Django development server.
"""

import requests
import json

BASE_URL = "http://localhost:8000/api"

def test_api():
    print("Testing API endpoints...")
    
    # Test 1: List books (should work without authentication)
    print("\n1. Testing GET /api/books/")
    try:
        response = requests.get(f"{BASE_URL}/books/")
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"Found {len(data.get('results', []))} books")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Test 2: List authors (should work without authentication)
    print("\n2. Testing GET /api/authors/")
    try:
        response = requests.get(f"{BASE_URL}/authors/")
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"Found {len(data.get('results', []))} authors")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Test 3: Create author (should fail without authentication)
    print("\n3. Testing POST /api/authors/ (should fail without auth)")
    try:
        data = {"name": "Test Author"}
        response = requests.post(f"{BASE_URL}/authors/", json=data)
        print(f"Status: {response.status_code}")
        if response.status_code == 401:
            print("✓ Correctly rejected unauthorized request")
        else:
            print(f"Unexpected response: {response.text}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Test 4: Search books
    print("\n4. Testing search functionality")
    try:
        response = requests.get(f"{BASE_URL}/books/?search=harry")
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"Search results: {len(data.get('results', []))} books")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Test 5: Filter books
    print("\n5. Testing filter functionality")
    try:
        response = requests.get(f"{BASE_URL}/books/?publication_year=1997")
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"Filter results: {len(data.get('results', []))} books")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\nAPI testing completed!")

if __name__ == "__main__":
    test_api()