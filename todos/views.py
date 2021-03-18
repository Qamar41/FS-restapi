from django.shortcuts import render,HttpResponse
from rest_framework.generics import ListCreateAPIView, ListAPIView
from .serializers import TodosSerializer
from .models import Todo
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .services import TodosListView ,updatelogic,deletelogic
from .datalayer import alldata

def home(request):
    return render (request, 'index.html' )



# # List of all the tasks
class TodosListView(ListCreateAPIView):
    queryset=alldata()   #alldata() is coming from datalayer.py
    serializer_class = TodosSerializer



class TodosCreateView(generics.CreateAPIView):
    serializer_class = TodosSerializer




@api_view(['GET'])
def taskDetail(request, pk):
	tasks = taskdetails(pk)
	serializer = TodosSerializer(tasks, many=False)
	return Response(serializer.data)





# Updating tasks
@api_view(['GET', 'PATCH'])
def TaskUpdate(request, pk):
    updating=updatelogic(request,pk)
    return Response(updating.data)
    
  


# Deleting Task
@api_view(['GET', 'DELETE'])
def TaskDelete(request, pk):
    x=deletelogic(request,pk)
    return Response(x.data)