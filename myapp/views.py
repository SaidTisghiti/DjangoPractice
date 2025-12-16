#from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render

# Create your views here.

def index(request):
    #return HttpResponse("Index page")
    return render(request, 'index.html')

def hello(request, username):
    print(f"Username from URL: {username}")
    return HttpResponse("<h1>Hello, %s!</h1>" % username)

def about(request):
    #return HttpResponse("<h1>About Page</h1><p>This is the about page of our website.</p>")
    return render(request, 'about.html')

def projects(request):
    projects = Project.objects.all()
    # return JsonResponse({'projects': list(projects.values())})
    return render(request, 'projects.html', {'projects': projects})

def tasks(request):
    # task = Task.objects.get(id=id)
    # task = get_object_or_404(Task, id=id)
    # return HttpResponse("task: %s - %s" % (task.title, task.description))
    tasks = Task.objects.all()

    return render(request, 'tasks.html', {'tasks': tasks})