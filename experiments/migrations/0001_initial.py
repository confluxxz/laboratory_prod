# Generated by Django 4.2.11 on 2024-05-26 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Количество')),
                ('created_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('approved', models.BooleanField(default=False, verbose_name='Одобрено')),
                ('session_key', models.CharField(blank=True, max_length=32, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.items', verbose_name='Предмет')),
            ],
            options={
                'verbose_name': 'Эксперимент',
                'verbose_name_plural': 'Эксперименты',
                'db_table': 'experiment',
            },
        ),
    ]
