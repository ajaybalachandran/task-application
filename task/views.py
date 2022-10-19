from django.shortcuts import render, redirect
from django.views.generic import View
from task.models import Task
from task.forms import RegistrationForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html")


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "login.html")


class SignupView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "signup.html")


class TaskAddView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "add_task.html")

    def post(self, request, *args, **kwargs):
        # print(request.POST)
        username = request.user
        task = request.POST.get('task')
        Task.objects.create(user=username, task_name=task)
        # return render(request, "add_task.html")
        return redirect('todo-all')


class TaskListView(View):
    def get(self, request, *args, **kwargs):
        # qs = Task.objects.all()
        if request.user.is_authenticated:
            qs = request.user.task_set.all()
            return render(request, "task_list.html", {'todos': qs})
        else:
            return redirect("todo-signin")


class TaskDetailView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        task = Task.objects.get(id=id)
        return render(request, "task_details.html", {"todo": task})


class TaskDeleteView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        task = Task.objects.get(id=id)
        task.delete()
        return redirect("todo-all")


class RegistrationView(View):
    def get(self, request, *args, **kwargs):
        form = RegistrationForm()
        return render(request, 'registration.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            # form.save()
            return redirect('todo-all')
        else:
            return render(request, 'registration.html', {'form': form})


class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'signin.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')
            usr = authenticate(request, username=uname, password=pwd)
            if usr:
                login(request, usr)
                return redirect('todo-all')
            else:
                return render(request, 'signin.html', {'form': form})


# function based view
def signout_view(request, *args, **kwargs):
    logout(request)
    return redirect('todo-signin')
