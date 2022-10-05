from django import forms
from django.http import HttpRequest
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from todolist.models import Task


class NewTodoForm(forms.Form):
    date = forms.DateField(label="Tanggal")
    title = forms.CharField(label="Judul")
    description = forms.CharField(
        label="Deskripsi", widget=forms.Textarea(attrs={"cols": ""})
    )


def register(request: HttpRequest):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Akun telah berhasil dibuat!")
            return redirect("todolist:login_user")

    context = {"form": form}
    return render(request, "register.html", context)


def login_user(request: HttpRequest):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("todolist:show_todos")
        else:
            messages.info(request, "Username atau Password salah!")
    return render(request, "login.html")


def logout_user(request: HttpRequest):
    logout(request)
    return redirect("todolist:login_user")


@login_required(login_url="/todolist/login")
def show_todos(request: HttpRequest):
    todos = Task.objects.filter(user=request.user).order_by("date").all()
    ctx = {"todos": todos}
    return render(request, "list_todos.html", ctx)


def create_todo(request: HttpRequest):
    if request.method == "POST":
        form = NewTodoForm(request.POST)
        if form.is_valid():
            task = Task(
                date=form.cleaned_data["date"],
                title=form.cleaned_data["title"],
                description=form.cleaned_data["description"],
                user=request.user,
            )
            task.save()
            messages.success(request, "Berhasil disimpan!")
            return redirect("todolist:show_todos")

    form = NewTodoForm()
    ctx = {"form": form}
    return render(request, "create.html", ctx)


def update_todo(request: HttpRequest, post_id: int):
    if request.method == "POST":
        task = Task.objects.filter(id=post_id, user=request.user).first()
        if task:
            task.is_finished = not task.is_finished
            task.save()
            messages.success(request, "Berhasil update!")
        else:
            messages.error(request, "Task tidak ditemukan!")

    return redirect("todolist:show_todos")


def delete_todo(request: HttpRequest, post_id: int):
    if request.method == "POST":
        task = Task.objects.filter(id=post_id, user=request.user).first()
        if task:
            task.delete()
            messages.success(request, "Berhasil dihapus!")
        else:
            messages.error(request, "Task tidak ditemukan!")

    return redirect("todolist:show_todos")
