from todolist_app import views
from django.urls import path

urlpatterns=[
    path('',views.todolist,name='todolist'), #http://127.0.0.1:8000/task/ defined in project urls.py
    path('abc',views.pavan,name='pavan'),    #http://127.0.0.1:8000/task/abc
    path('contact',views.contact,name='contact'), #http://127.0.0.1:8000/task/contact
    path('about',views.about,name='about') ,  #http://127.0.0.1:8000/task/about
    path('list',views.listpage,name='listpage'),
    path('condition',views.conditionpage,name='conditionpage')
    

]