# Generated by Django 5.0.2 on 2024-02-18 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("about", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profesor",
            name="poza",
            field=models.ImageField(
                blank=True, null=True, upload_to="about/pictures/", verbose_name="Poza"
            ),
        ),
    ]
