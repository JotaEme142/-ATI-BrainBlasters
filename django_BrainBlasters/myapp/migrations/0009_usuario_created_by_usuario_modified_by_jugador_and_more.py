# Generated by Django 5.0.7 on 2024-08-02 23:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_remove_usuario_created_by_remove_usuario_modified_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='usuario',
            name='modified_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modified', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('puntaje_acumulado', models.IntegerField(default=0)),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.categoria')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
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
            name='Premio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=150)),
                ('estado', models.CharField(max_length=50)),
                ('ganador', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
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
            name='Sorteo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_sorteo', models.DateField()),
                ('categoria', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.categoria')),
                ('ganador1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sorteos_ganados1', to=settings.AUTH_USER_MODEL)),
                ('ganador2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sorteos_ganados2', to=settings.AUTH_USER_MODEL)),
                ('ganador3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sorteos_ganados3', to=settings.AUTH_USER_MODEL)),
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
    ]