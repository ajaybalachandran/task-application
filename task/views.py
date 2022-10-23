from django.shortcuts import render, redirect
from django.views.generic import View
from task.models import Task
from task.forms import RegistrationForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils.decorators import method_decorator
# Create your views here.


def sigin_required(fn):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "You must login")
            return redirect('todo-signin')
        else:
            return fn (request, *args, **kwargs)
    return wrapper

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html")


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "login.html")


class SignupView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "signup.html")


@method_decorator(sigin_required, name="dispatch")
class TaskAddView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "add_task.html")

    def post(self, request, *args, **kwargs):
        # print(request.POST)
        username = request.user
        task = request.POST.get('task')
        Task.objects.create(user=username, task_name=task)
        # return render(request, "add_task.html")
        messages.success(request, "task has been created")
        return redirect('todo-all')


@method_decorator(sigin_required, name="dispatch")
class TaskListView(View):
    def get(self, request, *args, **kwargs):
        # qs = Task.objects.all()
        # if request.user.is_authenticated:
        qs = request.user.task_set.all()
        return render(request, "task_list.html", {'todos': qs})
        # else:
            # return redirect("todo-signin")


@method_decorator(sigin_required, name="dispatch")
class TaskDetailView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        task = Task.objects.get(id=id)
        return render(request, "task_details.html", {"todo": task})


@method_decorator(sigin_required, name="dispatch")
class TaskDeleteView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        task = Task.objects.get(id=id)
        task.delete()
        messages.success(request, "task deleted")
        return redirect("todo-all")


class RegistrationView(View):
    def get(self, request, *args, **kwargs):
        form = RegistrationForm()
        return render(request, 'registration.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            # form.save()
            messages.success(request, "account created")
            return redirect('todo-signin')
        else:
            messages.error(request, "registration failed")
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
                messages.error(request, "invalid credentials")
                return render(request, 'signin.html', {'form': form})


# function based view
@sigin_required
def signout_view(request, *args, **kwargs):
    logout(request)
    return redirect('todo-signin')
