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
	docker run $(IMAGE_NAME) "Hello the World" 4
	docker run $(IMAGE_NAME) "Hello the World" 99
	docker run $(IMAGE_NAME) 3 "Hello the World"
	docker run $(IMAGE_NAME) 

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