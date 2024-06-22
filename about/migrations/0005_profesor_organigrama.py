# Generated by Django 5.0.2 on 2024-02-19 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("about", "0004_remove_profesor_obligatoriu"),
    ]

    operations = [
        migrations.AddField(
            model_name="profesor",
            name="organigrama",
            field=models.CharField(
                choices=[
                    (" ", " "),
                    ("CD", "CD"),
                    ("DD", "DD"),
                    ("RPC", "RPC"),
                    ("CDMG", "CDMG"),
                    ("CUPP", "CUPP"),
                    ("Necunoscut", "Necunoscut"),
                    ("CTFMI", "CTFMI"),
                    ("CRDMTP", "CRDMTP"),
                ],
                default=(" ", " "),
                max_length=10,
            ),
        ),
    ]