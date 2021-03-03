from django.db import models

class Part(models.Model):
  title=models.CharField(max_length=100)
  kind=models.CharField(max_length=20)

  def __str__(self):
    return '<Part:id='+str(self.id)+','+self.title+'>'

class Language(models.Model):
  name=models.CharField(max_length=100)

  def __str__(self):
    return '<Part:id='+str(self.id)+','+self.name+'>'


class Code(models.Model):
  title=models.CharField(max_length=100)
  who=models.ForeignKey(User,on_delete=models.CASCADE,related_name=who)
  part=models.ForeignKey(Part,on_delete=models.CASCADE,related_name=part)
  kind=models.CharField(max_length=1)
  good=models.IntegerField(max_value=10000)
  language=models.ForeignKey(Language,on_delete=models.CASCADE,related_name=language)
  explain=models.CharField(max_length=1000)
  time=models.FloatField(min_value=0,max_value=10)
  date=models.DateTimeField()
  code=models.CharField(min_length=20,max_length=524288)
  title=models.CharField(max_length=100)
  r=ti

  def __str__(self):
    return '<Part:id='+str(self.id)+','+self.title+'>'


