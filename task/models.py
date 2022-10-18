from django.db import models

# Create your models here.


class Task(models.Model):
    task_name = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name
