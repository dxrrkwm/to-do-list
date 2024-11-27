from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy

from app.forms import TagForm, TaskForm
from app.models import Task, Tag


class IndexView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags").order_by("-datetime")
    template_name = "index.html"
    context_object_name = "tasks"


class CreateTaskView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("app:task_list")


class UpdateTaskView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("app:task_list")


class DeleteTaskView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("app:task_list")


class TagListView(generic.ListView):
    model = Tag


class CreateTagView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("app:tag_list")


class UpdateTagView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("app:tag_list")


class DeleteTagView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("app:tag_list")


def do_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect("/")
