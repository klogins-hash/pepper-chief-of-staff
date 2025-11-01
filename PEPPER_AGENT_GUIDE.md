# Pepper Potts Chief of Staff - VAPI Agent Guide

## 🎯 Overview

Your **Pepper Potts-style Chief of Staff** voice agent is now fully operational! This agent is designed specifically for INFJ personality with ADHD combined type, providing strategic support, complete memory, and extensive capabilities.

---

## 📋 Agent Details

**Assistant ID**: `29629fb8-5419-4742-b88a-9b1650b41c71`  
**Name**: Pepper - Chief of Staff  
**Model**: Anthropic Claude 3.5 Sonnet  
**Voice**: Cartesia (warm, professional female voice)  
**Transcriber**: Deepgram Nova 2

---

## 🛠️ Integrated Tools

Your agent has access to 6 powerful tools:

### 1. **Memory Management** (Mem0)
- **Purpose**: Complete remembrance of all conversations, preferences, and context
- **Capabilities**:
  - Store new memories automatically during conversations
  - Search through past memories
  - Retrieve all stored context
- **Use Cases**: 
  - "Remember that I prefer morning meetings"
  - "What did we discuss about the project last week?"
  - "What are my dietary restrictions?"

### 2. **Web Search** (Firecrawl)
- **Purpose**: Search the web for current information
- **Capabilities**:
  - Real-time web search with full content extraction
  - Returns comprehensive, structured results
- **Use Cases**:
  - "What's the latest news on AI agents?"
  - "Find information about ADHD productivity strategies"
  - "Search for the best project management tools"

### 3. **AI-Optimized Search** (Tavily)
- **Purpose**: Advanced AI-powered search for research
- **Capabilities**:
  - Neural search with semantic understanding
  - Provides direct answers along with sources
  - Basic or advanced search depth
- **Use Cases**:
  - "Research the best approaches for executive function support"
  - "What are the latest INFJ career insights?"

### 4. **Document Writer**
- **Purpose**: Create documents, emails, reports, and written content
- **Capabilities**:
  - Professional writing using Claude 3.5
  - Supports markdown, plain text, and email formats
  - Context-aware content generation
- **Use Cases**:
  - "Draft an email to my team about the project update"
  - "Write a project proposal for the new initiative"
  - "Create a meeting agenda for tomorrow"

### 5. **Task Breakdown**
- **Purpose**: Break complex tasks into manageable steps (ADHD support)
- **Capabilities**:
  - Breaks down overwhelming tasks
  - Provides time estimates
  - Identifies starting points
  - Anticipates obstacles
  - Includes celebration points
- **Use Cases**:
  - "Help me break down this presentation into steps"
  - "I need to organize my office - where do I start?"
  - "This project feels overwhelming, can you help?"

### 6. **Calendar Management**
- **Purpose**: Schedule management and reminders
- **Capabilities**:
  - Check availability
  - Schedule meetings
  - List events
  - Set reminders
- **Use Cases**:
  - "What's on my calendar today?"
  - "Schedule a meeting for next Tuesday at 2pm"
  - "Remind me to follow up on the proposal"

---

## 🎭 Personality & Approach

### Core Traits
- **Strategic Partner**: Sees the big picture, connects dots
- **Highly Organized**: Remembers everything so you don't have to
- **Warm but Direct**: Supportive yet willing to lovingly push back
- **Task-Oriented**: Breaks down complexity into manageable steps
- **Proactive**: Anticipates needs and follows up

### ADHD-Optimized Support
- ✅ Breaks hyperfocus gently when needed
- ✅ Provides structure without rigidity
- ✅ Helps with task initiation and executive function
- ✅ Tracks context to reduce cognitive load
- ✅ Redirects with compassion
- ✅ Celebrates wins for dopamine boosts

### INFJ-Optimized Approach
- ✅ Honors the need for meaningful work
- ✅ Respects intuition and pattern recognition
- ✅ Provides space for reflection while maintaining momentum
- ✅ Understands the balance between helping others and self-care
- ✅ Validates feelings while keeping things on track

---

## 🚀 How to Use Your Agent

### Via VAPI Dashboard

