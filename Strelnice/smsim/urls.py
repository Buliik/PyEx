"""smsim URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import strelnice.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^zamestnanec/(?P<idZam>\d+)', strelnice.views.zam_name, name="zam_name"),
    url(r'^zamestnanec/index/', strelnice.views.zam_index, name="zam_index"),
    url(r'^zamestnanec/search/', strelnice.views.zam_date_search, name="zam_date_search"),
    url(r'^zakaznik/(?P<idZak>\d+)', strelnice.views.zak_name, name="zak_name"),
    url(r'^zakaznik/index/', strelnice.views.zak_index, name="zak_index"),
    url(r'^zakaznik/search/', strelnice.views.zak_date_search, name="zak_narozen_search"),
    url(r'^prostor/(?P<idSpr>\d+)', strelnice.views.spr_name, name="spr_name"),
    url(r'^prostor/search/', strelnice.views.vzdalenost_search, name="vzdalenost_search"),
    url(r'^prostor/index/', strelnice.views.spr_index, name="spr_index"),
    url(r'^zbran/(?P<idZbr>\d+)', strelnice.views.zbr_name, name="zbr_name"),
    url(r'^zbran/index/', strelnice.views.zbr_index, name="zbr_index"),
    url(r'^zbran/search/', strelnice.views.raze_search, name="raze_search"),
    url(r'^zbran/search2/', strelnice.views.rok_search, name="rok_search"),
    url(r'^strelba/(?P<idStr>\d+)', strelnice.views.str_name, name="str_name"),
    url(r'^strelba/index/', strelnice.views.str_index, name="str_index"),
    url(r'^strelba/search/', strelnice.views.str_date_search, name="str_date_search"),
    url(r'^rezervace/(?P<idRez>\d+)', strelnice.views.rez_name, name="rez_name"),
    url(r'^rezervace/index/', strelnice.views.rez_index, name="rez_index"),
]
