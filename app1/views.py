from django.shortcuts import render
from django.http import HttpResponse
from .models import student


def index(request):
    return HttpResponse("hello world")
def htm(request):
    return render(request,"hello.html")
def add(request):
    x=request.POST["name"]
    y=request.POST["rollno"]
    temp=student(name=x,rollno=y)
    temp.save()
    data= student.objects.all().values()
    return render(request,"out.html",{'temp':data})




# Create your views here.
