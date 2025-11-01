#!/usr/bin/env python3
"""
VAPI Tool Server v2 - Fixed Mem0 authentication and API format
"""

import os
import json
from flask import Flask, request, jsonify
from datetime import datetime
import requests
from anthropic import Anthropic
from mem0 import MemoryClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv('/home/ubuntu/.env')

MEM0_API_KEY = os.getenv("MEM0_API_KEY")
FIRECRAWL_API_KEY = os.getenv("FIRECRAWL_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

print(f"Loaded API keys:")
print(f"  MEM0: {MEM0_API_KEY[:10]}..." if MEM0_API_KEY else "  MEM0: NOT SET")
print(f"  ANTHROPIC: {ANTHROPIC_API_KEY[:10]}..." if ANTHROPIC_API_KEY else "  ANTHROPIC: NOT SET")

app = Flask(__name__)

# Initialize clients
anthropic_client = Anthropic(api_key=ANTHROPIC_API_KEY)
mem0_client = MemoryClient(api_key=MEM0_API_KEY)

class ToolHandler:
    """Handles all tool executions"""
    
    @staticmethod
    def mem0_memory(action: str, user_id: str, content: str = None) -> dict:
        """Handle Mem0 memory operations using official SDK"""
        try:
            if action == "add":
                # Add memory using SDK
                messages = [
                    {"role": "user", "content": content}
                ]
                
                result = mem0_client.add(
                    messages=messages,
                    user_id=user_id,
                    version="v2"
                )
                
                return {
                    "success": True,
                    "message": f"Memory stored successfully",
                    "data": result
                }
            
            elif action == "search":
                # Search memories using SDK with proper filters
                results = mem0_client.search(
                    query=content,
                    filters={"user_id": user_id},
                    version="v2"
                )
                
                return {
                    "success": True,
                    "message": f"Found {len(results.get('results', []))} relevant memories",
                    "memories": results.get('results', [])
                }
            
            elif action == "get_all":
                # Get all memories using SDK with proper filters
                results = mem0_client.get_all(
                    filters={"user_id": user_id},
                    version="v2"
                )
                
                return {
                    "success": True,
                    "message": f"Retrieved {len(results)} memories",
                    "memories": results
                }
            
        except Exception as e:
            return {
                "success": False,
                "message": f"Error in memory operation: {str(e)}"
            }
    
    @staticmethod
    def web_search(query: str, num_results: int = 5) -> dict:
        """Handle Firecrawl web search"""
        try:
            headers = {
                "Authorization": f"Bearer {FIRECRAWL_API_KEY}",
                "Content-Type": "application/json"
            }
            
            payload = {
                "query": query,
                "limit": num_results
            }
            
            response = requests.post(
                "https://api.firecrawl.dev/v1/search",
                headers=headers,
                json=payload
            )
            
            if response.status_code == 200:
                results = response.json()
                return {
                    "success": True,
                    "message": f"Found {len(results.get('data', []))} results for '{query}'",
                    "results": results.get('data', [])
                }
            else:
                return {
                    "success": False,
                    "message": f"Search failed: {response.text}"
                }
        except Exception as e:
            return {
                "success": False,
                "message": f"Error in web search: {str(e)}"
            }
    
    @staticmethod
    def tavily_search(query: str, search_depth: str = "basic") -> dict:
        """Handle Tavily AI search"""
        try:
            headers = {
                "Content-Type": "application/json"
            }
            
            payload = {
                "api_key": TAVILY_API_KEY,
                "query": query,
                "search_depth": search_depth,
                "include_answer": True,
                "include_raw_content": False
            }
            
            response = requests.post(
                "https://api.tavily.com/search",
                headers=headers,
                json=payload
            )
            
            if response.status_code == 200:
                results = response.json()
                return {
                    "success": True,
                    "message": f"Search completed for '{query}'",
                    "answer": results.get('answer', ''),
                    "results": results.get('results', [])
                }
            else:
                return {
                    "success": False,
                    "message": f"Tavily search failed: {response.text}"
                }
        except Exception as e:
            return {
                "success": False,
                "message": f"Error in Tavily search: {str(e)}"
            }
    
    @staticmethod
    def write_document(task: str, context: str = "", format: str = "markdown") -> dict:
        """Handle document writing using Anthropic"""
        try:
            prompt = f"""Write the following document:

Task: {task}

{f'Context: {context}' if context else ''}

Format: {format}

Please write a complete, well-structured document that fulfills this task. Be professional, clear, and thorough."""

            message = anthropic_client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=4000,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            document_content = message.content[0].text
            
            return {
                "success": True,
                "message": "Document created successfully",
                "document": document_content,
                "format": format
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"Error writing document: {str(e)}"
            }
    
    @staticmethod
    def break_down_task(task: str, context: str = "", time_available: str = "") -> dict:
        """Break down complex tasks into manageable steps"""
        try:
            prompt = f"""As a supportive Chief of Staff helping someone with ADHD, break down this task into clear, manageable steps:

Task: {task}

{f'Context: {context}' if context else ''}
{f'Time Available: {time_available}' if time_available else ''}

Please provide:
1. A breakdown into small, concrete steps
2. Estimated time for each step
3. Which step to start with
4. Any potential obstacles and how to overcome them
5. Celebration points along the way

Be encouraging and practical. Focus on making it easy to start."""

            message = anthropic_client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=2000,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            breakdown = message.content[0].text
            
            return {
                "success": True,
                "message": "Task broken down successfully",
                "breakdown": breakdown
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"Error breaking down task: {str(e)}"
            }
    
    @staticmethod
    def manage_calendar(action: str, date: str = None, details: str = None) -> dict:
        """Handle calendar operations (placeholder for now)"""
        return {
            "success": True,
            "message": f"Calendar {action} requested for {date if date else 'today'}",
            "note": "Calendar integration requires additional setup with your calendar provider",
            "details": details
        }

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "timestamp": datetime.now().isoformat()})

