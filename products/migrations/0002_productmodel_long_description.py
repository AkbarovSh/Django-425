# Generated by Django 5.0 on 2023-12-13 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='long_description',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
