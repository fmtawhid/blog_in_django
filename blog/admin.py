from django.contrib import admin
from . models import *
# Register your models here.

admin.site.register(auth)
admin.site.register(catagory)
class articleAdmin(admin.ModelAdmin):
    list_display= ['title', 'article_auth']
    search_fields= ['title', 'article_auth']
    list_per_page= 10
    list_filter = ['title', 'article_auth']
admin.site.register(article, articleAdmin)

