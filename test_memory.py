#!/usr/bin/env python3
"""Test Mem0 memory functionality"""

import requests
import json

WEBHOOK_URL = "https://5000-i56c1e9ksjn5gfk546mv5-247ad190.manusvm.computer"

print("=" * 60)
print("Testing Mem0 Memory Integration")
print("=" * 60)
print()

# Test 1: Add a memory
print("Test 1: Adding a memory...")
response = requests.post(
    f"{WEBHOOK_URL}/test/memory",
    json={
        "action": "add",
        "user_id": "test_user_123",
        "content": "I am an INFJ with ADHD combined type. I prefer morning meetings and need 15-minute buffers between calls."
    }
)

print(f"Status: {response.status_code}")
result = response.json()
print(f"Result: {json.dumps(result, indent=2)}")
print()

# Test 2: Search memories
print("Test 2: Searching memories...")
response = requests.post(
    f"{WEBHOOK_URL}/test/memory",
    json={
        "action": "search",
        "user_id": "test_user_123",
        "content": "meeting preferences"
    }
)

print(f"Status: {response.status_code}")
result = response.json()
print(f"Result: {json.dumps(result, indent=2)}")
print()

# Test 3: Get all memories
print("Test 3: Getting all memories...")
response = requests.post(
    f"{WEBHOOK_URL}/test/memory",
    json={
        "action": "get_all",
        "user_id": "test_user_123"
    }
)

print(f"Status: {response.status_code}")
result = response.json()
print(f"Result: {json.dumps(result, indent=2)}")
print()

print("=" * 60)
print("Memory tests completed!")
print("=" * 60)
