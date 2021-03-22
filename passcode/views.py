from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import TemplateView
from .forms import PassCodeForm
from .forms import PassCodeLanguageForm
from .forms import PassCodeCommentForm
from .forms import PostForm
from .models import Part
from .models import Code
from .models import Comment
from .models import Language
from .models import Good
from .models import CodeReport
from .models import CommentReport
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

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

class PostFormView(LoginRequiredMixin,TemplateView):

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
    part=Part.objects.get(id=part)
    kind=kind
    language=Language.objects.get(id=request.POST['language'])
    explain=request.POST['explain']
    time=request.POST['time']
    date=datetime.datetime.now()
    content=request.POST['content']
    code=Code(title=title,oner=oner,part=part,kind=kind,language=language,explain=explain,time=time,date=date,content=content)
    code.save()
    return redirect(to='/passcode/')


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
    ranking=Code.objects.filter(part=item.part,kind=item.kind).order_by('good').reverse()[0:5]
    self.params['list']=ranking

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
    ranking=Code.objects.filter(part=item.part,kind=item.kind).order_by('good').reverse()[0:5]
    self.params['list']=ranking

    return render(request,'passcode/comment.html',self.params)

@login_required()
def good(request,code_id):
  good_code=Code.objects.get(id=code_id)
  is_good=Good.objects.filter(user=request.user).filter(code=good_code).count()

  if is_good > 0:
    messages.success(request,'即にGoodしています。')
    return redirect(to='/passcode/comment/'+str(code_id))
  
  good_code.good+=1
  good_code.save()

  good=Good()
  good.user=request.user
  good.code=good_code
  good.save()
  return redirect(to='/passcode/comment/'+str(code_id))

@login_required()
def code_report(request,code_id):
  report_code=Code.objects.get(id=code_id)
  is_good=CodeReport.objects.filter(user=request.user).filter(code=report_code).count()

  if is_good > 0:
    messages.success(request,'即にReportしています。')
    return redirect(to='/passcode/comment/'+str(code_id))
  
  report_code.report+=1
  report_code.save()

  report=CodeReport()
  report.user=request.user
  report.code=report_code
  report.save()
  return redirect(to='/passcode/comment/'+str(code_id))

@login_required()
def comment_report(request,comment_id,comment_item):
  report_comment=Comment.objects.get(id=comment_item)
  is_good=CommentReport.objects.filter(user=request.user).filter(comment=report_comment).count()

  if is_good > 0:
    messages.success(request,'即にReportしています。')
    return redirect(to='/passcode/comment/'+str(comment_id))
  
  report_comment.report+=1
  report_comment.save()

  report=CommentReport()
  report.user=request.user
  report.comment=report_comment
  report.save()
  return redirect(to='/passcode/comment/'+str(comment_id))



class PassCodePersonView(TemplateView):

  def __init__(self):
    self.params={
      'title':{},
      'list':{},
    }

  def get(self,request,user):

    self.title=Code.objects.get(id=user)

    item=Code.objects.filter(oner=user).order_by('date').reverse()
    self.params['list']=item

    return render(request,'passcode/person.html',self.params)

  def post(self,request,user):
    
    self.title=Code.objects.get(id=user)

    item=Code.objects.filter(oner=user).order_by('date').reverse()
    self.params['list']=item

    return render(request,'passcode/person.html',self.params)