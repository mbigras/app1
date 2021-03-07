help:
	@echo "App1 is a small flask app for experimentation."
	@echo ""
	@echo "The following are common commands for this project:"
	@echo ""
	@echo "make build"
	@echo "make run"
	@echo "curl localhost:8080"

build:
	docker build -t app1 .

run: build
	docker run -it -p 8080:8080 app1

deps:
	pip install -r requirements.txt -r requirements-dev.txt

format:
	black *.py
