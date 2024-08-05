TEMPLATES_AUTO_RELOAD=True

build-docker:
	docker build -t defe .
docker:
	docker run -p 8080:8080 defe