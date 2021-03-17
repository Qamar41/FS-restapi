from django.urls import path
from .views import *
from .import views

urlpatterns = [
    path('',views.home ),
    #for list of All Tasks
    path('api/tasks', TodosListView.as_view()),
    path('api/create-task', TodosCreateView.as_view()),
    #updating specific task using its id
    path('api/task-update/<str:pk>', TaskUpdate, name="task-update"),
    #deleting specific task using its id
    path('api/task-delete/<str:pk>', TaskDelete, name="task-delete"),
]
