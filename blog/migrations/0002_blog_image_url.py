# Generated by Django 5.0.2 on 2025-06-07 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image_url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
