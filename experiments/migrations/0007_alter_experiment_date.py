# Generated by Django 4.2.11 on 2024-06-11 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0006_alter_experiment_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата бронирования'),
        ),
    ]