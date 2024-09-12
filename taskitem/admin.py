from django.contrib import admin

from taskitem.models import TaskItem, Subtask_item

# Register your models here.
admin.site.register(TaskItem)
admin.site.register(Subtask_item)
