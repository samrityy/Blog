# Generated by Django 4.0.10 on 2023-09-29 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_images_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
