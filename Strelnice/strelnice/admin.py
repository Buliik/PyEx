from django.contrib import admin
from .models import Zamestnanec
from .models import Zakaznik
from .models import Prostor
from .models import Zbran
from .models import Strelba
from .models import Rezervace

admin.site.register(Zamestnanec)
admin.site.register(Zakaznik)
admin.site.register(Prostor)
admin.site.register(Zbran)
admin.site.register(Strelba)
admin.site.register(Rezervace)

# Register your models here.
