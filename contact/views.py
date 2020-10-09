from django.shortcuts import render, redirect
from .models import Contac
from .forms import ContacForm


def list_go(request):
    all_of_list = Contac.objects.all()
    return render(request, 'contact/list.html', {'all_of_list': all_of_list})


def detail(request):
    show_all_detail = Contac.objects.all()
    return render(request, 'contact/detail.html', {'show_all': show_all_detail})


def main_full(request):
    hello_world = 'Hello World'
    return render(request, 'contact/base.html', {'hi': hello_world})


def create(request):
    error = ''
    if request.method == 'POST':
        form = ContacForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = 'Error'
    form = ContacForm()
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'contact/create.html', data)

