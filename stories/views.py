from django.shortcuts import render  
from django.contrib.auth.models import User 
from django.db.models import Q 
from django.contrib import messages 
from django.views.generic import ListView, DetailView 
from .models import * 
from django.core.paginator import Paginator



# Create your views here.
class StoryListView(ListView):
    model = Story
    template_name = 'stories/story_list.html'
    context_object_name = 'story_data'
    # paginate_by = 20


class StoryDetailView(DetailView):
    model = Story 
    template_name = 'stories/story_detail.html'


def search_story_view(request):
    query = request.GET.get('q', None)
    if query == None or query == "":
        story_data = Story.objects.all()
    elif query is not None:
        story_data = Story.objects.filter(
            Q(publisher__username__icontains=query)|
            Q(publisher__email__icontains=query)|
            Q(title__icontains=query)|
            Q(content__icontains=query)|
            Q(author__icontains=query)|
            Q(date__icontains=query)).distinct()

    context = {
        'story_data':story_data
    }
    return render(request, 'stories/story_list.html', context)











