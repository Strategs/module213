# Generated by Django 4.2.5 on 2023-10-12 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quoteapp', '0002_rename_autor_quote_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
