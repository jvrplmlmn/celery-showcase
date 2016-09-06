from .tasks import *
from .util import *

def main():
    async_result_dummy = workflow_chain_dummy()
    print_celery(async_result_dummy)

    async_result_passing = workflow_chain_passing_id()
    print_celery(async_result_passing)


if __name__ == '__main__':
   main()
