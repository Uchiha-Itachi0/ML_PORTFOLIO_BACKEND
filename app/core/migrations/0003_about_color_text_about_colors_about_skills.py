# Generated by Django 5.0.6 on 2024-07-02 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='color_text',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='about',
            name='colors',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='about',
            name='skills',
            field=models.JSONField(default=list),
        ),
    ]
