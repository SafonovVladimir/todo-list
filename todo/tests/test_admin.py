from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin12345",
        )
        self.client.force_login(self.admin_user)

    def test_worker_listed(self):
        url = reverse("admin:todo_worker_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.admin_user.first_name)
        self.assertContains(res, self.admin_user.last_name)
