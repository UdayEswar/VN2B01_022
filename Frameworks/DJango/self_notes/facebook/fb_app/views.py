import requests
from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog,Student


# Create your views here.

def name(request):
    return HttpResponse("Hii,\n Welcome To My World")


def name1(request):
    return HttpResponse("Hi i'm Vasanth")


def name2(request):
    return HttpResponse("Hi i'm Sunitha")

def name4(request):
    return HttpResponse('Hi We Are Vasudev')


def name5(request):
    return HttpResponse(f'Vasanth and Sunitha Are Made For Each Other {"💞💕Vasudev💞💕"}')

def city(request, city):
    return HttpResponse(f'Enter The any Name {city}')

def watsap(request):
    post = Blog.objects.all()
    return render(request, "Whatsapp Project.html", {"post": post})


def student(request):
    student = Student.objects.all()

    return render(request,"Student Details.html",{'student':student})

def post(request):
    name = request.post['uday']
    return HttpResponse(f'This Is post {name}')







