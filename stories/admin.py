from django.contrib import admin
from .models import *


# Register your models here. 
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'is_available', 'author', 'date')
    list_filter = ('is_available','date',)
    list_editable = ('is_available',)
    search_fields = ('title', 'publisher', 'is_available', 'author', 'date')   

admin.site.register(Story, StoryAdmin)



