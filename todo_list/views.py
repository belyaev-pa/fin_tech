from django.shortcuts import render_to_response
from rest_framework import generics
from todo_list.serializers import TaskSerializer
from todo_list.models import Task



class TaskListView(generics.ListCreateAPIView):
    """   Вывод и создание списка задач    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskListDetailView(generics.RetrieveUpdateDestroyAPIView):
    """  Создаем read/write/update/delete для каждой задачи """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


def index(request):
    context = {}
    return render_to_response('todo_list/index.html', context)