1. Go to [VAPI Dashboard](https://dashboard.vapi.ai)
2. Navigate to **Assistants**
3. Find **"Pepper - Chief of Staff"**
4. Click **"Test"** to start a voice conversation
5. Or click **"Deploy"** to get phone number or web integration

### Via API Call

```python
import requests

VAPI_API_KEY = "your-private-key"
assistant_id = "29629fb8-5419-4742-b88a-9b1650b41c71"

# Create a phone call
response = requests.post(
    "https://api.vapi.ai/call/phone",
    headers={
        "Authorization": f"Bearer {VAPI_API_KEY}",
        "Content-Type": "application/json"
    },
    json={
        "assistantId": assistant_id,
        "customer": {
            "number": "+1234567890"  # Your phone number
        }
    }
)
```

### Via Web Integration

```javascript
import Vapi from "@vapi-ai/web";

const vapi = new Vapi("your-public-key");

// Start call
vapi.start("29629fb8-5419-4742-b88a-9b1650b41c71");

// End call
vapi.stop();
```

---

## 🔧 Technical Architecture

### Tool Server
- **URL**: `https://5000-i56c1e9ksjn5gfk546mv5-247ad190.manusvm.computer/webhook/tools`
- **Framework**: Flask (Python)
- **Hosting**: Exposed via public webhook
- **Timeout**: 30 seconds per tool call

### Memory System
- **Provider**: Mem0 Cloud
- **Type**: Persistent, cross-session memory
- **User ID**: Automatically tracked per user
- **Graph Support**: Ready for MemAPI Graph integration

### Voice Pipeline
- **STT**: Deepgram Nova 2 (high accuracy, low latency)
- **LLM**: Anthropic Claude 3.5 Sonnet (conversational, intelligent)
- **TTS**: Cartesia Sonic (natural, human-like)

---

## 📊 Conversation Flow

1. **User speaks** → Deepgram transcribes
2. **Claude processes** → Understands intent, checks memory
3. **Tool calls** (if needed) → Searches web, stores memory, breaks down tasks
4. **Claude responds** → Contextual, personalized response
5. **Cartesia speaks** → Natural voice output
6. **Memory stored** → Everything remembered for next time

---

## 🎨 Customization Options

### Adjust Personality
Edit the system prompt in the assistant configuration to modify:
- Tone (more formal/casual)
- Directness level
- Proactivity
- Communication style

### Add More Tools
Create additional tools for:
- Email integration (Gmail, Outlook)
- Project management (Asana, Notion)
- Note-taking (Obsidian, Roam)
- Calendar sync (Google Calendar, Outlook)
- Database queries (Supabase)

### Enhance Memory
- Integrate MemAPI Graph for relationship mapping
- Add context caching for faster responses
- Implement automatic memory summarization

---

## 🔐 Security & Privacy

- **API Keys**: Stored securely in environment variables
- **Memory**: User-specific, isolated storage
- **Webhooks**: HTTPS-only communication
- **Data**: Not shared between users
- **Retention**: Controlled by Mem0 settings

---

## 📞 Example Conversations

### Morning Check-in
**You**: "Good morning Pepper, what's on my plate today?"  
**Pepper**: "Good morning! Let me check your calendar and memory. You have three meetings scheduled, and yesterday you mentioned wanting to finish the project proposal. Should we break that down into steps before your first meeting at 10am?"

### Task Overwhelm
**You**: "I need to organize this entire project but I don't know where to start."  
**Pepper**: "I hear you - that can feel overwhelming. Let me break this down into manageable pieces. First, let's identify the main components of the project. Can you tell me what the end goal looks like?"

### Research Request
**You**: "Can you research the best productivity methods for ADHD?"  
**Pepper**: "Absolutely! Let me search for the latest research on ADHD productivity strategies." *[searches web]* "I found several evidence-based approaches. The most recommended are: time-blocking, body doubling, and the Pomodoro technique adapted for ADHD. Would you like me to break down how to implement any of these?"

### Memory Recall
**You**: "What did I say about my meeting preferences?"  
**Pepper**: *[searches memory]* "You mentioned that you prefer morning meetings when your focus is strongest, you like to have agendas sent at least a day in advance, and you need 15-minute buffers between meetings to process and transition. Should I help you restructure any upcoming meetings based on these preferences?"

---

## 🚨 Troubleshooting

### Agent Not Responding to Tool Calls
- Check that the webhook server is running: `curl https://5000-i56c1e9ksjn5gfk546mv5-247ad190.manusvm.computer/health`
- Verify API keys are set correctly
- Check tool server logs: `tail -f /home/ubuntu/tool_server.log`

### Memory Not Persisting
- Verify Mem0 API key is valid
- Check that user_id is being passed correctly
- Test memory endpoint: `curl -X POST https://5000-i56c1e9ksjn5gfk546mv5-247ad190.manusvm.computer/test/memory`

### Voice Quality Issues
- Check Cartesia API key
- Verify network latency
- Consider switching voice model if needed

---

## 📈 Next Steps

### Immediate Enhancements
1. **Supabase Integration**: Set up database for structured data storage
2. **Calendar Sync**: Connect to Google Calendar or Outlook
3. **MemAPI Graph**: Implement graph-based memory for relationship mapping
4. **Context Caching**: Use Anthropic's prompt caching for faster responses

### Long-term Improvements
1. **Email Integration**: Read and send emails
2. **Project Management**: Sync with Asana, Notion, or Linear
3. **Habit Tracking**: Monitor and encourage positive habits
4. **Analytics Dashboard**: Track productivity patterns and insights
5. **Multi-modal Support**: Add image and document analysis

---

## 📚 Resources

- **VAPI Documentation**: https://docs.vapi.ai
- **Mem0 Documentation**: https://docs.mem0.ai
- **Anthropic Claude**: https://docs.anthropic.com
- **Cartesia Voice**: https://cartesia.ai

---

## 💡 Tips for Best Results

1. **Be Specific**: The more context you provide, the better Pepper can help
2. **Use Memory**: Ask Pepper to remember important preferences and information
3. **Break Down Tasks**: Don't hesitate to ask for help breaking down overwhelming tasks
4. **Provide Feedback**: Tell Pepper what's working and what's not - she adapts
5. **Regular Check-ins**: Daily or weekly check-ins help maintain momentum

---

## 🎉 You're All Set!

Your Pepper Potts Chief of Staff is ready to help you stay organized, focused, and productive. She remembers everything, searches the web, writes documents, breaks down tasks, and provides the strategic support you need.

**Start your first conversation and experience the difference!**

---

*Created with ❤️ for INFJ ADHD combined type productivity and wellbeing*
