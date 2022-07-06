from django.db import models


class Articles(models.Model):
    title = models.CharField(max_length=40)
    content = models.CharField(max_length=1024)
    dateOfCreation = models.DateTimeField()
    isArchive = models.BooleanField(default=False)