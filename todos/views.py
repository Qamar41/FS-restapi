from django.shortcuts import render,HttpResponse
from rest_framework.generics import ListCreateAPIView, ListAPIView
from .serializers import TodosSerializer
from .models import Todo
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics



def home(request):
    return render (request, 'index.html' )

# List of all the tasks
class TodosListView(ListCreateAPIView):
    queryset=Todo.objects.all()
    serializer_class = TodosSerializer

class TodosCreateView(generics.CreateAPIView):
    queryset=Todo.objects.all()
    serializer_class = TodosSerializer




@api_view(['GET'])
def taskDetail(request, pk):
	tasks = Todo.objects.get(id=pk)
	serializer = TodosSerializer(tasks, many=False)
	return Response(serializer.data)





# Updating tasks
@api_view(['GET', 'PATCH'])
def TaskUpdate(request, pk):
    try:
        model = Todo.objects.get(id=pk)
    except:
        return Response('Not Found')

    if request.method == 'GET':
        serializer = TodosSerializer(instance=model)
        return Response(serializer.data)

    if request.method == 'PATCH':

        serializer = TodosSerializer(model, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data)

        else:
            return Response('Failed')


# Deleting Task
@api_view(['GET', 'DELETE'])
def TaskDelete(request, pk):
    try:
        model = Todo.objects.get(id=pk)
    except:
        return Response('Not Found')

    if request.method == 'GET':
        serializer = TodosSerializer(instance=model)
        return Response(serializer.data)

    if request.method == 'DELETE':
        model.delete()
        return Response('Deleted')
