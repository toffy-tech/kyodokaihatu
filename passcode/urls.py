from django.urls import path
from . import views
from .views import PassCodeView

urlpatterns=[
  path(r'',PassCodeView.as_view(),name='index')
]