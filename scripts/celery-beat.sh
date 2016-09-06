#!/bin/bash

celery -A test_celery beat --loglevel=info
