from django.contrib import admin
from .models import *

admin.site.register(Services)

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photo', 'time_create', 'is_published', 'content')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_pubslished', )
    list_filter = ('time_create', 'is_published')
# Register your models here.