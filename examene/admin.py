from django.contrib import admin

from .models import (
    Examen,
    Document
)

admin.site.register(Examen)
admin.site.register(Document)