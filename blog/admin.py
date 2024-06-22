from django.contrib import admin
from django.http import HttpRequest

# Register your models here.

from .models import (
    Post,
    Link,
    Slider
)

admin.site.register(Post)

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
            if Link.objects.count() > 4:
                self.message_user(request, "Only four entries allowed. Save operation aborted.")
            else:
                super().save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        return False
    
@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
            if Slider.objects.count() > 1:
                self.message_user(request, "Only one entry allowed. Save operation aborted.")
            else:
                super().save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        return False