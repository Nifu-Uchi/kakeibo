from django.urls import path

from . import views

app_name = 'kakeibo_tuto'

urlpatterns = [
    path('Suitoh_list/', views.SuitohListView.as_view(), name='Suitoh_list'),
    ]