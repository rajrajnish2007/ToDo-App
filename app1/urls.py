from django.urls import path
from .import views

urlpatterns =[
    #Add Task
    path('taskname/', views.taskname,name = 'taskname'),
    #Mark as done
    path('mark_as_done/<int:pk>/',views.mark_as_done, name = 'mark_as_done'),
    #Mark as Undone
    path('task_undone/<int:pk>/',views.task_undone, name = 'task_undone'),
    #Edit Task
    path('edit_task/<int:pk>/',views.edit_task,name='edit_task'),
    #Delete Task
    path('remove_task/<int:pk>/',views.remove_task,name = 'remove_task')
]