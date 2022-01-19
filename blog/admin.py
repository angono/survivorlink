from django.contrib import admin
from .models import * 


# Register your models here.

admin.site.site_header = 'Survivors Link'

admin.site.register(CustomerCall)

admin.site.register(CustomerEmail)


class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'content') 

admin.site.register(About, AboutAdmin)






