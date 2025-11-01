#!/usr/bin/env python3
"""
Update the VAPI assistant with the webhook server URL
"""

import os
import json
import requests

VAPI_API_KEY = os.getenv("VAPI_PRIVATE_KEY")
WEBHOOK_URL = "https://5000-i56c1e9ksjn5gfk546mv5-247ad190.manusvm.computer/webhook/tools"

# Load the assistant config
with open('/home/ubuntu/vapi_agent_config.json', 'r') as f:
    config = json.load(f)

assistant_id = config['assistant_id']
tool_ids = config['tool_ids']

print(f"Updating assistant {assistant_id} with webhook URL...")
print(f"Webhook URL: {WEBHOOK_URL}")
print()

headers = {
    "Authorization": f"Bearer {VAPI_API_KEY}",
    "Content-Type": "application/json"
}

# Update assistant with server URL
update_payload = {
    "server": {
        "url": WEBHOOK_URL,
        "timeoutSeconds": 30
    },
    "serverMessages": [
        "conversation-update",
        "end-of-call-report",
        "function-call",
        "hang",
        "speech-update",
        "status-update",
        "tool-calls",
        "user-interrupted"
    ]
}

response = requests.patch(
    f"https://api.vapi.ai/assistant/{assistant_id}",
    headers=headers,
    json=update_payload
)

if response.status_code == 200:
    print("✅ Assistant updated successfully with webhook URL!")
    print()
    print("Your Pepper Potts Chief of Staff agent is now fully configured!")
    print()
    print(f"Assistant ID: {assistant_id}")
    print(f"Webhook URL: {WEBHOOK_URL}")
    print()
    print("You can now test your agent in the VAPI dashboard or via API calls.")
else:
    print(f"❌ Failed to update assistant: {response.status_code}")
    print(f"Response: {response.text}")
