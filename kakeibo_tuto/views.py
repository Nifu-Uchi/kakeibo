from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Category,Ranks,Suitoh
from . forms import SuitohForm
from django.urls import reverse_lazy

class SuitohListView(ListView):

    model = Suitoh
    template_name = 'kakeibo_tuto/Suitoh_list.html'

    '''全取得'''
    def queryset(self):
        return Suitoh.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        context["foo"] = test('a')
        return context
def test(goma):
    param = {'object_list':Suitoh.objects.all(),
             'hello':'django',}
    return (str(param["hello"])+goma)




def test3(request):
        return render(request,'kakeibo_tuto/Suitoh_list.html',{'hel':'hev',})

class SuitohCreateView(CreateView):

    model = Suitoh

    form_class = SuitohForm

    success_url = reverse_lazy('kakeibo_tuto:create_done')


def create_done(request):

    return render(request,'kakeibo_tuto/create_done.html')



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