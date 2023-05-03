from django.shortcuts import render
from app.forms import *
# Create your views here.
from django.http import HttpResponse

def student(request):
    SFO=studentform()
    d={'SFO':SFO}

    if request.method=='POST':
        SFDO=studentform(request.POST)
        if SFDO.is_valid():
            return HttpResponse(str(SFDO.cleaned_data))
        else:
            return HttpResponse('data is not valid')


    return render(request,'student.html',d)