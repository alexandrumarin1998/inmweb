from django.db import models

from about.models import Profesor

from ckeditor.fields import RichTextField

class CodCor(models.Model):
    
    denumire = models.CharField(max_length=50)
    cod = models.CharField(max_length=50)

    def __str__(self):
        return self.denumire + " : " + self.cod

    class Meta:
        verbose_name = "Coduri COR"
        verbose_name_plural = "Coduri COR"

class Specializare(models.Model):

    nume = models.CharField(max_length=50, unique=True)
    acronim = models.CharField(max_length=20, default="")
    imagine = models.ImageField(upload_to='programe_de_studii/images/', null=True, blank=True)
    ciclu = models.CharField(max_length=50, choices=[('Licenta', 'Licenta'), ('Master', 'Master')], default='Licenta')
    detalii = RichTextField(null=True, blank=True, verbose_name="Detalii")
    coduri_cor = models.ManyToManyField(CodCor, blank=True)
    numar_locuri = models.IntegerField(default=0, verbose_name="Numar de locuri")

    def __str__(self):
        return self.nume + " - " + self.ciclu

    class Meta:
        verbose_name = "Program de studii"
        verbose_name_plural = "Programe de studii"

class PlanDeInvatamant(models.Model):

    fisier = models.FileField(upload_to='programe_de_studii/planuri_de_invatamant/', null=True)
    specializare = models.ForeignKey(Specializare, on_delete=models.CASCADE, related_name='planuri')
    an = models.IntegerField( choices=[(1, 'Anul 1'), (2, 'Anul 2'), (3, 'Anul 3'), (4, 'Anul 4')], default=1, unique=True)

    def __str__(self):
        return "Plan de invatamant " + self.specializare.nume + " - Anul " + str(self.an)
    
    class Meta:
        verbose_name = "Plan de invatamant"
        verbose_name_plural = "Planuri de invatamant"

class Orar(models.Model):

    specializare = models.ForeignKey(Specializare, on_delete=models.CASCADE, related_name='orare')
    an = models.IntegerField( choices=[(1, 'Anul 1'), (2, 'Anul 2'), (3, 'Anul 3'), (4, 'Anul 4')], default=1)
    semestru = models.IntegerField( choices=[(1, 'Semestrul 1'), (2, 'Semestrul 2')], default=1)
    orar = models.FileField(upload_to='programe_de_studii/orare/', null=True, verbose_name="Orar")

    def __str__(self):
        return self.specializare.nume + " - Anul " + str(self.an) + " - Semestrul " + str(self.semestru)

    class Meta:
        verbose_name = "Orar"
        verbose_name_plural = "Orare"

class Curs(models.Model):

    specializare = models.ForeignKey(Specializare, on_delete=models.CASCADE, related_name='cursuri')
    an = models.IntegerField( choices=[(1, 'Anul 1'), (2, 'Anul 2'), (3, 'Anul 3'), (4, 'Anul 4')], default=1)
    semestru = models.IntegerField( choices=[(1, 'Semestrul 1'), (2, 'Semestrul 2')], default=1)
    nume = models.CharField(max_length=50)
    profesori = models.ManyToManyField(Profesor)
    fisa_disciplinei = models.FileField(upload_to='programe_de_studii/fise_disciplina/', null=True, blank=True, verbose_name="Fisa disciplinei")
    obligatoriu = models.BooleanField(choices=[(True, "Obligatoriu"), (False, "Optional")], default=True)
    limba = models.CharField(max_length=50, default="Romana")

    def __str__(self):
        return self.nume + " - " + self.specializare.nume + " - Anul " + str(self.an) + " - Semestrul " + str(self.semestru)

    class Meta:
        verbose_name = "Curs"
        verbose_name_plural = "Cursuri"