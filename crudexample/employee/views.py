from django.shortcuts import render
from .models import Members
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse


# Create your views here.

def emp(request):
    return render(request,'index.html')  
def add(request):
    return render(request,'add.html')  

def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  member = Members(firstname=x, lastname=y)
  member.save()
  data="inserted"
  return render(request,'add.html',{'data':data})  

def index(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers
  }
  return HttpResponse(template.render(context, request))

def update(request, id):
  mymember = Members.objects.get(id=id)
  
  context = {
    'mymember': mymember,
  }
  return render(request,'update.html',context)

def updaterecord(request, id):
  first = request.POST['first']
  last = request.POST['last']
  member = Members.objects.get(id=id)
  member.firstname = first
  member.lastname = last
  member.save()
  return HttpResponseRedirect(reverse('index'))


def delete(request, id):
  member = Members.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))