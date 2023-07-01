from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from .models import Project, Task
from accounts.models import Profile

# Create your views here.


class HomePageView(ListView):
    model = Task
    context_object_name = 'task'
    template_name = 'index.html'

    def get(self, request):
        all_tasks = Task.objects.all().order_by('-id')
        doned_tasks = Task.objects.filter(status='doned')
        inprocess_tasks = Task.objects.filter(status='inprocess')

        data = {
            'all_tasks': all_tasks,
            'doned_tasks': doned_tasks,
            'inprocess_tasks': inprocess_tasks
        }

        return render(request, self.template_name, context=data)


def profile_project_add(request):
    if request.method == 'POST':
        author = Profile.objects.get(id=request.user.id)
        print(author)
        Project.objects.create(
            author=author,
            project_name=request.POST.get('project_name'),
            project_link=request.POST.get('project_link'),
            poster=request.POST.get('poster')
        )
        print('ok')
    return redirect("accounts:profile")
