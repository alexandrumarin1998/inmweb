# Generated by Django 5.0.2 on 2024-02-22 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("about", "0005_profesor_organigrama"),
        ("examene", "0002_examene_anul"),
        ("programe_de_studii", "0017_alter_specializare_detalii"),
    ]

    operations = [
        migrations.CreateModel(
            name="Document",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fisier", models.FileField(null=True, upload_to="examene/documente/")),
                ("denumire", models.CharField(max_length=150)),
            ],
            options={
                "verbose_name": "Document",
                "verbose_name_plural": "Documente",
            },
        ),
        migrations.RenameModel(
            old_name="Examene",
            new_name="Examen",
        ),
    ]
