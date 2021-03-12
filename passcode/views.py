from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from .forms import PassCodeForm
from .forms import PassCodeLanguageForm
from .forms import PassCodeCommentForm
from .forms import PostForm
from .models import Part
from .models import Code
from .models import Comment

import datetime

class PassCodeView(TemplateView):

  def __init__(self):
    self.params={
      'form':PassCodeForm,
      'data':{},
    }

  def get(self,request):
    item=Part.objects.filter()
  # ABCDに作成
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

class PassCodeCodeView(TemplateView):

  def __init__(self):
    self.params={
      'form':PassCodeLanguageForm,
      'data':{},
      'list':{},
      'id':'',
      'kind':'',
      'title':'',
    }

  def get(self,request,part,kind):
    self.params['id']=part
    self.params['kind']=kind
    self.params['title']=Part.objects.get(id=part)


    item=Code.objects.filter(part=part,kind=kind).order_by('date').reverse()
    self.params['data']=item

    # イイねリストの取り出し
    item=Code.objects.filter(part=part,kind=kind).order_by('good').reverse()[0:5]
    self.params['list']=item

    return render(request,'passcode/code.html',self.params)

  def post(self,request,part,kind):
    self.params['id']=part
    self.params['kind']=kind
    self.params['title']=Part.objects.get(id=part)

    language=request.POST['language']
    item=Code.objects.filter(language=language,part=part,kind=kind).order_by('date').reverse()
    self.params['data']=item

    # イイねリストの取得
    item=Code.objects.filter(language=language,part=part,kind=kind).order_by('good').reverse()[0:5]
    self.params['list']=item
    return render(request,'passcode/code.html',self.params)

# @login_required(login_url='/admin/login/')
class PostFormView(TemplateView):

  def __init__(self):

    self.params={
      'title':'投稿フォーム',
      'form':PostForm,
      'id':'',
      'kind':'',
    }

  def get(self,request,part,kind):
    self.params['id']=part
    self.params['kind']=kind
    return render(request,'passcode/postform.html',self.params)

  def post(self,request,part,kind):
    self.params['id']=part
    self.params['kind']=kind
    title=request.POST['title']
    oner=request.user
    part=part
    kind=kind
    language=request.POST['language']
    explain=request.POST['explain']
    time=request.POST['time']
    date=datetime.datetime.now()
    content=request.POST['content']
    code=Code(title=title,oner=oner,part=part,kind=kind,language=language,explain=explain,time=time,date=date,content=content,code=content)
    code.save()
    return redirect(to='/passcode/code/part/kind')


class PassCodeCommentView(TemplateView):

  def __init__(self):
    self.params={
      'title':{},
      'form':PassCodeCommentForm,
      'data':{},
      'list':{},
      'id':'',
    }

  def get(self,request,part):
    self.params['id']=part

    #コード取得
    item=Code.objects.get(id=part)
    self.params['title']=item

    #コメント取得
    item_comment=Comment.objects.filter(code=part)
    self.params['data']=item_comment

    # イイねリストの取り出し
    item=Code.objects.filter(id=part)
    
    # ranking=Code.objects.filter(part=item['part'],kind=item['kind']).order_by('good').reverse()[0:5]
    self.params['list']=item

    return render(request,'passcode/comment.html',self.params)

  def post(self,request,part):
    self.params['id']=part

    #コード取得
    item=Code.objects.get(id=part)
    self.params['title']=item

    #コメント取得
    word=request.POST['word']
    item_comment=Comment.objects.filter(code=part,comment_contain=word)
    self.params['data']=item_comment

    # イイねリストの取り出し
    item=Code.objects.filter(id=part)
    
    # ranking=Code.objects.filter(part=item['part'],kind=item['kind']).order_by('good').reverse()[0:5]
    self.params['list']=item

    return render(request,'passcode/comment.html',self.params)

