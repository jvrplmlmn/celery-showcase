from test_celery import tasks, util


def main():
    async_result_dummy = tasks.workflow_chain_dummy()
    util.print_celery(async_result_dummy)

    async_result_passing = tasks.workflow_chain_passing_id()
    util.print_celery(async_result_passing)


if __name__ == '__main__':
    main()
