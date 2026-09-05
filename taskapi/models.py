from django.db import models

# Create your models here.
class TaskManager(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=False)
    status = models.BooleanField(default=False, choices= (True,False))


