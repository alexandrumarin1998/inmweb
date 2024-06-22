"""upg_ime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from upg_ime import views
from about import views as about_views
from programe_de_studii import views as specializari_views
from examene import views as examene_views
from blog import views as blog_views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

handler404 = 'upg_ime.views.error_404'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="acasa"),
    path('contact', views.contact, name="contact"),
    path('prezentare', about_views.prezentare, name="prezentare"),
    path('organizare', about_views.organizare, name="organizare"),
    path('membri', about_views.membri, name="membri"),
    path('burse', views.burse, name="burse"),
    path('specializari', specializari_views.specializari, name='specializari'),
    path('specializari/specializare/<str:name>', specializari_views.specializare, name='specializare'),
    path('examene', examene_views.examene, name='examene'),
    path('examene_continut', examene_views.examene_continut, name='examene_continut'),
    path('articol/<str:name>', blog_views.articol, name='articol')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
