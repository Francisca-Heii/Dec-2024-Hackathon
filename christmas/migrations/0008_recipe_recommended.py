# Generated by Django 4.2.17 on 2024-12-14 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('christmas', '0007_recipe_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recommended',
            field=models.BooleanField(default=False),
        ),
    ]