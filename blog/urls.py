from django.urls import path 
from .views import *

app_name = 'blog'

urlpatterns = [
    path('about/', about_page_view, name='blog-about'), 
    path('policy/', privacy_policy_view, name='blog-policy'),
    path('terms/', terms_conditions_view, name='blog-term'),

]




