# Generated by Django 5.1 on 2024-09-17 19:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskitem', '0003_alter_taskitem_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtaskitem',
            name='rel_task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtask_item_set', to='taskitem.taskitem'),
        ),
    ]
