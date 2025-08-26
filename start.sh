#!/bin/bash

# LiteLLM Proxy Startup Script

echo "=== LiteLLM Proxy Setup ==="

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Check if configuration files exist
if [ ! -f ".secret-config.json" ]; then
    echo "Warning: .secret-config.json not found!"
    echo "Please copy .secret-config.json.example to .secret-config.json and configure it."
fi

if [ ! -f ".secret-env.env" ]; then
    echo "Warning: .secret-env.env not found!"
    echo "Please copy .secret-env.env.example to .secret-env.env and configure it."
fi

# Start the proxy server
echo "Starting LiteLLM Proxy Server..."
python proxy_server.py "$@"
