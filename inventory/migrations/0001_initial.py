# Generated by Django 4.0.4 on 2023-11-16 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0003_clientsystem_is_assistant'),
        ('dishes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DryMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dry_method', models.CharField(max_length=100, verbose_name='Способ Сушки')),
            ],
            options={
                'verbose_name': 'Способ работы оборудования',
                'verbose_name_plural': 'Способы работы оборудования',
            },
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название оборудования')),
                ('is_avaliabe', models.BooleanField(default=True, verbose_name='Готов к работе')),
                ('place', models.CharField(default='', max_length=500, verbose_name='Место хранения')),
            ],
            options={
                'verbose_name': 'Оборудование эксперимента',
                'verbose_name_plural': 'Оборудование эксперимента',
            },
        ),
        migrations.CreateModel(
            name='ExtraFields',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название дополнительного поля')),
                ('hint', models.CharField(max_length=300, verbose_name='Подсказка')),
                ('importance', models.BooleanField(blank=True, default=True, verbose_name='Обязательность')),
                ('value', models.FloatField(default=0, verbose_name='Значение по умолчанию')),
            ],
            options={
                'verbose_name': 'Дополнительное поле',
                'verbose_name_plural': 'Дополнительные поля',
            },
        ),
        migrations.CreateModel(
            name='Reagents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('quantity', models.FloatField(default=0, verbose_name='Количество')),
                ('units', models.IntegerField(choices=[(1, 'mg'), (2, 'g'), (3, 'kg'), (4, 'ml'), (5, 'l')], verbose_name='Единицы измерения')),
                ('place', models.CharField(default='', max_length=500, verbose_name='Место хранения')),
                ('last_update_date', models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')),
            ],
            options={
                'verbose_name': 'Реагенты',
                'verbose_name_plural': 'Реагенты',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('dry_method', models.CharField(max_length=200, verbose_name='Метод сушки')),
                ('analyse_method', models.CharField(max_length=100, verbose_name='Метод аналитического исследования, прибор для исследования')),
                ('form', models.CharField(max_length=100, verbose_name='Форма полученных частиц')),
                ('file', models.FileField(blank=True, max_length=255, null=True, upload_to=None)),
            ],
            options={
                'verbose_name': 'Результат',
                'verbose_name_plural': 'Результаты',
            },
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(default=0, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Значение дополнительного поля',
                'verbose_name_plural': 'Значения дополнительных полей',
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, null=True)),
                ('is_approved', models.BooleanField(blank=True, default=None, null=True)),
                ('accept_person', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accept_persons', to='clients.clientsystem', verbose_name='Согласующий')),
            ],
            options={
                'verbose_name': 'Лабораторная работа',
                'verbose_name_plural': 'Лабораторные работы',
            },
        ),
        migrations.CreateModel(
            name='WorkReagents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(default=0, verbose_name='Количество')),
                ('units', models.IntegerField(choices=[(1, 'mg'), (2, 'g'), (3, 'kg'), (4, 'ml'), (5, 'l')], verbose_name='Единицы измерения')),
                ('reagent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_reagents', to='inventory.reagents')),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reagents', to='inventory.work')),
            ],
            options={
                'verbose_name': 'Реагенты для лабораторной работы',
                'verbose_name_plural': 'Реагенты для лабораторной работы',
            },
        ),
        migrations.CreateModel(
            name='WorkDishes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0, verbose_name='Количество')),
                ('dishes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dishes.dishes', verbose_name='Посуда')),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='inventory.work', verbose_name='Работа')),
            ],
            options={
                'verbose_name': 'Посуда эксперимента',
                'verbose_name_plural': 'Посуда эксперимента',
            },
        ),
    ]
