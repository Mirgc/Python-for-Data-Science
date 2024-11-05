# Variables
IMAGE_NAME = python3

# Default target (build and run)
.PHONY: all
all: build run

# Build the Docker image
.PHONY: build
build:
	docker build -t $(IMAGE_NAME) .

# Run the Docker container
.PHONY: run
run:
	docker run $(IMAGE_NAME) 14
	docker run $(IMAGE_NAME) -5
	docker run $(IMAGE_NAME) 0
	docker run $(IMAGE_NAME)
	docker run $(IMAGE_NAME) Hi!
	docker run $(IMAGE_NAME) 3.14
	docker run $(IMAGE_NAME) 13 5

# Stop the running Docker container
.PHONY: stop
stop:
	docker stop $(CONTAINER_NAME)

# Remove the Docker container
.PHONY: remove
remove:
	docker rm $(CONTAINER_NAME)

# Clean up: stop and remove the container
.PHONY: clean
clean: stop remove

# Rebuild the image and restart the container
.PHONY: restart
restart: clean build run

# Show logs from the container
.PHONY: logs
logs:
	docker logs -f $(CONTAINER_NAME)

# Enter the container shell (useful for debugging)
.PHONY: exec
exec:
	docker exec -it $(CONTAINER_NAME) /bin/sh