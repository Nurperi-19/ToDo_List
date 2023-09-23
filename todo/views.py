from rest_framework.decorators import api_view
from rest_framework.response import Response
from todo.serializers import *
from todo.models import *
from rest_framework import status
from rest_framework.generics import ListCreateAPIView

# ClassBasedView
class TaskListAPIView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# FunctionBasedView

@api_view(['GET', 'DELETE', 'PUT'])
def tasks_detail_view(request, id):
    try:
        task = Task.objects.get(id=id)
    except Task.DoesNotExist:
        return Response(data={'error: task not found'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        title = request.data.get('title')
        description = request.data.get('description')

        task.title = title
        task.description = description
        task.save()
        return Response(data=TaskSerializer(task).data,
                        status=status.HTTP_201_CREATED)


