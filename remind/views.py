from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .forms import TaskCreateForm
from .models import Task


class IndexView(generic.ListView):
    queryset = Task.objects.order_by("-date").reverse()
    paginate_by = 50


class AddView(generic.CreateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy('remind:index')


class UpdateView(generic.UpdateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy('remind:index')


class DeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy('remind:index')


class DetailView(generic.DetailView):
    model = Task
