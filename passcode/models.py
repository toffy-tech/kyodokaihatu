from django.conf import settings
from django.db import models

class Part(models.Model):
  title=models.CharField(max_length=100)
  kind=models.CharField(max_length=20)

  def __str__(self):
    return '<Part:id='+str(self.id)+','+self.title+'>'

class Language(models.Model):
  name=models.CharField(max_length=100)

  def __str__(self):
    return '<Language:id='+str(self.id)+','+self.name+'>'


class Code(models.Model):
  title=models.CharField(max_length=100)
  oner=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='oner')
  part=models.ForeignKey(Part,on_delete=models.CASCADE,related_name='part')
  kind=models.CharField(max_length=1)
  good=models.IntegerField(default=0)
  language=models.ForeignKey(Language,on_delete=models.CASCADE,related_name='language')
  explain=models.CharField(max_length=1000)
  time=models.FloatField()
  date=models.DateTimeField()
  content=models.CharField(max_length=524288)
  report=models.IntegerField(default=0)

  def __str__(self):
    return '<Code:id='+str(self.id)+','+self.title+'>'

class Comment(models.Model):
  comment=models.CharField(max_length=1000)
  code=models.ForeignKey(Code,on_delete=models.CASCADE,related_name='code')
  user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='user')
  report=models.IntegerField(default=0)
  data=models.DateTimeField()

  def __str__(self):
    return '<Comment:id='+str(self.id)+',user_id='+str(self.user)+'>'