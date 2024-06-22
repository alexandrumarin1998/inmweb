from django.db import models
from django.conf import settings

class Profesor(models.Model):
    nume = models.CharField(max_length=50)
    prenume = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)

    grad = models.CharField(max_length=30)
    birou = models.CharField(max_length=10)

    poza = models.ImageField(upload_to='about/pictures/', null=True, blank=True, verbose_name="Poza")
    cv = models.FileField(upload_to='about/cvs/', null=True, blank=True, verbose_name="CV")

    organigrama = models.CharField(max_length = 10, choices=[(" ", " "),
                                                             ("CD", "CD"),
                                                             ("DD", "DD"),
                                                             ("RPC", "RPC"),
                                                             ("CDMG", "CDMG"),
                                                             ("CUPP", "CUPP"),
                                                             ("Necunoscut", "Necunoscut"),
                                                             ("CTFMI", "CTFMI"),
                                                             ("CRDMTP", "CRDMTP")],
                                                     default = (" "," "))

    def __str__(self):
        return self.nume + " " + self.prenume
    
    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesori"
        
    
