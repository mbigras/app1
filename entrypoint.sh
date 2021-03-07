#!/usr//bin/env bash

PORT=${PORT:-8080}

echo "Starting app1 listening on port $PORT"
exec gunicorn app1:app --bind=0.0.0.0:$PORT
