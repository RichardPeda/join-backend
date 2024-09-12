from django.db import models
from contacts.models import Contact


# Choises for priority
URGENT = 'URG'
MEDIUM = 'MED'
LOW = 'LOW'

# Choises for status
TD = 'TODO'
IP = 'INPROGRESS'
AF = 'AWAITFEEDBACK'
DN = 'DONE'

PRIORITY_CHOISES = [(URGENT, 'urgent'), (MEDIUM, 'medium'), (LOW, 'low') ]
STATUS_CHOISES = [(TD, 'Todo'), (IP, 'inProgress'), (AF, 'awaitFeedback') ,(DN, 'done') ]


class TaskItem(models.Model):
    title = models.CharField(max_length=30, default='')
    description = models.CharField(max_length=100, default='')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOISES, default=MEDIUM)
    status = models.CharField(max_length=13, choices=STATUS_CHOISES, default=TD)
    contacts = models.ManyToManyField(Contact, blank=True)

class Subtask_item(models.Model):
     title = models.CharField(max_length=30, blank=False)
     checked = models.BooleanField(default=False)
     rel_task = models.ForeignKey(TaskItem, on_delete=models.CASCADE)

