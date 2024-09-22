from django.db import models
from contacts.models import Contact
from datetime import date


# Choises for priority
URGENT = 'urgent'
MEDIUM = 'medium'
LOW = 'low'

# Choises for status
TD = 'toDo'
IP = 'inProgress'
AF = 'awaitFeedback'
DN = 'done'

#Choises for category
TECHNICAL_TASK = 'Technical Task'
USER_STORY = 'User Story'

PRIORITY_CHOISES = [(URGENT, 'urgent'), (MEDIUM, 'medium'), (LOW, 'low') ]
STATUS_CHOISES = [(TD, 'toDo'), (IP, 'inProgress'), (AF, 'awaitFeedback') ,(DN, 'done') ]
CATEGORY_CHOISES =[(TECHNICAL_TASK, 'Technical Task'), (USER_STORY, 'User Story')]


class TaskItem(models.Model):
    title = models.CharField(max_length=30, default='')
    description = models.CharField(max_length=100, default='')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOISES, default=MEDIUM)
    status = models.CharField(max_length=13, choices=STATUS_CHOISES, default=TD)
    contacts = models.ManyToManyField(Contact, blank=True)
    due_date = models.DateField(default=date.today, editable=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOISES, default=None)

class SubtaskItem(models.Model):
     title = models.CharField(max_length=30, blank=False)
     checked = models.BooleanField(default=False)
     rel_task = models.ForeignKey(TaskItem, on_delete=models.CASCADE, related_name='subtask_item_set')

