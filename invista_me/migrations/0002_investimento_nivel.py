# Generated by Django 4.1.5 on 2023-02-01 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("invista_me", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="investimento",
            name="nivel",
            field=models.IntegerField(default=1),
        ),
    ]