from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),

    path('add/',addNewTodo,name='add'),
    path('complete/<int:todo_pk>/',completeTodo,name='complete'),

    path('delete/',deleteTodo,name='delete'),
]
