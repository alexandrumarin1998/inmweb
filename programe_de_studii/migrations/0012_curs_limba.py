# Generated by Django 5.0.2 on 2024-02-18 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("programe_de_studii", "0011_curs_obligatoriu"),
    ]

    operations = [
        migrations.AddField(
            model_name="curs",
            name="limba",
            field=models.CharField(default="Romana", max_length=50),
        ),
    ]
