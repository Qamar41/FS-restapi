from .models import Todo

def alldata():
    return Todo.objects.all()

def taskdetails(pk):
    return Todo.objects.get(id=pk)