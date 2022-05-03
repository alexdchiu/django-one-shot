from django.urls import path

from todos.views import (
  TodoListView,
)

urlpatterns = [
  path("todos",TodoListView.as_view(), name = "todos_list"),
]