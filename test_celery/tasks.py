from __future__ import absolute_import
from celery.utils.log import get_task_logger
from celery.canvas import chain
from test_celery.celery import app

LOG = get_task_logger(__name__)


__all__ = [
    'add',
    'workflow_chain_dummy',
    'workflow_chain_passing_id'
]


@app.task
def add(x, y):
    return x + y


@app.task(bind=True, acks_late=True)
def first_task(self):
    print('First task of the workflow')
    LOG.info('Logging a message for #1')


@app.task(bind=True, acks_late=True)
def second_task(self):
    print('Second task of the workflow')
    LOG.info('Logging a message for #2')


def workflow_chain_dummy():
    """ I do shit """

    return chain(
        first_task.si(),
        second_task.si()
    ).delay()


@app.task(bind=True, acks_late=True)
def more_task_one(self, more):
    print('--> more_task_one {}'.format(more))
    LOG.info('--> more_task_one {}'.format(more))
    return more


@app.task(bind=True, acks_late=True)
def more_task_two(self, more):
    print('--> more_task_two {}'.format(more))
    LOG.info('--> more_task_two {}'.format(more))
    return more


def workflow_chain_passing_id():
    return chain(
        more_task_one.s('42'),
        more_task_one.s()
    ).delay()
