from django.urls import path

from . import views

app_name = 'kakeibo_tuto'

urlpatterns = [
    path('Suitoh_list/', views.SuitohListView.as_view(), name='Suitoh_list'),
    path('Suitoh_create/', views.SuitohCreateView.as_view(), name='add'),
    path('create_done/', views.create_done, name='create_done'),
    path('update/<int:pk>/', views.SuitohUpdateView.as_view(), name='Suitoh_update'),
    path('update_done/', views.update_done, name='update_done'),
    path('delete/<int:pk>/', views.SuitohDeleteView.as_view(), name='Suitoh_delete'),
    path('delete_done/', views.delete_done, name='delete_done'),
    ]