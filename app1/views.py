from django.shortcuts import redirect,get_object_or_404,render
from django.http import HttpResponse
from .models import Task
# Create your views here.
def taskname(request):
    task_stored = request.POST['task']
    Task.objects.create(task = task_stored)

    return redirect ('home')

def mark_as_done(request,pk):
    task_cmplt = get_object_or_404(Task,pk=pk)
    task_cmplt.is_completed= True
    task_cmplt.save()
    return redirect('home')

def task_undone(request,pk):
    task_remove = get_object_or_404(Task,pk=pk)  
    task_remove.is_completed =False
    task_remove.save()
    return redirect('home')

def edit_task(request,pk):
    task_update = get_object_or_404(Task,pk=pk)
    if request.method=='POST':
        updated_task =request.POST['task']
        task_update.task = updated_task
        task_update.save()
        return redirect('home')

    else:
        context={
            'task_update': task_update
        }
        return render(request,'edit_task.html',context)

def remove_task(request,pk):
    task = get_object_or_404(Task,pk = pk)
    task.delete()
    return redirect('home')