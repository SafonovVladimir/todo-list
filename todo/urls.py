from django.urls import path

from todo.views import (
    index,
    TaskListView,
    TaskCreateView,
    TaskDetailView,
    TaskUpdateView,
    TaskDeleteView,
    toggle_complete_task,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    TagDetailView,
    WorkerDeleteView,
    WorkerDetailView,
    WorkerCreateView,
)

urlpatterns = [
    path("", index, name="index"),

    path("worker/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("worker/create/", WorkerCreateView.as_view(), name="worker-create"),
    path(
        "worker/<int:pk>/delete/",
        WorkerDeleteView.as_view(),
        name="worker-delete",
    ),

    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path(
        "tasks/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path("tasks/<int:pk>/toggle_complete/",
         toggle_complete_task,
         name="toggle-complete-task"
         ),

    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/", TagDetailView.as_view(), name="tag-detail"),
    path("tags/<int:pk>/update/",
         TagUpdateView.as_view(),
         name="tag-update"
         ),
    path("tags/<int:pk>/delete/",
         TagDeleteView.as_view(),
         name="tag-delete"
         ),
]

app_name = "todo_list"
