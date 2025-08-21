#!/usr/bin/env python3
"""
Simple test script for the Social Media API
Run this script to test the basic functionality
"""

import requests
import json
import sys

BASE_URL = "http://localhost:8000/api"

def test_user_registration():
    """Test user registration endpoint"""
    print("Testing user registration...")
    
    data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpass123",
        "password_confirm": "testpass123",
        "bio": "Test user bio"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/accounts/register/", json=data)
        if response.status_code == 201:
            print("✅ User registration successful")
            return response.json().get('token')
        else:
            print(f"❌ User registration failed: {response.status_code}")
            print(response.text)
            return None
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to server. Make sure the server is running.")
        return None

def test_user_login():
    """Test user login endpoint"""
    print("Testing user login...")
    
    data = {
        "username": "testuser",
        "password": "testpass123"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/accounts/login/", json=data)
        if response.status_code == 200:
            print("✅ User login successful")
            return response.json().get('token')
        else:
            print(f"❌ User login failed: {response.status_code}")
            print(response.text)
            return None
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to server. Make sure the server is running.")
        return None

def test_create_post(token):
    """Test post creation endpoint"""
    print("Testing post creation...")
    
    headers = {"Authorization": f"Token {token}"}
    data = {
        "title": "Test Post",
        "content": "This is a test post content."
    }
    
    try:
        response = requests.post(f"{BASE_URL}/posts/", json=data, headers=headers)
        if response.status_code == 201:
            print("✅ Post creation successful")
            return response.json().get('id')
        else:
            print(f"❌ Post creation failed: {response.status_code}")
            print(response.text)
            return None
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to server. Make sure the server is running.")
        return None

def test_get_posts(token):
    """Test getting posts endpoint"""
    print("Testing get posts...")
    
    headers = {"Authorization": f"Token {token}"}
    
    try:
        response = requests.get(f"{BASE_URL}/posts/", headers=headers)
        if response.status_code == 200:
            print("✅ Get posts successful")
            posts = response.json()
            print(f"   Found {len(posts.get('results', posts))} posts")
            return True
        else:
            print(f"❌ Get posts failed: {response.status_code}")
            print(response.text)
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to server. Make sure the server is running.")
        return False

def test_user_profile(token):
    """Test user profile endpoint"""
    print("Testing user profile...")
    
    headers = {"Authorization": f"Token {token}"}
    
    try:
        response = requests.get(f"{BASE_URL}/accounts/profile/", headers=headers)
        if response.status_code == 200:
            print("✅ Get user profile successful")
            profile = response.json()
            print(f"   Username: {profile.get('username')}")
            print(f"   Bio: {profile.get('bio')}")
            return True
        else:
            print(f"❌ Get user profile failed: {response.status_code}")
            print(response.text)
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to server. Make sure the server is running.")
        return False

def main():
    """Run all tests"""
    print("🚀 Starting Social Media API Tests")
    print("=" * 50)
    
    # Test user registration
    token = test_user_registration()
    if not token:
        print("\n❌ Tests failed. Cannot proceed without authentication token.")
        sys.exit(1)
    
    print()
    
    # Test user login
    login_token = test_user_login()
    if not login_token:
        print("\n❌ Tests failed. Cannot proceed without authentication token.")
        sys.exit(1)
    
    print()
    
    # Test user profile
    test_user_profile(login_token)
    
    print()
    
    # Test post creation
    post_id = test_create_post(login_token)
    
    print()
    
    # Test getting posts
    test_get_posts(login_token)
    
    print()
    print("=" * 50)
    print("✅ All tests completed!")
    
    if post_id:
        print(f"📝 Test post created with ID: {post_id}")
    
    print("\n🎉 Your Social Media API is working correctly!")
    print("You can now use tools like Postman or curl to test the full API.")

if __name__ == "__main__":
    main()