# Generated by Django 5.0.7 on 2024-07-26 00:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_usuario_apellido'),
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
        migrations.AddField(
            model_name='usuario',
            name='role',
            field=models.CharField(choices=[('admin', 'Administrador'), ('user', 'Usuario')], default='user', max_length=10),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]