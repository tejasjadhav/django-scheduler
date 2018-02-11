from __future__ import unicode_literals

from uuid import uuid4

from django.db import models


class ScheduledTask(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    function_name = models.CharField(max_length=1000)
    description = models.TextField(blank=True, null=True)

    args = models.TextField(blank=True, null=True)
    kwargs = models.TextField(blank=True, null=True)
    rrule = models.TextField(blank=True, null=True)

    STATUS_CREATED = 'created'
    STATUS_RUNNING = 'running'
    STATUS_SUCCESS = 'success'
    STATUS_FAILURE = 'failure'
    STATUS_CANCELLED = 'cancelled'
    STATUS_CHOICES = (
        (STATUS_CREATED, 'Created'),
        (STATUS_RUNNING, 'Running'),
        (STATUS_SUCCESS, 'Success'),
        (STATUS_FAILURE, 'Failure'),
        (STATUS_CANCELLED, 'Cancelled'),
    )

    status = models.CharField(max_length=255, choices=STATUS_CHOICES,
                              default=STATUS_CREATED)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.function_name

    def __str__(self):
        return self.function_name

    def save_status(self, status):
        """Sets and saves the status to the scheduled task.

        Arguments:
            status (str): Status.

        Returns:
            ScheduledTask: Current scheduled task instance.
        """
        self.status = status
        self.save(update_fields=('status', ))
        return self


class ScheduledTaskRunLog(models.Model):
    task_id = models.UUIDField()
    scheduled_task = models.ForeignKey(ScheduledTask, on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.task_id)

    def __str__(self):
        return str(self.task_id)


models.deletion.PROTECT
