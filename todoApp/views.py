from django.shortcuts import render,redirect
from todoApp.models import Todo
from todoApp.forms import TodoForm
# Create your views here.
def index(request):
    todo_list = Todo.objects.order_by('id')
    form = TodoForm()
    context = {'todo_list':todo_list,'form':form}
    return  render(request,"todoApp/index.html",context)


def addTodo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        new_todo = Todo(text = request.POST['text'])
        new_todo.save()
    return index(request)

def complete(request,id):
    todo = Todo.objects.get(id = id)
    todo.complete = True
    todo.save()
    return index(request)

def deleteCompleted(request):
    Todo.objects.filter(complete__exact = True).delete()
    return index(request)

def deleteAll(request):
    Todo.objects.all().delete()
    return index(request)
