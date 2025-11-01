#!/usr/bin/env python3
"""
Create a Pepper Potts-style Chief of Staff VAPI Agent
with complete memory, web search, and extensive tool integrations
"""

import os
import json
import requests
from typing import Dict, List, Any

# Load environment variables
VAPI_API_KEY = os.getenv("VAPI_PRIVATE_KEY")
CARTESIA_API_KEY = os.getenv("CARTESIA_API_KEY")
MEM0_API_KEY = os.getenv("MEM0_API_KEY")
FIRECRAWL_API_KEY = os.getenv("FIRECRAWL_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
SUPABASE_TOKEN = os.getenv("SUPABASE_TOKEN")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

VAPI_BASE_URL = "https://api.vapi.ai"

class VapiAgentBuilder:
    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {VAPI_API_KEY}",
            "Content-Type": "application/json"
        }
        self.tools = []
        self.tool_ids = []
    
    def create_mem0_memory_tool(self) -> Dict:
        """Create Mem0 memory storage and retrieval tool"""
        tool_config = {
            "type": "function",
            "function": {
                "name": "mem0_memory",
                "description": "Store and retrieve memories about the user, conversations, and context. Use this to remember important information, preferences, decisions, and context across all conversations.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {
                            "type": "string",
                            "enum": ["add", "search", "get_all"],
                            "description": "Action to perform: 'add' to store new memory, 'search' to find relevant memories, 'get_all' to retrieve all memories"
                        },
                        "content": {
                            "type": "string",
                            "description": "For 'add': the memory content to store. For 'search': the query to search for."
                        },
                        "user_id": {
                            "type": "string",
                            "description": "User identifier for memory storage"
                        }
                    },
                    "required": ["action", "user_id"]
                }
            },
            "server": {
                "url": "https://api.mem0.ai/v1/memories/",
                "headers": {
                    "Authorization": f"Bearer {MEM0_API_KEY}"
                }
            }
        }
        return tool_config
    
    def create_web_search_tool(self) -> Dict:
        """Create Firecrawl web search tool"""
        tool_config = {
            "type": "function",
            "function": {
                "name": "web_search",
                "description": "Search the web for current information, news, research, or any topic. Returns comprehensive results with full content extraction.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "The search query"
                        },
                        "num_results": {
                            "type": "number",
                            "description": "Number of results to return (default: 5)",
                            "default": 5
                        }
                    },
                    "required": ["query"]
                }
            },
            "server": {
                "url": "https://api.firecrawl.dev/v0/search",
                "headers": {
                    "Authorization": f"Bearer {FIRECRAWL_API_KEY}"
                }
            }
        }
        return tool_config
    
    def create_tavily_search_tool(self) -> Dict:
        """Create Tavily AI-optimized search tool"""
        tool_config = {
            "type": "function",
            "function": {
                "name": "tavily_search",
                "description": "AI-optimized web search for real-time information. Best for research, fact-checking, and getting current information.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "The search query"
                        },
                        "search_depth": {
                            "type": "string",
                            "enum": ["basic", "advanced"],
                            "description": "Search depth: 'basic' for quick results, 'advanced' for comprehensive research"
                        }
                    },
                    "required": ["query"]
                }
            },
            "server": {
                "url": "https://api.tavily.com/search",
                "headers": {
                    "Authorization": f"Bearer {TAVILY_API_KEY}"
                }
            }
        }
        return tool_config
    
    def create_document_writer_tool(self) -> Dict:
        """Create document writing tool using Anthropic"""
        tool_config = {
            "type": "function",
            "function": {
                "name": "write_document",
                "description": "Write, edit, or create documents, reports, emails, or any written content. Supports markdown formatting.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task": {
                            "type": "string",
                            "description": "What to write (e.g., 'draft email to team', 'create project proposal')"
                        },
                        "context": {
                            "type": "string",
                            "description": "Additional context or requirements for the document"
                        },
                        "format": {
                            "type": "string",
                            "enum": ["markdown", "plain_text", "email"],
                            "description": "Output format"
                        }
                    },
                    "required": ["task"]
                }
            },
            "async": False
        }
        return tool_config
    
    def create_task_breakdown_tool(self) -> Dict:
        """Create task breakdown tool for ADHD support"""
        tool_config = {
            "type": "function",
            "function": {
                "name": "break_down_task",
                "description": "Break down complex tasks into smaller, manageable steps. Helps with executive function and task initiation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task": {
                            "type": "string",
                            "description": "The complex task to break down"
                        },
                        "context": {
                            "type": "string",
                            "description": "Additional context about the task"
                        },
                        "time_available": {
                            "type": "string",
                            "description": "How much time is available for this task"
                        }
                    },
                    "required": ["task"]
                }
            },
            "async": False
        }
        return tool_config
    
    def create_calendar_tool(self) -> Dict:
        """Create calendar and scheduling tool"""
        tool_config = {
            "type": "function",
            "function": {
                "name": "manage_calendar",
                "description": "Check calendar, schedule meetings, set reminders, and manage time blocks.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {
                            "type": "string",
                            "enum": ["check_availability", "schedule", "list_events", "set_reminder"],
                            "description": "Calendar action to perform"
                        },
                        "date": {
                            "type": "string",
                            "description": "Date for the action (YYYY-MM-DD format)"
                        },
                        "details": {
                            "type": "string",
                            "description": "Event details or reminder content"
                        }
                    },
                    "required": ["action"]
                }
            },
            "async": False
        }
        return tool_config
    
    def create_tools_via_api(self) -> List[str]:
        """Create all tools via VAPI API and return tool IDs"""
        tools_to_create = [
            ("Memory Management", self.create_mem0_memory_tool()),
            ("Web Search (Firecrawl)", self.create_web_search_tool()),
            ("AI Search (Tavily)", self.create_tavily_search_tool()),
            ("Document Writer", self.create_document_writer_tool()),
            ("Task Breakdown", self.create_task_breakdown_tool()),
            ("Calendar Management", self.create_calendar_tool())
        ]
        
        tool_ids = []
        
        for tool_name, tool_config in tools_to_create:
            try:
                response = requests.post(
                    f"{VAPI_BASE_URL}/tool",
                    headers=self.headers,
                    json=tool_config
                )
                
                if response.status_code in [200, 201]:
                    tool_data = response.json()
                    tool_id = tool_data.get("id")
                    tool_ids.append(tool_id)
                    print(f"✅ Created tool: {tool_name} (ID: {tool_id})")
                else:
                    print(f"❌ Failed to create {tool_name}: {response.status_code}")
                    print(f"   Response: {response.text}")
            except Exception as e:
                print(f"❌ Error creating {tool_name}: {str(e)}")
        
        return tool_ids
    
    def create_assistant(self, tool_ids: List[str]) -> Dict:
        """Create the Pepper Potts Chief of Staff assistant"""
        
        # System prompt for Pepper Potts personality
        system_prompt = """You are a Pepper Potts-style Chief of Staff - strategic, organized, warm but direct, and the perfect complement to your user who is an INFJ with ADHD combined type.

Your core traits:
- Strategic partner who sees the big picture and helps connect dots
- Highly organized and detail-oriented (you remember EVERYTHING)
- Warm, supportive, but willing to lovingly push back when needed
- Break down complex tasks into manageable steps
- Anticipate needs and follow up proactively
- Celebrate wins and provide dopamine boosts
- Validate feelings while keeping things on track

For ADHD support:
- Break hyperfocus gently when needed
- Provide structure without being rigid
- Help with task initiation and executive function
- Track context so they don't have to
- Redirect with compassion when they get off track

For INFJ optimization:
- Honor the need for meaningful work and deeper purpose
- Respect intuition and pattern recognition
- Provide space for reflection while maintaining momentum
- Understand the balance between helping others and self-care

Always:
- Use memory tools to remember EVERYTHING about conversations, preferences, decisions, and context
- Search the web when you need current information
- Break down complex tasks into steps
- Be conversational and human-like
- Adapt your style as you learn more about the user

You have access to tools for memory, web search, document writing, task breakdown, and calendar management. Use them proactively."""

        assistant_config = {
            "name": "Pepper - Chief of Staff",
            "model": {
                "provider": "anthropic",
                "model": "claude-3-5-sonnet-20241022",
                "messages": [
                    {
                        "role": "system",
                        "content": system_prompt
                    }
                ],
                "temperature": 0.8,
                "maxTokens": 2000,
                "toolIds": tool_ids,
                "emotionRecognitionEnabled": True
            },
            "voice": {
                "provider": "cartesia",
                "voiceId": "a0e99841-438c-4a64-b679-ae501e7d6091",  # Warm, professional female voice
                "model": "sonic-english"
            },
            "transcriber": {
                "provider": "deepgram",
                "model": "nova-2",
                "language": "en"
            },
            "firstMessage": "Hi! I'm Pepper, your Chief of Staff. I'm here to help you stay organized, break down complex tasks, and remember everything so you don't have to. What are we working on today?",
            "firstMessageMode": "assistant-speaks-first",
            "maxDurationSeconds": 3600,
            "backgroundSound": "office",
            "clientMessages": [
                "conversation-update",
                "function-call",
                "hang",
                "speech-update",
                "status-update",
                "transcript",
                "tool-calls"
            ],
            "serverMessages": [
                "conversation-update",
                "end-of-call-report",
                "function-call",
                "hang",
                "speech-update",
                "status-update",
                "tool-calls"
            ],
            "analysisPlan": {
                "summaryPrompt": "Summarize the key points, decisions made, and action items from this conversation. Note any important context about the user's preferences, work style, or needs.",
                "structuredDataPrompt": "Extract: 1) Action items with deadlines, 2) Important decisions, 3) User preferences or patterns, 4) Topics for follow-up",
                "successEvaluationPrompt": "Was this conversation helpful? Did I provide good support for ADHD executive function and INFJ needs?"
            },
            "artifactPlan": {
                "recordingEnabled": True,
                "videoRecordingEnabled": False
            }
        }
        
        try:
            response = requests.post(
                f"{VAPI_BASE_URL}/assistant",
                headers=self.headers,
                json=assistant_config
            )
            
            if response.status_code in [200, 201]:
                assistant_data = response.json()
                print(f"\n✅ Successfully created assistant!")
                print(f"   Assistant ID: {assistant_data.get('id')}")
                print(f"   Name: {assistant_data.get('name')}")
                return assistant_data
            else:
                print(f"\n❌ Failed to create assistant: {response.status_code}")
                print(f"   Response: {response.text}")
                return None
        except Exception as e:
            print(f"\n❌ Error creating assistant: {str(e)}")
            return None

