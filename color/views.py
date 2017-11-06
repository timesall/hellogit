# coding: utf-8
from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return render(request,'index.html')

def noName(request,year):
    return HttpResponse(u'今年是%s年'%year)

def mingMing(request,year,month,day):
    return HttpResponse(u'今天是%s年%s月%s日'%(year,month,day))

def getTest(request):
    id = request.GET.get('id')
    name = request.GET.get('name')
    age = request.GET.get('age')
    context = {'id':id,'name':name,'age':age}
    return render(request,'index.html',context)
    #return  HttpResponse(int(id),str(name),int(age))
# get 和命名参数综合练习
def getTestName(request,date):
    # 接收地址栏的值
    id = request.GET['id']
    name = request.GET['name']
    age = request.GET['age']
    return render(request,'index.html',{'date':date,'id':id,'name':name,'age':age})