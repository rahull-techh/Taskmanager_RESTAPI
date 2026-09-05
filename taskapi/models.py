from django.db import models

# Create your models here.
class TaskManager(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=False)
    completed = models.BooleanField(default=False)


