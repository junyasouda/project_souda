# Generated by Django 3.2.3 on 2021-07-25 07:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('remind', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='contents',
            field=models.TextField(max_length=255, verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='日付'),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=30, verbose_name='担当者'),
        ),
        migrations.AlterField(
            model_name='task',
            name='subject',
            field=models.CharField(max_length=255, verbose_name='項目'),
        ),
    ]
