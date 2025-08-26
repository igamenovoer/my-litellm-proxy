#!/usr/bin/env python3
"""
LiteLLM Proxy Server
A proxy server for channeling 3rd party LLM APIs to coding clients.
"""

import os
import json
import argparse
import asyncio
from pathlib import Path
from typing import Optional

import uvicorn
from dotenv import load_dotenv
from litellm import proxy

# Load environment variables from .secret-env.env if it exists
env_file = Path(".secret-env.env")
if env_file.exists():
    load_dotenv(env_file)


def load_config(config_path: str = ".secret-config.json") -> Optional[dict]:
    """Load configuration from JSON file."""
    config_file = Path(config_path)
    if not config_file.exists():
        print(f"Warning: Configuration file {config_path} not found.")
        print("Using environment variables and default settings.")
        return None
    
    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            config = json.load(f)
        print(f"Loaded configuration from {config_path}")
        return config
    except Exception as e:
        print(f"Error loading configuration: {e}")
        return None


def setup_proxy(config: Optional[dict] = None, debug: bool = False):
    """Setup and configure the LiteLLM proxy."""
    
    # Set debug mode if requested
    if debug:
        os.environ["LITELLM_LOG"] = "DEBUG"
        os.environ["LITELLM_SET_VERBOSE"] = "true"
    
    # Load configuration if provided
    if config:
        # Set model list
        if "model_list" in config:
            proxy.model_list = config["model_list"]
        
        # Set general settings
        if "general_settings" in config:
            general = config["general_settings"]
            if "master_key" in general:
                proxy.master_key = general["master_key"]
            if "database_url" in general:
                proxy.prisma_client = general["database_url"]
        
        # Set router settings
        if "router_settings" in config:
            router = config["router_settings"]
            for key, value in router.items():
                setattr(proxy, key, value)
        
        # Set LiteLLM settings
        if "litellm_settings" in config:
            litellm_settings = config["litellm_settings"]
            for key, value in litellm_settings.items():
                os.environ[f"LITELLM_{key.upper()}"] = str(value)
    
    return proxy.app


def main():
    """Main function to start the proxy server."""
    parser = argparse.ArgumentParser(description="LiteLLM Proxy Server")
    parser.add_argument(
        "--config",
        default=".secret-config.json",
        help="Path to configuration file (default: .secret-config.json)"
    )
    parser.add_argument(
        "--host",
        default=os.getenv("LITELLM_PROXY_HOST", "127.0.0.1"),
        help="Host to bind the server to (default: 127.0.0.1)"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=int(os.getenv("LITELLM_PROXY_PORT", "8000")),
        help="Port to bind the server to (default: 8000)"
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug mode"
    )
    parser.add_argument(
        "--reload",
        action="store_true",
        help="Enable auto-reload for development"
    )
    
    args = parser.parse_args()
    
    # Load configuration
    config = load_config(args.config)
    
    # Setup proxy
    app = setup_proxy(config, args.debug)
    
    print(f"Starting LiteLLM Proxy Server on {args.host}:{args.port}")
    print(f"Debug mode: {args.debug}")
    print(f"Auto-reload: {args.reload}")
    print(f"API endpoint: http://{args.host}:{args.port}")
    print(f"Health check: http://{args.host}:{args.port}/health")
    print(f"OpenAI-compatible endpoint: http://{args.host}:{args.port}/v1")
    
    # Start the server
    uvicorn.run(
        app,
        host=args.host,
        port=args.port,
        reload=args.reload,
        log_level="debug" if args.debug else "info"
    )


if __name__ == "__main__":
    main()
