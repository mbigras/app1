#!/usr//bin/env bash
# Entrypoint enters Python virtual environment, runs Gunicorn, then runs App1.

PORT=${PORT:-8080}

if [ -d venv ]
then
	source venv/bin/activate
fi

exec gunicorn app1:app --bind=0.0.0.0:$PORT
