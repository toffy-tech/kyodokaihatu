from django.contrib import admin
from .models import Part,Language,Code,Comment,Good,CodeReport,CommentReport

admin.site.register(Part)
admin.site.register(Language)
admin.site.register(Code)
admin.site.register(Comment)
admin.site.register(Good)
admin.site.register(CodeReport)
admin.site.register(CommentReport)