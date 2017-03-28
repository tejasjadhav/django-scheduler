from datetime import timedelta

from celery import Celery
from django.test import TestCase
from django.utils import timezone

from scheduler.models import (
    ScheduledTask,
    ScheduledTaskRunLog
)
from scheduler.scheduler import TaskScheduler
from scheduler.tasks import RepeatTask


app = Celery()
app.conf.task_always_eager = True
app.conf.task_eager_propagates = True

@app.task(bind=True, base=RepeatTask)
def test_task(*args, **kwargs):
    return {
        'args': args,
        'kwargs': kwargs,
    }


class SchedulerTestCase(TestCase):
    def setUp(self):
        self.valid_args = (
            1,
            'string',
            True,
            None,
            [2, 3, 4],
            {'a': 'Apple', 'b': 'Banana'}
        )

        self.valid_kwargs = {
            'c': 1,
            'd': 'Dog',
            'e': False,
            'f': None,
            'g': [5, 6, 7],
            'h': {'i': 'Ice', 'j': 'Jackal'}
        }

        self.valid_rrule = 'RRULE:FREQ=SECONDLY;COUNT=10'
        self.valid_trigger_at = timezone.now()
        self.valid_until = timezone.now() + timedelta(hours=1)

    def test_task_creation(self):
        task_id = TaskScheduler.schedule(
            func=test_task,
            description='Test task',
            args=self.valid_args,
            kwargs=self.valid_kwargs,
            rrule_string=self.valid_rrule,
            trigger_at=self.valid_trigger_at,
            until=self.valid_until
        )

        scheduled_task = ScheduledTask.objects.get(pk=task_id)
        run_count = ScheduledTaskRunLog.objects.filter(
            scheduled_task=scheduled_task).count()

        self.assertEqual(run_count, 10)