@app.route('/webhook/tools', methods=['POST'])
def handle_tool_calls():
    """Main webhook endpoint for all VAPI tool calls"""
    try:
        data = request.json
        print(f"\n📥 Received tool call: {json.dumps(data, indent=2)}")
        
        message = data.get('message', {})
        tool_call_list = message.get('toolCallList', [])
        
        results = []
        
        for tool_call in tool_call_list:
            tool_id = tool_call.get('id')
            tool_name = tool_call.get('name')
            arguments = tool_call.get('arguments', {})
            
            print(f"\n🔧 Processing tool: {tool_name}")
            print(f"   Arguments: {arguments}")
            
            # Route to appropriate handler
            if tool_name == "mem0_memory":
                result = ToolHandler.mem0_memory(
                    action=arguments.get('action'),
                    user_id=arguments.get('user_id', 'default_user'),
                    content=arguments.get('content')
                )
            
            elif tool_name == "web_search":
                result = ToolHandler.web_search(
                    query=arguments.get('query'),
                    num_results=arguments.get('num_results', 5)
                )
            
            elif tool_name == "tavily_search":
                result = ToolHandler.tavily_search(
                    query=arguments.get('query'),
                    search_depth=arguments.get('search_depth', 'basic')
                )
            
            elif tool_name == "write_document":
                result = ToolHandler.write_document(
                    task=arguments.get('task'),
                    context=arguments.get('context', ''),
                    format=arguments.get('format', 'markdown')
                )
            
            elif tool_name == "break_down_task":
                result = ToolHandler.break_down_task(
                    task=arguments.get('task'),
                    context=arguments.get('context', ''),
                    time_available=arguments.get('time_available', '')
                )
            
            elif tool_name == "manage_calendar":
                result = ToolHandler.manage_calendar(
                    action=arguments.get('action'),
                    date=arguments.get('date'),
                    details=arguments.get('details')
                )
            
            else:
                result = {
                    "success": False,
                    "message": f"Unknown tool: {tool_name}"
                }
            
            # Format result for VAPI
            results.append({
                "toolCallId": tool_id,
                "result": json.dumps(result)
            })
            
            print(f"✅ Tool result: {result.get('message', 'Completed')}")
        
        response = {"results": results}
        print(f"\n📤 Sending response: {json.dumps(response, indent=2)}")
        
        return jsonify(response)
    
    except Exception as e:
        print(f"\n❌ Error handling tool call: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({
            "error": str(e),
            "results": []
        }), 500

@app.route('/test/memory', methods=['POST'])
def test_memory():
    """Test endpoint for memory operations"""
    data = request.json
    result = ToolHandler.mem0_memory(
        action=data.get('action', 'add'),
        user_id=data.get('user_id', 'test_user'),
        content=data.get('content', 'Test memory')
    )
    return jsonify(result)

@app.route('/test/search', methods=['POST'])
def test_search():
    """Test endpoint for web search"""
    data = request.json
    result = ToolHandler.web_search(
        query=data.get('query', 'test query')
    )
    return jsonify(result)

if __name__ == '__main__':
    print("=" * 60)
    print("VAPI Tool Server v2 Starting")
    print("=" * 60)
    print(f"Health check: http://localhost:5000/health")
    print(f"Tool webhook: http://localhost:5000/webhook/tools")
    print("=" * 60)
    app.run(host='0.0.0.0', port=5000, debug=True)
