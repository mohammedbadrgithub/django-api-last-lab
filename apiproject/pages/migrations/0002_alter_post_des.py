# Generated by Django 4.1.7 on 2023-03-10 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='des',
            field=models.TextField(blank=True, null=True),
        ),
    ]
