@echo off
echo === LiteLLM Proxy Setup ===

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt

REM Check if configuration files exist
if not exist ".secret-config.json" (
    echo Warning: .secret-config.json not found!
    echo Please copy .secret-config.json.example to .secret-config.json and configure it.
)

if not exist ".secret-env.env" (
    echo Warning: .secret-env.env not found!
    echo Please copy .secret-env.env.example to .secret-env.env and configure it.
)

REM Start the proxy server
echo Starting LiteLLM Proxy Server...
python proxy_server.py %*
