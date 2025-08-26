# My LiteLLM Proxy

A LiteLLM proxy server for channeling 3rd party LLM APIs to coding clients like Claude Code, Gemini CLI, Cline, Roo Code, and other AI-powered development tools.

## Overview

This project sets up a [LiteLLM](https://github.com/BerriAI/litellm) proxy server that acts as a unified interface for multiple LLM providers. It allows you to use various AI models from different providers through a single OpenAI-compatible API endpoint.

## Features

- **Universal API Interface**: OpenAI-compatible API for all supported LLM providers
- **Multiple Provider Support**: Supports OpenAI, Anthropic, Google, Cohere, Azure, AWS Bedrock, and many more
- **Load Balancing**: Distribute requests across multiple models/providers
- **Cost Tracking**: Monitor usage and costs across different providers
- **Rate Limiting**: Control API usage and prevent quota exhaustion
- **Caching**: Reduce costs and improve response times with intelligent caching
- **Authentication**: Secure your proxy with API keys and user management

## Supported Coding Clients

This proxy is designed to work seamlessly with popular AI coding tools:

- **Claude Code** (VS Code Extension)
- **Gemini CLI**
- **Cline** (formerly Claude Dev)
- **Roo Code**
- **Cursor IDE**
- **GitHub Copilot alternatives**
- **Any OpenAI API-compatible client**

## Quick Start

### Prerequisites

- Python 3.8+
- pip or conda
- API keys for your chosen LLM providers

### Installation

1. Clone this repository:
`ash
git clone https://github.com/igamenovoer/my-litellm-proxy.git
cd my-litellm-proxy
`

2. Install dependencies:
`ash
pip install -r requirements.txt
`

3. Configure your API keys and settings:
`ash
cp .secret-config.json.example .secret-config.json
cp .secret-env.env.example .secret-env.env
`

4. Edit the configuration files with your API keys and preferences.

5. Start the proxy server:
`ash
python proxy_server.py
`

The proxy will be available at http://localhost:8000 by default.

## Configuration

### API Keys and Credentials

Store your sensitive configuration in the following files (these are gitignored):

- **.secret-config.json**: JSON configuration with API keys, model mappings, and provider settings
- **.secret-env.env**: Environment variables for additional credentials and URLs

### Example Configuration

See the example files for configuration templates:
- .secret-config.json.example
- .secret-env.env.example

## Usage with Coding Clients

### Claude Code (VS Code)

1. Install the Claude Code extension
2. Set the API endpoint to your proxy: http://localhost:8000
3. Use your proxy API key for authentication

### Gemini CLI

`ash
export OPENAI_API_BASE=http://localhost:8000/v1
export OPENAI_API_KEY=your-proxy-api-key
gemini-cli "Your prompt here"
`

### Cline

1. Configure Cline to use custom OpenAI endpoint
2. Set base URL: http://localhost:8000
3. Use your proxy API key

## Supported Providers

- OpenAI (GPT-3.5, GPT-4, GPT-4 Turbo)
- Anthropic (Claude 2, Claude 3, Claude 3.5)
- Google (Gemini Pro, Gemini Ultra)
- Cohere
- Azure OpenAI
- AWS Bedrock
- Hugging Face
- Ollama (local models)
- And many more...

## Features

### Load Balancing

Configure multiple models for the same endpoint to distribute load and improve reliability.

### Cost Tracking

Monitor your usage and costs across different providers with built-in analytics.

### Rate Limiting

Protect your API quotas with configurable rate limiting per user/model.

### Caching

Reduce costs and improve performance with intelligent response caching.

## Development

### Running in Development Mode

`ash
python proxy_server.py --debug
`

### Testing

`ash
python -m pytest tests/
`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Security

- Never commit API keys or sensitive credentials
- Use the provided .secret-* files for sensitive configuration
- Consider using environment variables in production
- Implement proper authentication for production deployments

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- [LiteLLM Documentation](https://docs.litellm.ai/)
- [GitHub Issues](https://github.com/igamenovoer/my-litellm-proxy/issues)
- [Discussions](https://github.com/igamenovoer/my-litellm-proxy/discussions)

## Acknowledgments

- [LiteLLM](https://github.com/BerriAI/litellm) - The amazing library that makes this proxy possible
- All the AI model providers for their APIs
- The open-source community for the coding tools this proxy supports
