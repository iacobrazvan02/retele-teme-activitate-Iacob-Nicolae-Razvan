cd "$(dirname "$0")"
osascript -e 'tell app "Terminal" to do script "cd '"$(pwd)"' && python3 server.py"'
sleep 1
osascript -e 'tell app "Terminal" to do script "cd '"$(pwd)"' && python3 client.py"'
osascript -e 'tell app "Terminal" to do script "cd '"$(pwd)"' && python3 client.py"'
osascript -e 'tell app "Terminal" to do script "cd '"$(pwd)"' && python3 client.py"'