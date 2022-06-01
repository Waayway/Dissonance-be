#!/bin/bash

# Load Env files

if [ -f .env ]
then
  export $(cat .env | sed 's/#.*//g' | xargs)
fi

# Start green testing
green test


