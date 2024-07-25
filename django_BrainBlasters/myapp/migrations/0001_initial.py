# Generated by Django 5.0.7 on 2024-07-24 11:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('is_staff', models.BooleanField()),
                ('password', models.CharField(max_length=128, unique=True)),
                ('alias', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.BooleanField(default=False)),
                ('pregunta_txt1', models.CharField(max_length=100, null=True)),
                ('pregunta_txt2', models.CharField(max_length=100, null=True)),
                ('pregunta_txt3', models.CharField(max_length=100, null=True)),
                ('pregunta_txt4', models.CharField(max_length=100, null=True)),
                ('pregunta_img1', models.ImageField(null=True, upload_to='')),
                ('pregunta_img2', models.ImageField(null=True, upload_to='')),
                ('pregunta_img3', models.ImageField(null=True, upload_to='')),
                ('pregunta_img4', models.ImageField(null=True, upload_to='')),
                ('respuesta', models.IntegerField(default=0)),
                ('categoria', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_jugadores', models.IntegerField(default=0)),
                ('categoria', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Trivia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.categoria')),
                ('pregunta', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.pregunta')),
            ],
        ),
        migrations.CreateModel(
            name='Sorteo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_sorteo', models.DateField()),
                ('categoria', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.categoria')),
                ('ganador1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sorteos_ganados1', to='myapp.usuario')),
                ('ganador2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sorteos_ganados2', to='myapp.usuario')),
                ('ganador3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sorteos_ganados3', to='myapp.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Premio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=150)),
                ('estado', models.CharField(max_length=50)),
                ('ganador', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('puntaje_acumulado', models.IntegerField(default=0)),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.categoria')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.usuario')),
            ],
        ),
    ]