from django.contrib import admin

from taskitem.models import TaskItem, SubtaskItem
from users.serializers import User

# Register your models here.
admin.site.register(User)
admin.site.register(TaskItem)
admin.site.register(SubtaskItem)
