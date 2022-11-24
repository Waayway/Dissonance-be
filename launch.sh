#!/bin/bash
# Clear the screen
clear

# Load Env files

if [ -f .env ]
then
  export $(cat .env | sed 's/#.*//g' | xargs)
fi

# Start API, fastapi/uvicorn
python app.py


