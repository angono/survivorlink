from django.shortcuts import render, get_object_or_404  
from django.views.generic import ListView, DetailView 
from .models import * 



# Create your views here.
def tip_list_view(request):
    tip_data = Tip.objects.all()
    context = {
        'tip_data':tip_data
    }
    return render(request, 'tips/tip_list.html', context)


def tip_detail_view(request, ids):
    ids = get_object_or_404(Tip, id=ids)
    context = {
        'ids':ids
    }
    return render(request, 'tips/tips_detail.html', context)












