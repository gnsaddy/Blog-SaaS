#!/bin/bash

# code to push docker image to AWS ECR
# https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html

echo "Building Codejee MS prod image"
# login to aws ecr and push image to aws ecr
aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 923411774909.dkr.ecr.us-east-2.amazonaws.com
# build the image
docker build -t codejee_ms . --no-cache

# tag the image
docker tag codejee_ms:latest 923411774909.dkr.ecr.us-east-2.amazonaws.com/codejee_ms:latest

# push the image to the registry
docker push 923411774909.dkr.ecr.us-east-2.amazonaws.com/codejee_ms:latest

echo "removing untagged images from ECR"
ECR_REGION=us-east-2
ECR_REPO=codejee_ms
# remove untagged images from ECR
IMAGES_TO_DELETE=$(aws ecr list-images --region $ECR_REGION --repository-name $ECR_REPO --filter "tagStatus=UNTAGGED" --query 'imageIds[*]' --output json)

aws ecr batch-delete-image --region $ECR_REGION --repository-name $ECR_REPO --image-ids "$IMAGES_TO_DELETE" || true
