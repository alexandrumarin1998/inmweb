# Generated by Django 5.0.2 on 2024-02-18 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("programe_de_studii", "0002_codcor_specializare_detalii_specializare_imagine"),
    ]

    operations = [
        migrations.AddField(
            model_name="specializare",
            name="coduri_cor",
            field=models.ManyToManyField(to="programe_de_studii.codcor"),
        ),
    ]
