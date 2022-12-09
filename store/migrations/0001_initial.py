# Generated by Django 4.1.3 on 2022-12-09 10:42

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField(max_length=500)),
                (
                    "slug",
                    autoslug.fields.AutoSlugField(
                        editable=False, populate_from="title"
                    ),
                ),
                ("image", models.ImageField(upload_to="uploads/category_photos/")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.BooleanField(default=False, help_text="0=default ,1=Hidden"),
                ),
                (
                    "trending",
                    models.BooleanField(
                        default=False, help_text="0=default ,1=Trending"
                    ),
                ),
                ("meta_title", models.CharField(max_length=150)),
                ("meta_keywords", models.CharField(max_length=150)),
                ("meta_description", models.TextField(max_length=500)),
            ],
        ),
    ]
