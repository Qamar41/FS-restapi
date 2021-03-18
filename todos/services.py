
from .models import Todo
from .serializers import TodosSerializer
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework import status
from .datalayer import alldata , taskdetails


# def tasks(self,request):
#     alltask= alldata()
#     serial_data=TodosSerializer(alltask)
#     return Response(serial_data.data,status=status.HTTP_200_OK)


# List of all the tasks
class TodosListView(ListCreateAPIView):
    queryset=alldata()
    serializer_class = TodosSerializer


                                            # updataing task 

def updatelogic(request,pk):
    try:
        model = taskdetails(pk)
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





                                                    # deleting task
def deletelogic(request,pk):
    try:
        model = taskdetails(pk)
    except:
        return Response('Not Found')

    if request.method == 'GET':
        serializer = TodosSerializer(instance=model)
        return Response(serializer.data)

    if request.method == 'DELETE':
        model.delete()
        return Response('Deleted')