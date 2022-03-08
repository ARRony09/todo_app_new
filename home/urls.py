from django.urls import path

from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('create', views.create,name="create"),
    path('current', views.current,name="current"),
    path('completed', views.completed,name="completed"),
    path('login', views.handlelogin,name="handlelogin"),
    path('signup', views.handlesignup,name="handlesignup"),
    path('logout', views.handlelogout,name="handlelogout"),
    path('todo_details/<str:pk>', views.todo_details,name="todo_details"),
    path('todo_details/<str:pk>/delete', views.delete,name="delete"),
    path('todo_details/<str:pk>/completetodo', views.completetodo,name="completetodo")
]
