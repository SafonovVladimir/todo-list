from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=63)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField()
    tags = models.ManyToManyField("Tag", related_name="tasks")

    def __str__(self):
        return self.content


class Tag(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name
