#!/usr//bin/env bash
# Entrypoint runs Gunicorn, then runs App1.

HOST=${HOST:-127.0.0.1}
PORT=${PORT:-8080}

if [ -d venv ]
then
	source venv/bin/activate
fi

exec gunicorn app1:app --bind=$HOST:$PORT
