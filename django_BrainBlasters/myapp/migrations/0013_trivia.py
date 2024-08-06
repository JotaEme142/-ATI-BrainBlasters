# Generated by Django 5.0.7 on 2024-08-03 23:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_delete_trivia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trivia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.BooleanField(default=False)),
                ('pregunta', models.CharField(max_length=100, null=True)),
                ('opcion_txt1', models.CharField(max_length=100, null=True)),
                ('opcion_txt2', models.CharField(max_length=100, null=True)),
                ('opcion_txt3', models.CharField(max_length=100, null=True)),
                ('opcion_txt4', models.CharField(max_length=100, null=True)),
                ('opcion_img1', models.ImageField(null=True, upload_to='')),
                ('opcion_img2', models.ImageField(null=True, upload_to='')),
                ('opcion_img3', models.ImageField(null=True, upload_to='')),
                ('opcion_img4', models.ImageField(null=True, upload_to='')),
                ('respuesta', models.IntegerField(default=0)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.categoria')),
            ],
        ),
    ]