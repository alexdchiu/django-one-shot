from django.urls import path

from todos.views import (
  TodoListEditView,
  TodoListView,
  TodoListDetailView,
  TodoListCreateView,
  TodoListEditView,
  TodoListDeleteView,
  TodoItemCreateView,
  TodoItemEditView,
)

urlpatterns = [
  path("",TodoListView.as_view(), name = "todolists_list"),
  path("<int:pk>/", TodoListDetailView.as_view(), name="todolist_detail"),
  path("create/",TodoListCreateView.as_view(), name="todolist_create"),
  path("<int:pk>/edit/", TodoListEditView.as_view(), name="todolist_edit"),
  path("<int:pk>/delete/", TodoListDeleteView.as_view(),name="todolist_delete"),
  path("todos/items/create/", TodoItemCreateView.as_view(),name="todoitem_create"),
  path("todos/items/<int:pk>/edit/", TodoItemEditView.as_view(),name="todoitem_edit"),    
]