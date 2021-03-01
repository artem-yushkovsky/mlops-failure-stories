#!/bin/bash

cp favicon.png /var/www/k8s.af/workdir/

IMAGE=mlops-failure-stories
docker build -t $IMAGE .
docker run -d --name mlops-failure-stories -u $(id -u) -v /var/www/k8s.af/workdir:/workdir --restart=always $IMAGE
