from django.urls import path

from todolist.views import login_user, logout_user, register, show_todos, create_todo


app_name = "todolist"

urlpatterns = [
    path("login/", login_user, name="login_user"),
    path("register/", register, name="register"),
    path("logout/", logout_user, name="logout_user"),
    path("create/", create_todo, name="create_todo"),
    path("", show_todos, name="show_todos"),
]
