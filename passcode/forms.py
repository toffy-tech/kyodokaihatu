from django import forms

class PassCodeForm(forms.Form):
  word=forms.CharField(label='title')