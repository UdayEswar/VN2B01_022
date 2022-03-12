from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *

def some_fun(request):
    return HttpResponse("Hello Harsha")

def some_fun2(request,name,id):
    return HttpResponse('Hello {} your id is {}'.format(name,id))

def rend_func(request):
    return render(request,'reels/index.html')

def rend_fun2(request,name,id):
    data = {'key_name':name,'key_id':id}
    return render(request,'reels/main.html',data)

def rend_fun3(request):
    names = ['harsha','ranjith','mani','madhu']
    locations = [ 'blr','hyd']
    ids = [1,2,3,4]
    data = {'key_names':names,'key_locations':locations,'key_ids':ids}
    return render(request,'reels/main2.html',data)

@csrf_exempt
def post_method(request):
    if request.method == 'POST':
        name = request.POST['name']
        id = request.POST['id']
        return HttpResponse(f'hello my {name} is {id}')
    if request.method == "GET":
        return HttpResponse('Hello harsha')
    
@csrf_exempt
def some_fun3(request):
    if request.method == 'POST':
        emp_name = request.POST['name']
        emp_id = request.POST['id']
        Data.objects.create(name=emp_name, id=emp_id)
        return HttpResponse(f'{emp_name} {emp_id}')
    if request.method == 'GET':
        return HttpResponse('hello my harsha')
    
        
        
        
class Name():
    def __init__(self, name):
        self.name = name
    def some_fun3(self):
        return f'{self.name}'

a = Name(name = 'harsha')
print(a.some_fun3())