# Generated by Django 5.0 on 2024-01-04 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movieapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="img",
            field=models.ImageField(default="img", upload_to="gallery"),
            preserve_default=False,
        ),
    ]
