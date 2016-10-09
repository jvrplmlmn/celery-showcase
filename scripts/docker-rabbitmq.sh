#!/bin/bash

docker run -e RABBITMQ_PASS=guest -e RABBITMQ_USER=guest -p 5672:5672 -p 15672:15672 rabbitmq:management
