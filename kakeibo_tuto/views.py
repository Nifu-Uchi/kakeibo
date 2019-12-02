from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Category, Ranks, Suitoh
from django.db import models
from .forms import SuitohForm
from django.urls import reverse_lazy

from urllib import request as req

from urllib import parse
import bs4
import random
import calendar
from django.db.models import Sum

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


def calview(request):

    return render(request, 'kakeibo_tuto/calen.html', {'cat':'日別支出'})

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

    #dict_s = sorted(dict.items().total, key=lambda x: x[1])
    ##月ごとの集計
    date_list = []
    for i in s_data:
        date_list.append((i.data.strftime('%Y/%m/%d')[:7]))


    date_list_s = list(set(date_list))
    date_list_s.sort(reverse=False)

    monthly_sum = []
    sumbymonth ={}
    for i in date_list_s:
        y,m = i.split("/")
        month_range = calendar.monthrange(int(y), int(m))[1]
        first_date = y + '-' + m +'-' + '01'
        last_date = y + '-' + m + '-' + str(month_range)
        total_of_month = Suitoh.objects.filter(data__range=(first_date, last_date)).aggregate(sum=models.Sum('out_cost'))['sum']
        sumbym ={'y':y,'m':m,'total':total_of_month}
        sumbymonth[i] = sumbym

    con = {'dict': dict,'sbm':sumbymonth}

    return render(request, 'kakeibo_tuto/Sumbycat.html', con)

def randcat(request):
    keyword = '猫かわいい'
    urlKeyword = parse.quote(keyword)
    url = 'https://www.google.com/search?hl=jp&q=' + urlKeyword + '&btnG=Google+Search&tbs=0&safe=off&tbm=isch'

    headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0", }
    requesta = req.Request(url=url, headers=headers)
    page = req.urlopen(requesta)

    html = page.read().decode('utf-8')
    html = bs4.BeautifulSoup(html, "html.parser")
    elems = html.select('.rg_meta.notranslate')
    counter = 0
    cats = []
    for ele in elems:
        ele = ele.contents[0].replace('"', '').split(',')
        eledict = dict()
        for e in ele:
            num = e.find(':')
            eledict[e[0:num]] = e[num + 1:]
        catU = eledict['ou']
        cats.append(catU)
    i = random.randrange(len(cats)-1)
    return render(request, 'kakeibo_tuto/randcat.html', {'cat':cats[i],'keyword':keyword})

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
