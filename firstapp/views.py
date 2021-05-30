from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dict={'insert_me' : "Hello i am from views.py inserted data from index.html file from templates folder"}
    return render(request,'firstapp/index.html',context=my_dict)