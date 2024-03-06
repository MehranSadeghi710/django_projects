from django.urls import path
from django.views.generic import detail, edit
from .views import *

app_name = 'home'
urlpatterns = [
    path('', home, name='home'),
    path('tasks', tasks, name='tasks'),
    path('todos', todo, name='todos'),
    path('tasks/<int:todo_id>/', delete, name='delete'),
    path('todos/<int:todo_id>/update', update, name='update'),
    path('tasks/<int:todo_id>/detail', detail, name='detail')
]