# Generated by Django 5.0.7 on 2024-08-11 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_alter_trivia_opcion_img1_alter_trivia_opcion_img2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trivia',
            name='opcion_img1',
            field=models.ImageField(blank=True, null=True, upload_to='media/img/'),
        ),
        migrations.AlterField(
            model_name='trivia',
            name='opcion_img2',
            field=models.ImageField(blank=True, null=True, upload_to='media/img/'),
        ),
        migrations.AlterField(
            model_name='trivia',
            name='opcion_img3',
            field=models.ImageField(blank=True, null=True, upload_to='media/img/'),
        ),
        migrations.AlterField(
            model_name='trivia',
            name='opcion_img4',
            field=models.ImageField(blank=True, null=True, upload_to='media/img/'),
        ),
    ]