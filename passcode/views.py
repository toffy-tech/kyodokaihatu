from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import PassCodeForm
from .models import Part

class PassCodeView(TemplateView):

  def __init__(self):
    self.params={
      'title':'Hello',
      'form':PassCodeForm,
      'data':{},q
    }

  def get(self,request):
    item=Part.objects.filter()
    for i in item:
      new=[]
      for j in (i.kind):
        new.append(j)
      i.kind=new
    self.params['data']=item
    return render(request,'passcode/index.html',self.params)

  def post(self,request):
    word=request.POST['word']
    item=Part.objects.filter(title__contains=word)
    for i in item:
      new=[]
      for j in (i.kind):
        new.append(j)
      i.kind=new
    self.params['data']=item
    return render(request,'passcode/index.html',self.params)