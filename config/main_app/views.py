from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from . models import Task

class HomePageView(ListView):
  model = Task
  context_object_name = 'task'
  template_name = 'task-list.html'