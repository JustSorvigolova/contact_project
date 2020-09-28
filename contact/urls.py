from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_go, name='main'),
    path('hook/', views.detail, name='hook')
]