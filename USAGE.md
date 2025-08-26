# Example Usage Guide

## Quick Test Setup

1. **Copy example files:**
`ash
cp .secret-config.json.example .secret-config.json
cp .secret-env.env.example .secret-env.env
`

2. **Edit .secret-config.json** and replace the placeholder API keys:
   - YOUR_OPENAI_API_KEY_HERE → Your actual OpenAI API key
   - YOUR_ANTHROPIC_API_KEY_HERE → Your actual Anthropic API key
   - YOUR_GOOGLE_API_KEY_HERE → Your actual Google API key
   - your-proxy-master-key-here → A secure master key for your proxy

3. **Start the server:**
`ash
python proxy_server.py
`

## Testing the Proxy

### Using curl:
`ash
# Test health endpoint
curl http://localhost:8000/health

# Test chat completion
curl -X POST http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-proxy-master-key-here" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
`

### Using with coding clients:

#### Claude Code (VS Code):
1. Install Claude Code extension
2. Set API endpoint: http://localhost:8000
3. API key: your-proxy-master-key-here

#### Cline:
1. Choose "Use OpenAI API"
2. API Key: your-proxy-master-key-here
3. Base URL: http://localhost:8000

#### Cursor IDE:
1. Go to Settings → Models
2. Add custom model
3. API Key: your-proxy-master-key-here
4. Base URL: http://localhost:8000

## Available Models

Based on the default configuration, these models are available:
- gpt-4-turbo (OpenAI GPT-4 Turbo)
- gpt-3.5-turbo (OpenAI GPT-3.5 Turbo)
- claude-3-5-sonnet (Anthropic Claude 3.5 Sonnet)
- claude-3-haiku (Anthropic Claude 3 Haiku)
- gemini-pro (Google Gemini Pro)
- gemini-1.5-pro (Google Gemini 1.5 Pro)
