# Generated by Django 5.0.7 on 2024-07-28 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_about_created_date_about_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='title',
            field=models.CharField(max_length=70),
        ),
    ]