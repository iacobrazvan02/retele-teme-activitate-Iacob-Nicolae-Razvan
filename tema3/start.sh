#!/bin/bash
echo "Pornire FTP Server..."
osascript -e 'tell application "Terminal" to do script "cd \"'$(pwd)'\" && python3 server.py"'

sleep 2

echo "Pornire FTP Client..."
osascript -e 'tell application "Terminal" to do script "cd \"'$(pwd)'\" && python3 client.py"'

echo "Succes! Terminalele au fost deschise."