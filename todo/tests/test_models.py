from django.contrib.auth import get_user_model
from django.test import TestCase

from todo.models import Task, Tag


class ModelTests(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="#bug")
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin12345",
        )
        self.client.force_login(self.admin_user)
        self.task = Task.objects.create(
            name="New functional",
            content="Add new functional to index page with buttons",
            deadline="2023-04-04 15:00:00",
            status=True,
        )

    def test_task_str(self):
        self.assertEqual(str(self.task), f"{self.task.name}")

    def test_worker_str(self):
        self.assertEqual(
            str(self.admin_user),
            f"{self.admin_user.username} "
            f"({self.admin_user.first_name} {self.admin_user.last_name})"
        )

    def test_create_worker(self):
        self.assertEqual(self.admin_user.username, "admin")
        self.assertTrue(self.admin_user.check_password("admin12345"))
