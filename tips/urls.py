from django.urls import path 
from .views import *

app_name = 'tips'

urlpatterns = [
    path('', TipListView.as_view(), name='tip-list'), 
    path('detail/<str:pk>/', TipDetailView.as_view(), name='tip-detail'),

]




