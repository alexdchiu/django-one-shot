from django.shortcuts import render
from django.views.generic.list import ListView

from todos.models import TodoList, TodoItem

from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

class TodoListView(ListView):
  model = TodoList
  template_name = "todos/list.html"

  # return render(request, "todos_list", HttpResponse(status=200))

