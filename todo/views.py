from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo.forms import TaskNameSearchForm, TaskForm
from todo.models import Task, Tag


def index(request):
    """View function for the home page of the site."""
    queryset = Task.objects.all()
    num_tasks = queryset.count()
    num_finished_tasks = queryset.filter(
        status=True
    ).count()
    num_unfinished_tasks = queryset.filter(
        status=False
    ).count()

    context = {
        "num_tasks": num_tasks,
        "num_finished_tasks": num_finished_tasks,
        "num_unfinished_tasks": num_unfinished_tasks,
    }

    return render(request, "todo/index.html", context=context)


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    # template_name = "todo/task_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)

        content = self.request.GET.get("content", "")

        context["search_form"] = TaskNameSearchForm(initial={
            "content": content,
        })

        return context

    def get_queryset(self):
        queryset = Task.objects.all()
        form = TaskNameSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                content__contains=form.cleaned_data["content"]
            )


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_list:task-list")


class TaskDetailView(generic.DetailView):
    model = Task


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_list:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo_list:task-list")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_list:tag-list")
