from django.urls import path 
from .views import *

app_name = 'story'

urlpatterns = [
    path('', story_list_view, name='story-list'), 
    path('story/detail/<str:ids>/',story_detail_view, name='story-detail'),
    path('search/story/', search_story_view, name='story-search'),

]




