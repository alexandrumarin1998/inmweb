# Generated by Django 4.1.4 on 2023-03-15 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='folder',
            name='files',
        ),
        migrations.RemoveField(
            model_name='folder',
            name='parent',
        ),
        migrations.DeleteModel(
            name='File',
        ),
        migrations.DeleteModel(
            name='Folder',
        ),
    ]
