from celery import shared_task
import time


@shared_task
def execute_something():
    for x in range(10):
        print(x)
        time.sleep(1)
    return 'done'