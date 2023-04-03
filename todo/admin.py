from django.contrib import admin
from django.contrib.auth.models import Group

from todo.models import Task, Tag

admin.site.unregister(Group)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "content",
        "created_at",
        "deadline",
        "status",
    )
    search_fields = ("content", "deadline",)
    list_filter = ("content", "deadline", "status",)


admin.site.register(Tag)
