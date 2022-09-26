from django.urls import path

from todolist.views import login_user, logout_user, register


app_name = "todolist"

urlpatterns = [
    path("login/", login_user, name="login_user"),
    path("register/", register, name="register"),
    path("logout/", logout_user, name="logout_user"),
]
