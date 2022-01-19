from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User 
from django.db.models import Q 
from django.contrib import messages 
from django.views.generic import ListView, DetailView 
from .models import * 
from django.core.paginator import Paginator


# Create your views here.
def story_list_view(request):
    story_data = Story.objects.all()
    context = {
        'story_data':story_data
    }
    return render(request, 'stories/story_list.html', context)


def story_detail_view(request, ids):
    ids = get_object_or_404(Story, id=ids)
    context = {
        'ids':ids
    }
    return render(request, 'stories/story_detail.html', context)


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











