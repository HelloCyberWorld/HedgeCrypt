# Generated by Django 4.1.1 on 2022-09-26 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0008_alter_post_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="uploads/"),
        ),
    ]