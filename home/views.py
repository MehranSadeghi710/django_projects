from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo


def home(request):
    return render(request, "index.html")


def tasks(request):
    tasks = Todo.objects.all()
    return render(request, "tasks.html", {'tasks': tasks, })


def delete(request, todo_id):
    task = Todo.objects.get(id=todo_id)
    task.delete()
    return redirect('home:home')


def update(request, todo_id):
    task = Todo.objects.get(id=todo_id)
    form = TodoForm(request.GET)
    if form.is_valid():
        todo_obj = Todo.objects.update()
        todo = form.cleaned_data
        todo_obj.title = todo['title']
        todo_obj.description = todo['description']
        todo_obj.status = todo['status']
        todo_obj.save()
    return redirect('home:update', task.id)


def detail(request, todo_id):
    task = Todo.objects.get(id=todo_id)
    return render(request, "detail.html", {'task': task, })


def todo(request):
    form = TodoForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            todo_obj = Todo.objects.create()
            todo = form.cleaned_data
            todo_obj.title = todo['title']
            todo_obj.description = todo['description']
            todo_obj.status = todo['status']
            todo_obj.save()
            return redirect('home:home')
    return render(request, "todo.html", {'form': form})



