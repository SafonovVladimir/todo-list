from django.test import TestCase
from django.urls import reverse

from todo.models import Task, Tag

TASK_URL = reverse("todo_list:task-list")
TAG_URL = reverse("todo_list:tag-list")


class PublicTaskTests(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            name="New functional",
            content="Add new functional to index page with buttons",
            deadline="2023-04-04 15:00:00",
            status=True,
        )

    def test_login_required(self):
        res = self.client.get(TASK_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_tag_list(self):
        response = self.client.get(reverse("todo_list:task-list"))
        self.assertNotEqual(response.status_code, 200)

    def test_tag_create(self):
        response = self.client.get(reverse("todo_list:task-create"))
        self.assertNotEqual(response.status_code, 200)

    def test_tag_update(self):
        response = self.client.get(reverse(
            "todo_list:task-update",
            args=[self.task.pk]
        ))
        self.assertNotEqual(response.status_code, 200)

    def test_tag_delete(self):
        response = self.client.get(reverse(
            "todo_list:task-delete",
            args=[self.task.pk]
        ))
        self.assertNotEqual(response.status_code, 200)


class PublicTagTests(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="#bug")

    def test_login_required(self):
        res = self.client.get(TAG_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_tag_list(self):
        response = self.client.get(reverse("todo_list:tag-list"))
        self.assertNotEqual(response.status_code, 200)

    def test_tag_create(self):
        response = self.client.get(reverse("todo_list:tag-create"))
        self.assertNotEqual(response.status_code, 200)

    def test_tag_update(self):
        response = self.client.get(reverse(
            "todo_list:tag-update",
            args=[self.tag.pk]
        ))
        self.assertNotEqual(response.status_code, 200)

    def test_tag_delete(self):
        response = self.client.get(reverse(
            "todo_list:tag-delete",
            args=[self.tag.pk]
        ))
        self.assertNotEqual(response.status_code, 200)
