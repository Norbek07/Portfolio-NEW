# Generated by Django 5.0.7 on 2024-07-28 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_about_alter_portfolio_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='about',
            name='image',
            field=models.ImageField(default='Images/about/default_image.jpg', upload_to='Images/about'),
        ),
    ]
