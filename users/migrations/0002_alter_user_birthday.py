# Generated by Django 4.2.5 on 2023-09-18 17:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="birthday",
            field=models.DateField(blank=True, null=True),
        ),
    ]
