from django.shortcuts import render  
from django.views.generic import ListView, DetailView 
from .models import * 



# Create your views here.
class TipListView(ListView):
    model = Tip
    template_name = 'tips/tip_list.html'
    context_object_name = 'tip_data'


class TipDetailView(DetailView):
    model = Tip 
    template_name = 'tips/tips_detail.html'












