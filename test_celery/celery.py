from __future__ import absolute_import
from celery import Celery

app = Celery('test_celery',
             broker='amqp://guest@localhost//',
             backend='redis://',
             include=['test_celery.tasks'])
