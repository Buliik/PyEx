from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from strelnice.models import Zakaznik
from strelnice.models import Zamestnanec
from strelnice.models import Prostor
from strelnice.models import Zbran
from strelnice.models import Strelba
from strelnice.models import Rezervace
from strelnice.forms import RazeSearchForm, RokSearchForm, VzdalenostSearchForm, ZamDateSearchForm, ZakDateSearchForm, StrDateSearchForm


def zam_name(request, idZam):
    zamestnanec = get_object_or_404(Zamestnanec, pk=idZam)
    return render(request, "zam_name.html", {'zamestnanec': zamestnanec})


def zam_index(request):
    zamestnanci = Zamestnanec.objects.all().order_by("prijmeni")
    return render(request, "zam_index.html", {'zamestnanci': zamestnanci})


def zam_date_search(request):
    if request.method == "POST":
        form = ZamDateSearchForm(request.POST)
        if form.is_valid():
            f = form.cleaned_data['from_date']
            t = form.cleaned_data['to_date']
            zamestnanci = Zamestnanec.objects.filter(datum_narozeni__gte=f, datum_narozeni__lte=t)
        else:
            zamestnanci = None
    else:
        zamestnanci = None
        form = ZamDateSearchForm()
    return render(request, "zam_narozen_search.html", {'zamestnanci':zamestnanci, 'form':form})


def zak_name(request, idZak):
    zakaznik = get_object_or_404(Zakaznik, pk=idZak)
    return render(request, "zak_name.html", {'zakaznik': zakaznik})


def zak_index(request):
    zakaznici = Zakaznik.objects.all().order_by("prijmeni")
    return render(request, "zak_index.html", {'zakaznici': zakaznici})


def zak_date_search(request):
    if request.method == "POST":
        form = ZakDateSearchForm(request.POST)
        if form.is_valid():
            f = form.cleaned_data['from_date']
            t = form.cleaned_data['to_date']
            zakaznici = Zakaznik.objects.filter(datum_narozeni__gte=f, datum_narozeni__lte=t)
        else:
            zakaznici = None
    else:
        zakaznici = None
        form = ZakDateSearchForm()
    return render(request, "zak_narozen_search.html", {'zakaznici':zakaznici, 'form':form})


def spr_name(request, idSpr):
    prostor = get_object_or_404(Prostor, pk=idSpr)
    return render(request, "spr_name.html", {'prostor': prostor})


def spr_index(request):
    prostory = Prostor.objects.all().order_by("idSpr")
    return render(request, "spr_index.html", {'prostory': prostory})


def vzdalenost_search(request):
    if request.method == "POST":
        form = VzdalenostSearchForm(request.POST)
        if form.is_valid():
            f = form.cleaned_data['from_vzdalenost']
            t = form.cleaned_data['to_vzdalenost']
            prostory = Prostor.objects.filter(vzdalenost__gte=f, vzdalenost__lte=t)
        else:
            prostory = None
    else:
        prostory = None
        form = VzdalenostSearchForm()
    return render(request, "vzdalenost_search.html", {'prostory':prostory, 'form':form})

def zbr_name(request, idZbr):
    zbran = get_object_or_404(Zbran, pk=idZbr)
    return render(request, "zbr_name.html", {'zbran': zbran})


def zbr_index(request):
    zbrane = Zbran.objects.all().order_by("nazev")
    return render(request, "zbr_index.html", {'zbrane': zbrane})


def raze_search(request):
    if request.method == "POST":
        form = RazeSearchForm(request.POST)
        if form.is_valid():
            f = form.cleaned_data['from_raze']
            t = form.cleaned_data['to_raze']
            zbrane = Zbran.objects.filter(raze__gte=f, raze__lte=t)
        else:
            zbrane = None
    else:
        zbrane = None
        form = RazeSearchForm()
    return render(request, "raze_search.html", {'zbrane':zbrane, 'form':form})


def rok_search(request):
    if request.method == "POST":
        form = RokSearchForm(request.POST)
        if form.is_valid():
            f = form.cleaned_data['from_rok']
            t = form.cleaned_data['to_rok']
            zbrane = Zbran.objects.filter(rok_vyroby__gte=f, rok_vyroby__lte=t)
        else:
            zbrane = None
    else:
        zbrane = None
        form = RokSearchForm()
    return render(request, "rok_search.html", {'zbrane':zbrane, 'form':form})



def str_name(request, idStr):
    strelba = get_object_or_404(Strelba, pk=idStr)
    return render(request, "str_name.html", {'strelba': strelba})


def str_index(request):
    strelby = Strelba.objects.all().order_by("idStr")
    return render(request, "str_index.html", {'strelby': strelby})


def str_date_search(request):
    if request.method == "POST":
        form = StrDateSearchForm(request.POST)
        if form.is_valid():
            f = form.cleaned_data['from_date']
            t = form.cleaned_data['to_date']
            strelby = Strelba.objects.filter(zacatek__gte=f, zacatek__lte=t)
        else:
            strelby = None
    else:
        strelby = None
        form = StrDateSearchForm()
    return render(request, "str_date_search.html", {'strelby':strelby, 'form':form})


def rez_name(request, idRez):
    rezervace = get_object_or_404(Rezervace, pk=idRez)
    return render(request, "rez_name.html", {'rezervace': rezervace})


def rez_index(request):
    rezervaces = Rezervace.objects.all().order_by("idRez")
    return render(request, "rez_index.html", {'rezervace': rezervaces})
