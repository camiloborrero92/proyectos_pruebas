# Generated by Django 3.1.5 on 2021-02-13 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='nombre',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
