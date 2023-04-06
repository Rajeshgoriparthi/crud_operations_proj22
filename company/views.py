from django.shortcuts import render
from django.http import HttpResponse
from company.models import *
from django.db.models.functions import Length
# Create your views here.

def back_to_frnt(request):
    Lod=departments.objects.all()
    d={'ddata':Lod}
    return render(request,'back_to_frnt.html',d)


def emp_table(request):
    Loe=employe.objects.all()
    Loe=employe.objects.filter(ename='Rajesh')
    Loe=employe.objects.order_by('ename')
    Loe=employe.objects.order_by('-ename')
    Loe=employe.objects.exclude(ename='Rajesh')
    Loe=employe.objects.all()
    Loe=employe.objects.filter(age__gt='22')
    Loe=employe.objects.filter(emp_id__gt='1001')
    Loe=employe.objects.filter(emp_id__gt='1002')
    Loe=employe.objects.filter(age__gte='24')
    Loe=employe.objects.filter(age__lt='23')
    Loe=employe.objects.filter(age__lte='23')
    Loe=employe.objects.order_by(Length('ename'))
    Loe=employe.objects.order_by(Length('ename').desc())
    d1={'edata':Loe}
    return render(request,'emp_table.html',d1)