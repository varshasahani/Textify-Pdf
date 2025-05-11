from django.urls import path
from . import views

urlpatterns = [
    path('uploadfile/', views.upload_file, name='upload_file'),
    path('success/', views.success, name='success'),
    path('', views.receipt_list, name='receipt_list'),
    ]