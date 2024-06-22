from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    titlu = models.CharField(max_length=100, unique=True)
    imagine = models.ImageField(upload_to='blog/images/', null=True)
    continut = RichTextField(null=True, blank=True, verbose_name="Continut")
    data_creare = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titlu
    
    class Meta:
        verbose_name = "Anunt"
        verbose_name_plural = "Anunturi"
        ordering = ['-data_creare']

class Link(models.Model):
    titlu = models.CharField(max_length=100, unique=True)
    url = models.CharField(max_length=1000)
    plasament = models.IntegerField(choices=[
        (1, "Link 1"),
        (2, "Link 2"),
        (3, "Link 3"),
        (4, "Link buton")
    ], unique=True)

    def __str__(self):
        return self.titlu

    class Meta:
        verbose_name = "Link"
        verbose_name_plural = "Link-uri"

class Slider(models.Model):
    imagine1 = models.FileField(upload_to='blog/images/', null=True, name="Imagine 1")
    imagine2 = models.FileField(upload_to='blog/images/', null=True, name="Imagine 2")
    titlu = models.CharField(max_length=50)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.titlu

    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = "Slidere"

