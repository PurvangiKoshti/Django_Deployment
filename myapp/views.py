from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'home.html',{'name':'Purvangi'})

def add(request):
    res= int(request.POST['num1']) + int(request.POST['num2'])

    
    # return HttpResponse("Result : {{res}}")
    return render(request,'result.html',{'result':res})


def view_product(request):
    return render(request,'view_product.html')