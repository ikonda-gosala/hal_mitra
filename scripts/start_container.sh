#!/bin/bash
set -e

# Pull the Docker image from Docker Hub
docker pull konda33/hal_mitra_aws_code_build:latest

# Run the Docker image as a container
docker run -d -p 5000:5000 konda33/hal_mitra_aws_code_build:latest
