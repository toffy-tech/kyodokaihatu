from django.urls import path
from . import views
from .views import PassCodeView
from .views import PassCodeCodeView
from .views import PassCodeCommentView
from .views import PostFormView
from .views import PassCodePersonView


urlpatterns=[
  path(r'',PassCodeView.as_view(),name='index'),
  path(r'code/<int:part>/<str:kind>',PassCodeCodeView.as_view(),name='code'),
  path(r'postform/<int:part>/<str:kind>',PostFormView.as_view(),name='postform'),
  path(r'comment/<int:part>',PassCodeCommentView.as_view(),name='comment'),
  path(r'person/<int:user>',PassCodePersonView.as_view(),name='person'),
  path('good/<int:code_id>',views.good,name='good'),
  path('code_report/<int:code_id>',views.code_report,name='code_report'),
  path('comment_report/<int:comment_id>/<int:comment_item>',views.comment_report,name='comment_report'),
]