from django.shortcuts import render , redirect
from .models import Todo
from .forms import TodoForm

from django.views.decorators.http import require_POST

# Create your views here.

def index(request):
    mytodo = Todo.objects.order_by('pk')
    form = TodoForm()
    context = {'mytodo' : mytodo , 'form' : form}

    return render(request,'todo_app/index.html',context)

@require_POST
def addNewTodo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        my_new_todo = Todo(text = request.POST['form_text'])
        my_new_todo.save()

    return redirect('index')

def completeTodo(request , todo_pk):
    mytodo = Todo.objects.get(pk=todo_pk)
    mytodo.complete = True
    mytodo.save()

    return redirect('index')

def deleteTodo(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('index')
