# Generated by Django 4.1.3 on 2022-12-09 10:52

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "Categories"},
        ),
        migrations.AlterField(
            model_name="category",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="uploads/category_photos/"
            ),
        ),
        migrations.CreateModel(
            name="Product",
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
                (
                    "product_image",
                    models.ImageField(
                        blank=True, null=True, upload_to="uploads/product_photos/"
                    ),
                ),
                ("quantity", models.IntegerField()),
                ("original_price", models.FloatField()),
                ("selling_price", models.FloatField()),
                ("tag", models.CharField(max_length=150)),
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
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="store.category"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Products",
            },
        ),
    ]
