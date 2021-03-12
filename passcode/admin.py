from django.contrib import admin
from .models import Part,Language,Code,Comment

admin.site.register(Part)
admin.site.register(Language)
admin.site.register(Code)
admin.site.register(Comment)