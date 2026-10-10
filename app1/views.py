from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Task
# Create your views here.
def taskname(request):
    task_stored = request.POST['task']
    Task.objects.create(task = task_stored)

    return redirect ('home')