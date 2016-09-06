#!/bin/bash

celery -A test_celery worker --loglevel=info --autoreload --purge
