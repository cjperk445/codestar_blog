# Generated by Django 4.2.21 on 2025-06-07 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='exerpt',
            field=models.TextField(blank=True),
        ),
    ]
