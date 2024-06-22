from django.contrib import admin
from django.shortcuts import redirect

from .models import Files

@admin.register(Files)
class FilesAdmin(admin.ModelAdmin):

    def changelist_view(self, request):
        return redirect('/filemanager')

    
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
