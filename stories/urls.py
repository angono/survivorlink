from django.urls import path 
from .views import *

app_name = 'story'

urlpatterns = [
    path('', StoryListView.as_view(), name='story-list'), 
    path('story/detail/<str:pk>/', StoryDetailView.as_view(), name='story-detail'),
    path('search/story/', search_story_view, name='story-search'),

]




