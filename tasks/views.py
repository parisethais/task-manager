from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views import View


from .models import Task
from .forms import TaskForm


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate_by = 10
    template_name = "tasks/task_list.html"
    context_object_name = "task_list"

    def get_queryset(self):
        queryset = Task.objects.select_related("task_type").prefetch_related("assignees")

        q = self.request.GET.get("q", "").strip()
        status = self.request.GET.get("status", "")
        priority = self.request.GET.get("priority", "")

        if q:
            queryset = queryset.filter(
                Q(name__icontains=q) | Q(description__icontains=q)
            )

        if status == "open":
            queryset = queryset.filter(is_completed=False)
        elif status == "completed":
            queryset = queryset.filter(is_completed=True)

        if priority in ["low", "medium", "high", "urgent"]:
            queryset = queryset.filter(priority=priority)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        context["total_tasks"] = queryset.count()
        context["open_tasks"] = queryset.filter(is_completed=False).count()
        context["completed_tasks"] = queryset.filter(is_completed=True).count()
        context["search_query"] = self.request.GET.get("q", "").strip()
        context["status_filter"] = self.request.GET.get("status", "")
        context["priority_filter"] = self.request.GET.get("priority", "")
        return context


class MyTaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate_by = 10
    template_name = "tasks/my_task_list.html"
    context_object_name = "task_list"

    def get_queryset(self):
        queryset = (
            Task.objects
            .select_related("task_type")
            .prefetch_related("assignees")
            .filter(assignees=self.request.user)
        )

        q = self.request.GET.get("q", "").strip()
        status = self.request.GET.get("status", "")
        priority = self.request.GET.get("priority", "")

        if q:
            queryset = queryset.filter(
                Q(name__icontains=q) | Q(description__icontains=q)
            )

        if status == "open":
            queryset = queryset.filter(is_completed=False)
        elif status == "completed":
            queryset = queryset.filter(is_completed=True)

        if priority in ["low", "medium", "high", "urgent"]:
            queryset = queryset.filter(priority=priority)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        context["total_tasks"] = queryset.count()
        context["open_tasks"] = queryset.filter(is_completed=False).count()
        context["completed_tasks"] = queryset.filter(is_completed=True).count()
        context["search_query"] = self.request.GET.get("q", "").strip()
        context["status_filter"] = self.request.GET.get("status", "")
        context["priority_filter"] = self.request.GET.get("priority", "")
        return context


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    template_name = "tasks/task_detail.html"
    context_object_name = "task"


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("tasks:task-list")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("tasks:task-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    template_name = "tasks/task_confirm_delete.html"
    success_url = reverse_lazy("tasks:task-list")


class TaskToggleCompleteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_completed = not task.is_completed
        task.save()
        next_url = request.POST.get("next") or reverse("tasks:task-detail", args=[task.pk])
        return redirect(next_url)


