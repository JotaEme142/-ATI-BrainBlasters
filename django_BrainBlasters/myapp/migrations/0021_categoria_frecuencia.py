# Generated by Django 5.0.7 on 2024-08-14 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_alter_trivia_opcion_img1_alter_trivia_opcion_img2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='frecuencia',
            field=models.IntegerField(default=30000),
        ),
    ]