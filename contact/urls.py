from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_full, name='main'),
    path('hook/', views.detail, name='hook'),
    path('new_contact',views.create, name='create'),
    path('post/<int:pk>', views.Post_Detail.as_view(), name='poster')
]