# Generated by Django 5.0.2 on 2024-10-09 20:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("finder", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="img",
            name="distance",
        ),
        migrations.AddField(
            model_name="img",
            name="description",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="img",
            name="name",
            field=models.CharField(default="", max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="img",
            name="photo",
            field=models.ImageField(upload_to="ImagesLoaded"),
        ),
    ]
