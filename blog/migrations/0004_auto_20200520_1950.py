# Generated by Django 3.0.6 on 2020-05-20 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogpagegalleryimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='intro',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]