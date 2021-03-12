from django.urls import path
from . import views
from .views import PassCodeView
from .views import PassCodeCodeView
from .views import PassCodeCommentView
from .views import PostFormView

urlpatterns=[
  path(r'',PassCodeView.as_view(),name='index'),
  path(r'code/<int:part>/<str:kind>',PassCodeCodeView.as_view(),name='code'),
  path(r'postform/<int:part>/<str:kind>',PostFormView.as_view(),name='postform'),
  path(r'comment/<int:part>',PassCodeCommentView.as_view(),name='comment'),
]