from django.shortcuts import render
from .models import Table, Reservation


def index(request):
    hello = Table.objects.all()
    return render(request, 'index.html', {'bitch': hello})


def index_detail(request, pk):
    what = Table.objects.get(pk=pk)
    if request.method == "POST":
        party = request.POST.get('hello')
        spot = request.POST.get('date')
        reserv = Reservation(table=what, party=party, spot=spot)
        reserv.save()
    return render(request, 'index_detail.html', {'what': what})


def to_reserv(request):
    table = Table.objects.get(pk=1)
    print(request)
    if request.method == "POST":
        party = request.POST.get('hello')
        spot = request.POST.get('date')
        reserv = Reservation(table=table, party=party, spot=spot)
        reserv.save()
    return render(request, 'reserv.html', {})