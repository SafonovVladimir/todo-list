from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Worker(AbstractUser):
    class Meta:
        verbose_name = "worker"
        verbose_name_plural = "workers"

    def __str__(self):
        return (
            f"{self.username} "
            f"({self.first_name} {self.last_name})"
        )

    def get_absolute_url(self):
        return reverse("todo_list:worker-detail", kwargs={"pk": self.pk})


class Task(models.Model):
    name = models.CharField(max_length=63)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField()
    tags = models.ManyToManyField("Tag", related_name="tasks")

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.content


class Tag(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name
