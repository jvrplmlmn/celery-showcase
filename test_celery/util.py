__all__ = [
    'chain_parents',
    'chain_children',
    'list_of_task_ids_in_a_chain_workflow',
    'print_celery'
]

def chain_parents(node):
    """
    :param node: A celery.result.AsyncResult object.
    :return: A celery.result.AsyncResult generator with all the referenced parents
     of the original celery.result.AsyncResult object.
    This is only working with 'chain' canvas:
    http://docs.celeryproject.org/en/latest/userguide/canvas.html#chains
    """
    while node.parent:
        yield node
        node = node.parent
    yield node


def chain_children(node):
    """
    :param node: A celery.result.AsyncResult object.
    :return: A celery.result.AsyncResult generator with all the referenced children
     of the original celery.result.AsyncResult object.
    This is only working with 'chain' canvas:
    http://docs.celeryproject.org/en/latest/userguide/canvas.html#chains
    """
    while node.children:
        yield node
        node = node.children
    yield node

def list_of_task_ids_in_a_chain_workflow(res):
    """
    :param res: A celery.result.AsyncResult object
    :return: A list that contains the task_ids of all the parent tasks of the given AsyncResult.
     The returned list has the same order as the tasks that were involved in the chain workflow.
    """
    return list(reversed([t.id for t in chain_parents(res)]))

def print_celery(res):
    l = list_of_task_ids_in_a_chain_workflow(res)
    if l is not None:
        print('-' * 60)
    for idx, e in enumerate(l, start=1):
        print('\t {} --> {}'.format(idx, e))
