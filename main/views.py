from django.shortcuts import render, redirect
from .models import CompanyDB
from .forms import CompanyDBForm


def index(request):
    tasks = CompanyDB.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html', {'title': 'О нас'})


def add(request):
    if request.method == "POST":
        form = CompanyDBForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return 'Error! Form is invalid'
    form = CompanyDBForm()
    context = {'title': 'Добавление нового рабочего', 'form': form}
    return render(request, 'main/add.html', context)


def delete(request, id):
    emp = CompanyDB.objects.get(pk=id)
    emp.delete()
    return redirect('/')
