from django.shortcuts import render
from .models import *
from .forms import *
from django.http import *
from django.contrib import messages

def student(request):
    if request.method =='POST':
        form = Student_from(request.POST)
        if form.is_valid():
            messages.success(request, 'user registration sucessfull')
            form.save()
            email=Student_from.cleaned_data['email']
            return HttpResponseRedirect('/studentform/')
    else:
        form = Student_from()
    return render(request,'student.html',{'form':form})
# Create your views here.
