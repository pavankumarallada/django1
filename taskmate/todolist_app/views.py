from django. shortcuts import render
from django.http import HttpResponse

# Create your views here.
def todolist(request):
    return render(request, 'html/todolist.html',{})


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