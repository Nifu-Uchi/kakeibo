from django.shortcuts import render

# Create your views here.

from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Category,Ranks,Suitoh

class SuitohListView(ListView):

    model = Suitoh
    template_name = 'kakeibo_tuto/Suitoh_list.html'

    '''全取得'''
    def queryset(self):
        return Suitoh.objects.all()