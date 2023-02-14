TEMPLATES_AUTO_RELOAD=True

build-docker:
	docker build -t defe .
docker:
	docker run -p 5000:5000 --name defe defe