# Setup Guide - Pepper Potts Chief of Staff

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/pepper-chief-of-staff.git
cd pepper-chief-of-staff
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Copy the example environment file and fill in your API keys:

```bash
cp .env.example .env
```

Edit `.env` with your actual API keys:
- Get VAPI keys from: https://dashboard.vapi.ai
- Get Mem0 API key from: https://app.mem0.ai
- Get Anthropic API key from: https://console.anthropic.com
- Get Firecrawl API key from: https://firecrawl.dev
- Get Tavily API key from: https://tavily.com
- Get Cartesia API key from: https://cartesia.ai

### 4. Create the VAPI Agent

Run the agent creation script:

```bash
python create_vapi_agent.py
```

This will:
- Create 6 tools in VAPI (Memory, Web Search, AI Search, Document Writer, Task Breakdown, Calendar)
- Create the Pepper Potts assistant
- Save the configuration to `vapi_agent_config.json`

### 5. Start the Tool Server

```bash
python vapi_tool_server_v2.py
```

The server will start on `http://localhost:5000`

### 6. Expose the Server (for production)

For production use, you'll need to expose your server to the internet so VAPI can reach it.

Options:
- Use a cloud service (AWS, Google Cloud, Azure)
- Use ngrok: `ngrok http 5000`
- Use a VPS with a public IP

### 7. Update Assistant with Webhook URL

Once your server is publicly accessible, update the assistant:

```bash
# Edit update_assistant_webhooks.py with your public URL
python update_assistant_webhooks.py
```

### 8. Test Your Agent

#### Via VAPI Dashboard
1. Go to https://dashboard.vapi.ai
2. Find "Pepper - Chief of Staff" in Assistants
3. Click "Test" to start a voice conversation

#### Via API
```python
import requests

response = requests.post(
    "https://api.vapi.ai/call/phone",
    headers={
        "Authorization": f"Bearer {VAPI_PRIVATE_KEY}",
        "Content-Type": "application/json"
    },
    json={
        "assistantId": "YOUR_ASSISTANT_ID",
        "customer": {
            "number": "+1234567890"
        }
    }
)
```

## Testing

### Test Memory Integration

```bash
python test_memory.py
```

This will test:
- Adding memories
- Searching memories
- Retrieving all memories

### Test Tool Server Health

```bash
curl http://localhost:5000/health
```

## Troubleshooting

### Server Not Starting
- Check that port 5000 is not in use: `lsof -i :5000`
- Verify all environment variables are set: `python -c "import os; from dotenv import load_dotenv; load_dotenv(); print(os.getenv('MEM0_API_KEY'))"`

### Memory Not Working
- Verify Mem0 API key is valid
- Check server logs: `tail -f tool_server_v2.log`
- Test memory endpoint directly: `curl -X POST http://localhost:5000/test/memory -H "Content-Type: application/json" -d '{"action":"add","user_id":"test","content":"Test memory"}'`

### VAPI Not Calling Tools
- Verify webhook URL is publicly accessible
- Check that the assistant has the correct server URL configured
- Look for tool call logs in the server output

## Production Deployment

### Using Docker (Recommended)

Create a `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "vapi_tool_server_v2.py"]
```

Build and run:

```bash
docker build -t pepper-chief-of-staff .
docker run -p 5000:5000 --env-file .env pepper-chief-of-staff
```

### Using a Process Manager

Install PM2:

```bash
npm install -g pm2
```

Start the server:

```bash
pm2 start vapi_tool_server_v2.py --interpreter python3 --name pepper-server
pm2 save
pm2 startup
```

## Customization

### Modify Personality

Edit the system prompt in `create_vapi_agent.py`:

```python
system_prompt = """You are a Pepper Potts-style Chief of Staff...
[Customize this text]
"""
```

Then recreate the assistant:

```bash
python create_vapi_agent.py
```

### Add New Tools

1. Add a new tool method in `vapi_tool_server_v2.py`:

```python
@staticmethod
def my_new_tool(param1: str) -> dict:
    # Your tool logic here
    return {
        "success": True,
        "message": "Tool executed",
        "data": result
    }
```

2. Add the tool to the webhook handler:

```python
elif tool_name == "my_new_tool":
    result = ToolHandler.my_new_tool(
        param1=arguments.get('param1')
    )
```

3. Create the tool in VAPI via the dashboard or API

## Support

For issues or questions:
- Check the [PEPPER_AGENT_GUIDE.md](PEPPER_AGENT_GUIDE.md) for detailed usage
- Review [README.md](README.md) for complete documentation
- Open an issue on GitHub

## License

MIT License - See LICENSE file for details
