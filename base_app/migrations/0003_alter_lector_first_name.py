# Generated by Django 4.0.5 on 2022-06-13 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0002_remove_lector_fullname_remove_student_fullname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lector',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='Имя'),
        ),
    ]
