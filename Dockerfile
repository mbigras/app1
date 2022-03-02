FROM python:3.10.2-alpine3.15
RUN apk add --no-cache bash
WORKDIR /app
RUN python -m venv venv \
	&& /app/venv/bin/pip install pip==22.0.3
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY app1.py entrypoint.sh ./
ENTRYPOINT ["/app/entrypoint.sh"]
