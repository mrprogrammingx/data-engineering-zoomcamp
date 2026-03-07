#!/bin/bash
# Exit immediately if a command exits with a non-zero status
set -e

# Start the Flask app in the background
# We use 'python app.py' to match your directory structure
python app.py &

# Give the app a moment to start
sleep 2

exec /bin/bash