from django.db import models
from about.models import Profesor
from programe_de_studii.models import Specializare

# Create your models here.
class Examen(models.Model):
    
    denumire = models.CharField(max_length=300)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name='profesor')
    student = models.CharField(max_length=100)
    specializare = models.ForeignKey(Specializare, on_delete=models.CASCADE, related_name='profesor')
    text = models.CharField(max_length=10)
    anul = models.IntegerField(default = 0, choices =
        [(0, "2020 - 2021"),
         (1, "2021 - 2022"),
         (2, "2022 - 2023"),
         (3, "2023 - 2024"),
         (4, "2024 - 2025"),
         (5, "2025 - 2026"),
         (6, "2026 - 2027"),
         (7, "2027 - 2028")]
    )

    def __str__(self):
        return self.denumire + " - " + self.student

    class Meta:
        verbose_name = "Examen"
        verbose_name_plural = "Examene"

class Document(models.Model):

    fisier = models.FileField(upload_to='examene/documente/', null=True)
    denumire = models.CharField(max_length=150)
    
    def __str__(self):
        return self.denumire

    class Meta:
        verbose_name = "Document"
        verbose_name_plural = "Documente"