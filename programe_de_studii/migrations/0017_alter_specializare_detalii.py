# Generated by Django 5.0.2 on 2024-02-20 20:26

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("programe_de_studii", "0016_alter_orar_orar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="specializare",
            name="detalii",
            field=ckeditor.fields.RichTextField(
                blank=True, null=True, verbose_name="Detalii"
            ),
        ),
    ]