from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from todo.models import Task, Tag, Worker

admin.site.unregister(Group)


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                    )
                },
            ),
        )
    )


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "content",
        "created_at",
        "deadline",
        "status",
    )
    search_fields = ("name", "content", "deadline",)
    list_filter = ("name", "content", "deadline", "status",)


admin.site.register(Tag)
