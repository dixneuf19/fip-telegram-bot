.PHONY: dev build run push release release-multi deploy

DOCKER_REPOSITERY=dixneuf19
IMAGE_NAME=fip-telegram-bot
IMAGE_TAG=$(shell git rev-parse HEAD)
DOCKER_IMAGE_PATH=$(DOCKER_REPOSITERY)/$(IMAGE_NAME):$(IMAGE_TAG)
APP_NAME=fip-telegram-bot
KUBE_NAMESPACE=fip
PLATFORMS="linux/amd64,linux/arm64"

dev:
	PYTHONPATH=. python fip_telegram_bot/main.py

format:
	black .

check-format:
	black --check .

test:
	PYTHONPATH=. pytest tests

build:
	docker build -t $(DOCKER_IMAGE_PATH) .

build-multi:
	docker buildx build --platform $(PLATFORMS) -t $(DOCKER_IMAGE_PATH) .

run: build
	docker run -p 8000:80 --env-file=.env $(DOCKER_IMAGE_PATH)

push:
	docker push $(DOCKER_IMAGE_PATH)

release: build push

release-multi:
	docker buildx build --platform $(PLATFORMS) -t $(DOCKER_IMAGE_PATH) . --push

deploy:
	kubectl apply -f $(APP_NAME).yaml

secret:
	kubectl create secret generic fip-telegram-bot --from-env-file=.env	

kube-credentials:
	NAMESPACE=${KUBE_NAMESPACE} ./scripts/generate-kubeconfig.sh
