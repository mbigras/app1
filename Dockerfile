FROM python:3.11.1-bullseye

WORKDIR /app

COPY requirements-to-freeze.txt ./

RUN pip install -r requirements-to-freeze.txt

COPY app1.py entrypoint.sh ./

ENTRYPOINT ["/app/entrypoint.sh"]
