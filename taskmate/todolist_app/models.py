from django.db import models

# Create your models here.
class TaskList(models.Model):
    taskname = models.CharField(max_length=255)
    done=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.taskname}-{self.done}"
