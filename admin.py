from django.contrib import admin

from .models import (
    ScheduledTask,
    ScheduledTaskRunLog
)


class ScheduledTaskRunLogTabularInline(admin.TabularInline):
    readonly_fields = [field.name
                       for field in ScheduledTaskRunLog._meta.fields
                       if field.name != 'id']
    ordering = ('created_at', )
    model = ScheduledTaskRunLog


@admin.register(ScheduledTask)
class ScheduledTaskModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ScheduledTask._meta.fields]
    inlines = (ScheduledTaskRunLogTabularInline, )
    ordering = ('-created_at', )
    model = ScheduledTask
