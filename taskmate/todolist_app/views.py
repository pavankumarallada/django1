from django. shortcuts import render,redirect
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm

# Create your views here.
def todolist(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todolist')  # redirect to the same view after saving
    else:
        form = TaskForm()

    task_lists = TaskList.objects.all()
    context = {
        'welcome_text': 'Welcome to TaskList home',
        'task_lists': task_lists,
        'form': form
    }
    return render(request, 'html/todolist.html', context)


def pavan(request):
    context={
        'welcome_text':'welcome to jinja 2 template pavan'
    }
    return render(request,'html/pavan.html',context)

def contact(request):
    context={
        'welcome_text':'welcome to jinja 2 template contact'
    }
    return render(request,'html/contact.html',context)

def about(request):
    context={
        'welcome_text':'welcome to jinja 2 template about'
    }
    return render(request,'html/about.html',context)


#below are the examples of for loop and if condition in jinja2 template
def listpage(request):
    items = ["Pen", "Book", "Laptop"]
    return render(request, "html/listpage.html", {"items": items})

def conditionpage(request):
    score = 72
    return render(request, "html/conditionpage.html", {"score": score})
