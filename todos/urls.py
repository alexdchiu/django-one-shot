from django.urls import path

from todos.views import (
  TodoListView,
  TodoListDetailView,
  TodoListCreateView,
  # TodoListUpdateView,
  # TodoListDeleteView,
)

urlpatterns = [
  path("",TodoListView.as_view(), name = "todolists_list"),
  path("<int:pk>/", TodoListDetailView.as_view(), name = "todolist_detail"),
  path("create/",TodoListCreateView.as_view(), name = "todolist_create"),
]