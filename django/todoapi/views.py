from .models import Task
from .serializers import TaskSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics

class TaskList(generics.ListCreateAPIView):
    """
    Lists and creates tasks
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

"""class TaskDetail(APIView):

    #Returns a single Task and allows updates and deletion of task.

    def get_object(self,task_id):
        try:
            return Task.objects.get(pk=task_id)
        except Task.DoesNotExist:
            raise Http404

    def get(self,request,task_id,format=None):
        task= self.get_object(task_id)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self,request,task_id,format=None):
        task = self.get_object(task_id)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serialize.data)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,task_id,format=None):
        task = self.get_object(task_id)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)"""
class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Returns a single Task and allows updates and deletion of a Task.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_url_kwarg = 'task_id'

