from django.shortcuts import render, redirect
from .models import *
from .forms import *


def index(request):
    return render(request, 'main/index.html', {'title': 'Главная страница сайта'})


def about(request):
    return render(request, 'main/about.html', {'title': 'О нас'})


def add(request):
    return render(request, 'main/add.html')


def delete_breaks(request, id):
    emp = MachineBreakdowns.objects.get(pk=id)
    emp.delete()
    return redirect('/')


def month(request):
    if request.method == "POST":
        form1 = MonthForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('/view/month_')
        else:
            return 'Error! Form is invalid'
    form1 = MonthForm()
    context = {'title': 'Добавление нового месяца', 'form1': form1}
    return render(request, 'main/add/month.html', context)


def month_(request):
    task = Month.objects.all()
    return render(request, 'main/view/month_.html', {'task': task})


def breaks(request):
    if request.method == "POST":
        form1 = BreaksForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('/')
        else:
            return 'Error! Form is invalid'
    form1 = BreaksForm()
    context = {'title': 'Добавление нового месяца', 'form1': form1}
    return render(request, 'main/add/breaks.html', context)


def breaks_(request):
    task = MachineBreakdowns.objects.all()
    return render(request, 'main/view/breaks_.html', {'task': task})


def coupon(request):
    if request.method == "POST":
        form1 = CouponForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('/')
        else:
            return 'Error! Form is invalid'
    form1 = CouponForm()
    context = {'title': 'Добавление нового месяца', 'form1': form1}
    return render(request, 'main/add/coupon.html', context)


def coupon_(request):
    task = Coupon.objects.all()
    return render(request, 'main/view/coupon_.html', {'task': task})


def employer(request):
    if request.method == "POST":
        form1 = EmployerForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('/')
        else:
            return 'Error! Form is invalid'
    form1 = EmployerForm()
    context = {'title': 'Добавление нового месяца', 'form1': form1}
    return render(request, 'main/add/employer.html', context)


def employer_(request):
    task = Employer.objects.all()
    return render(request, 'main/view/employer_.html', {'task': task})


def history(request):
    if request.method == "POST":
        form1 = HistoryForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('/')
        else:
            return 'Error! Form is invalid'
    form1 = HistoryForm()
    context = {'title': 'Добавление нового месяца', 'form1': form1}
    return render(request, 'main/add/history.html', context)


def history_(request):
    task = HistoryPromotions.objects.all()
    return render(request, 'main/view/history_.html', {'task': task})


def hospital(request):
    if request.method == "POST":
        form1 = HospitalForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('/')
        else:
            return 'Error! Form is invalid'
    form1 = HospitalForm()
    context = {'title': 'Добавление нового месяца', 'form1': form1}
    return render(request, 'main/add/hospital.html', context)


def hospital_(request):
    task = HospitalTrip.objects.all()
    return render(request, 'main/view/hospital_.html', {'task': task})


def machine(request):
    if request.method == "POST":
        form1 = MachineForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('/')
        else:
            return 'Error! Form is invalid'
    form1 = MachineForm()
    context = {'title': 'Добавление нового месяца', 'form1': form1}
    return render(request, 'main/add/machine.html', context)


def machine_(request):
    task = WorkingMachine.objects.all()
    return render(request, 'main/view/machine_.html', {'task': task})


def oil(request):
    if request.method == "POST":
        form1 = OilForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('/')
        else:
            return 'Error! Form is invalid'
    form1 = OilForm()
    context = {'title': 'Добавление нового месяца', 'form1': form1}
    return render(request, 'main/add/oil.html', context)


def oil_(request):
    task = OilChange.objects.all()
    return render(request, 'main/view/oil_.html', {'task': task})


def production(request):
    if request.method == "POST":
        form1 = ProductionForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('/')
        else:
            return 'Error! Form is invalid'
    form1 = ProductionForm()
    context = {'title': 'Добавление нового месяца', 'form1': form1}
    return render(request, 'main/add/production.html', context)


def production_(request):
    task = ProductionRate.objects.all()
    return render(request, 'main/view/production_.html', {'task': task})


def subdivision(request):
    if request.method == "POST":
        form1 = SubdivisionForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('/')
        else:
            return 'Error! Form is invalid'
    form1 = SubdivisionForm()
    context = {'title': 'Добавление нового месяца', 'form1': form1}
    return render(request, 'main/add/subdivision.html', context)


def subdivision_(request):
    task = Subdivision.objects.all()
    return render(request, 'main/view/subdivision_.html', {'task': task})


def table(request):
    if request.method == "POST":
        form1 = TableForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('/')
        else:
            return 'Error! Form is invalid'
    form1 = TableForm()
    context = {'title': 'Добавление нового месяца', 'form1': form1}
    return render(request, 'main/add/table.html', context)


def table_(request):
    task = TableSheet.objects.all()
    return render(request, 'main/view/table_.html', {'task': task})


def trip(request):
    if request.method == "POST":
        form1 = TripForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('/')
        else:
            return 'Error! Form is invalid'
    form1 = TripForm()
    context = {'title': 'Добавление нового месяца', 'form1': form1}
    return render(request, 'main/add/trip.html', context)


def trip_(request):
    task = Trip.objects.all()
    return render(request, 'main/view/trip_.html', {'task': task})


def vacation(request):
    if request.method == "POST":
        form1 = VacationForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('/')
        else:
            return 'Error! Form is invalid'
    form1 = VacationForm()
    context = {'title': 'Добавление нового месяца', 'form1': form1}
    return render(request, 'main/add/vacation.html', context)


def vacation_(request):
    task = Vacation.objects.all()
    return render(request, 'main/view/vacation_.html', {'task': task})


def position(request):
    if request.method == "POST":
        form1 = PositionForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('/')
        else:
            return 'Error! Form is invalid'
    form1 = PositionForm()
    context = {'title': 'Добавление нового месяца', 'form1': form1}
    return render(request, 'main/add/position.html', context)


def position_(request):
    task = PositionEm.objects.all()
    return render(request, 'main/view/position_.html', {'task': task})
