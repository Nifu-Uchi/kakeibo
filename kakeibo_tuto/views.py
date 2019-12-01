from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Category, Ranks, Suitoh
from django.db import models
from .forms import SuitohForm
from django.urls import reverse_lazy


class SuitohListView(ListView):
    model = Suitoh
    template_name = 'kakeibo_tuto/Suitoh_list.html'

    '''全取得'''

    def queryset(self):
        return Suitoh.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # はじめに継承元のメソッドを呼び出す
        context["foo"] = test('a')
        return context


def test(goma):
    param = {"hello": "help"}
    return str(param["hello"]) + goma


def Sumbycat(request):
    s_data =Suitoh.objects.all()
    total = 0
    for item in s_data:
        total += item.out_cost


    category_list = []
    category_data = Category.objects.all()

    for item in category_data:
        category_list.append(item.category_name)
    dict = {}
    for i, item in enumerate(category_list):
        category_total = Suitoh.objects.filter(cat__category_name=category_list[i]).aggregate(sum=models.Sum('out_cost'))['sum']
        if category_total != None:
            a = {'total':category_total, 'ratio': round((category_total/total)*100, 2)}
            dict[item]= a
        else:
            a = {'total': 0, 'ratio': 0}
            dict[item] = a


    # context = {'dict':sumbycats}
    a= {"aa":"aaa","xx":'xxxx'}
    b = {"aa":"bbb","xx":'xxxx'}
    #con = {"dict":{'a':a,'b':b}}
    con = {'dict': dict}
    #context = {'dict': sumbycats, 'lists': ['a', 'b', 'c', 'd']}
    return render(request, 'kakeibo_tuto/Sumbycat.html', con)


def test3(request):
    return render(request, 'kakeibo_tuto/Suitoh_list.html', {'hel': 'hev', })


class SuitohCreateView(CreateView):
    model = Suitoh

    form_class = SuitohForm

    success_url = reverse_lazy('kakeibo_tuto:create_done')


def create_done(request):
    return render(request, 'kakeibo_tuto/create_done.html')


class SuitohUpdateView(UpdateView):
    model = Suitoh

    form_class = SuitohForm

    success_url = reverse_lazy('kakeibo_tuto:update_done')


def update_done(request):
    return render(request, 'kakeibo_tuto/create_done.html')


class SuitohDeleteView(DeleteView):
    model = Suitoh
    success_url = reverse_lazy('kakeibo_tuto:delete_done')


def delete_done(request):
    return render(request, 'kakeibo_tuto/delete_done.html')
