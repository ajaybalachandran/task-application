"""task_application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task.views import IndexView, LoginView, RegistrationView, SignupView, TaskAddView, TaskListView, TaskDetailView, TaskDeleteView, RegistrationView, LoginView, signout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', IndexView.as_view()),
    path('login/', LoginView.as_view()),
    path('signup/', SignupView.as_view()),
    path('add_task/', TaskAddView.as_view(), name="todo-add"),
    path('todos/all/', TaskListView.as_view(), name="todo-all"),
    path('todos/<int:id>/', TaskDetailView.as_view(), name="todo-detail"),
    path('todos/<int:id>/remove/', TaskDeleteView.as_view(), name="todo-delete"),
    path('accounts/register/', RegistrationView.as_view(),
         name='todo-registration'),
    path('signin/', LoginView.as_view(), name='todo-signin'),
    path('signout/', signout_view, name='todo-signout'),


]
