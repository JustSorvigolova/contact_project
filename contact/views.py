from django.shortcuts import render
from .models import Contac


def list_go(request):
    all_of_list = Contac.objects.all()
    return render(request, 'contact/list.html', {'all_of_list': all_of_list})


def detail(request):
    show_all_detail = Contac.objects.all()
    return render(request, 'contact/detail.html', {'show_all': show_all_detail})