# Generated by Django 5.0.2 on 2024-02-18 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("programe_de_studii", "0004_alter_specializare_coduri_cor"),
    ]

    operations = [
        migrations.AddField(
            model_name="specializare",
            name="numar_locuri",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Numar de locuri"
            ),
        ),
    ]