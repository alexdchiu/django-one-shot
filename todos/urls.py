from django.urls import path

from todos.views import (
  TodoListView,
)

urlpatters = [
  path("",TodoListView.as_view(), name = "todos_list"),
]