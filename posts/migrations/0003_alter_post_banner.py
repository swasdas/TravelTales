# Generated by Django 4.2.22 on 2025-06-14 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0002_post_banner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="banner",
            field=models.ImageField(blank=True, default="default.jpg", upload_to=""),
        ),
    ]
