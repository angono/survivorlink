from django.contrib import admin
from .models import *


# Register your models here. 
class TipAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_available', 'date')
    list_filter = ('is_available','date',)
    list_editable = ('is_available',)
    search_fields = ('title', 'author', 'is_available', 'date')   

admin.site.register(Tip, TipAdmin)