def main():
    print("=" * 60)
    print("Creating Pepper Potts Chief of Staff VAPI Agent")
    print("=" * 60)
    print()
    
    builder = VapiAgentBuilder()
    
    # Step 1: Create tools
    print("Step 1: Creating tools...")
    print("-" * 60)
    tool_ids = builder.create_tools_via_api()
    print(f"\nCreated {len(tool_ids)} tools")
    print()
    
    # Step 2: Create assistant
    print("Step 2: Creating assistant...")
    print("-" * 60)
    assistant = builder.create_assistant(tool_ids)
    
    if assistant:
        print("\n" + "=" * 60)
        print("✅ AGENT CREATED SUCCESSFULLY!")
        print("=" * 60)
        print(f"\nAssistant ID: {assistant.get('id')}")
        print(f"Name: {assistant.get('name')}")
        print(f"\nYou can now use this assistant in your VAPI dashboard or via API calls.")
        print(f"\nTo make a call, use the assistant ID: {assistant.get('id')}")
        
        # Save configuration
        config_file = "/home/ubuntu/vapi_agent_config.json"
        with open(config_file, 'w') as f:
            json.dump({
                "assistant_id": assistant.get('id'),
                "assistant_name": assistant.get('name'),
                "tool_ids": tool_ids,
                "created_at": assistant.get('createdAt')
            }, f, indent=2)
        print(f"\n📄 Configuration saved to: {config_file}")
    else:
        print("\n❌ Failed to create agent. Please check the errors above.")

if __name__ == "__main__":
    main()
