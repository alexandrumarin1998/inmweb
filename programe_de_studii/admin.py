from django.contrib import admin

from .models import (
    Specializare,
    Orar,
    Curs,
    CodCor,
    PlanDeInvatamant
)

admin.site.register(Specializare)
admin.site.register(Orar)
admin.site.register(Curs)
admin.site.register(CodCor)
admin.site.register(PlanDeInvatamant)
