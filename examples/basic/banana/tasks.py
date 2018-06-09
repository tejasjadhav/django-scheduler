from celery import shared_task
from scheduler.tasks import RepeatTask


@shared_task(base=RepeatTask)
def say_hello(fruit):
    print(f'Hello, I ate {fruit} today.')
