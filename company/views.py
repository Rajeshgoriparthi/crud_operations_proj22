from django.shortcuts import render
from django.http import HttpResponse
from company.models import *
# Create your views here.

def back_to_frnt(request):
    Lod=departments.objects.all()
    d={'ddata':Lod}
    return render(request,'back_to_frnt.html',d)


def emp_table(request):
    Loe=employe.objects.all()
    d1={'edata':Loe}
    return render(request,'emp_table.html',d1)