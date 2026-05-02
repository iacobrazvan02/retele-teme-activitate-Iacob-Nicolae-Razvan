#!/bin/bash
echo "Se opresc procesele Python..."
pkill -f "python3 server.py"
pkill -f "python3 client.py"
echo "Toate procesele au fost oprite."