# Generated by Django 5.0.2 on 2024-02-19 18:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("programe_de_studii", "0012_curs_limba"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="specializare",
            name="plan_de_invatamant",
        ),
        migrations.CreateModel(
            name="PlanDeInvatamant",
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
                (
                    "fisier",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="programe_de_studii/planuri_de_invatamant/",
                    ),
                ),
                (
                    "an",
                    models.IntegerField(
                        choices=[
                            (1, "Anul 1"),
                            (2, "Anul 2"),
                            (3, "Anul 3"),
                            (4, "Anul 4"),
                        ],
                        default=1,
                    ),
                ),
                (
                    "specializare",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="planuri",
                        to="programe_de_studii.specializare",
                    ),
                ),
            ],
            options={
                "verbose_name": "Plan de invatamant",
                "verbose_name_plural": "Planuri de invatamant",
            },
        ),
    ]