from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse

from todos.models import TodoList, TodoItem

# from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

class TodoListView(ListView):
  model = TodoList
  template_name = "todos/list.html"
  context_object_name = "todolist"

  # return render(request, "todos_list", HttpResponse(status=200))

class TodoListDetailView(DetailView):
  model = TodoList
  template_name = "todos/detail.html"

class TodoListCreateView(CreateView):
  model = TodoList
  template_name = "todos/create.html"
  fields = ["name"]
  success_url = reverse_lazy("somewhere")
  pk = None

  def form_valid (self, form):
    item = form.save()
    self.pk = item.pk
    return super(TodoListCreateView, self).form_valid(form)

  def get_success_url(self):
    return reverse('todolist_detail', kwargs = {'pk':self.pk})



class TodoListEditView(UpdateView):
  model = TodoList
  template_name = "todos/edit.html"
  fields = ["name"]
  
  def get_success_url(self):
    todolistid = self.kwargs['pk']
    return reverse_lazy("todolist_detail", kwargs={'pk':todolistid})


class TodoListDeleteView(DeleteView):
  model = TodoList
  template_name = "todos/delete.html"
  success_url = reverse_lazy("todolists_list")

class TodoItemCreateView(CreateView):
  model = TodoItem
  template_name = "todos/items/create.html"
  fields = ["task", "due_date", "is_completed", "list"]
  success_url = reverse_lazy("somewhere")
  pk = None

  def form_valid (self, form):
    item = form.save()
    self.pk = item.list.pk
    return super(TodoItemCreateView, self).form_valid(form)

  def get_success_url(self):
    return reverse('todolist_detail', kwargs = {'pk':self.pk})

class TodoItemEditView(UpdateView):
  model = TodoItem
  template_name = "todos/items/edit.html"
  fields = ["task", "due_date", "is_completed", "list"]
  success_url = reverse_lazy("somewhere")
  pk = None

  def form_valid (self, form):
    item = form.save()
    self.pk = item.list.pk
    return super(TodoItemEditView, self).form_valid(form)

  def get_success_url(self):
    return reverse('todolist_detail', kwargs = {'pk':self.pk})