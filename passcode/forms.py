from django import forms
from .models import Language

class PassCodeForm(forms.Form):
  word=forms.CharField(label='title')

class PassCodeLanguageForm(forms.Form):
  item=Language.objects.all()
  data=[]
  for i in item:
    a=(i.id,i.name)
    data.append(a)
  language=forms.MultipleChoiceField(label='language',choices=data)

class PassCodeCommentForm(forms.Form):
  word=forms.CharField(label='keyword')

class PostForm(forms.Form):
  # 言語の取り出し
  item=Language.objects.all()
  data=[]
  for i in item:
    a=(i.id,i.name)
    data.append(a)

  title=forms.CharField(label='タイトル')
  language=forms.ChoiceField(label='言語',choices=data)
  time=forms.FloatField(label='実行時間')
  content=forms.CharField(label='コード')
  explain=forms.CharField(label='説明')
