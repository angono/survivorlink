from django.urls import path 
from .views import *

app_name = 'tips'

urlpatterns = [
    path('', tip_list_view, name='tip-list'), 
    path('detail/<str:ids>/', tip_detail_view, name='tip-detail'),

]




