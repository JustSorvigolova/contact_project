from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_full, name='main'),
    path('hook/', views.detail, name='hook'),
    path('list/', views.list_go, name='list'),
    path('new_contact',views.create, name='create'),
]