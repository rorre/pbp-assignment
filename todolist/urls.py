from django.urls import path

from todolist.views import (
    add_todos_json,
    delete_todo,
    login_user,
    logout_user,
    register,
    show_todos,
    create_todo,
    update_todo,
    show_todos_json,
)


app_name = "todolist"

urlpatterns = [
    path("login/", login_user, name="login_user"),
    path("register/", register, name="register"),
    path("logout/", logout_user, name="logout_user"),
    path("create/", create_todo, name="create_todo"),
    path("delete/<int:post_id>", delete_todo, name="delete_todo"),
    path("update/<int:post_id>", update_todo, name="update_todo"),
    path("json", show_todos_json, name="show_todos_json"),
    path("create/json", add_todos_json),
    path("", show_todos, name="show_todos"),
]
