from django.db import models
from users.models import User
from goods.models import Items
from experiments.models import UnitsType

class WorkItemQueryset(models.QuerySet):

    def total_quantity(self):
        if self:
            return sum(experiment.quantity for experiment in self)
        return 0


class Work(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь',
                             default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания эксперимента')
    name = models.TextField(max_length=150, blank=True, null=True, verbose_name='Название работы')
    description = models.CharField(max_length=350, blank=True, null=True,verbose_name='Описание работы')
    requires_files = models.BooleanField(default=False, verbose_name="Необходимость прикреплять дополнительные файлы")
    additional_files = models.FileField(upload_to='works_files' ,blank=True, null=True, verbose_name='Дополнительные файлы')
    is_done = models.BooleanField(default=False, verbose_name='Выполнено')
    status_experiment = models.BooleanField(default=None,  blank=True, null=True, verbose_name='Статус эксперимента')
    results = models.FileField(upload_to='works_results', blank=True, null=True, verbose_name='Результаты эксперимента')

    class Meta:
        db_table = "work"
        verbose_name = "Работа"
        verbose_name_plural = "Работы"

    def __str__(self):
        return f" Работа № {self.pk} {self.name}| Выполняет {self.user.first_name} {self.user.last_name}"


class WorkItem(models.Model):
    work = models.ForeignKey(to=Work, on_delete=models.CASCADE, verbose_name="Работа")
    item = models.ForeignKey(to=Items, on_delete=models.SET_DEFAULT, null=True, verbose_name="Предмет", default=None)
    name = models.CharField(max_length=150, verbose_name="Название")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    created_timestamp = models.DateTimeField(auto_now_add=True,
                                             verbose_name='Дата выполнения эксперимента эксперимента')
    date = models.DateTimeField(verbose_name='Дата бронирования', blank=True, null=True)
    units = models.IntegerField(verbose_name='Единицы измерения', choices=UnitsType.choices, blank=True, null=True, )

    class Meta:
        db_table = "work_item"
        verbose_name = "Задействованный предмет эксперимента"
        verbose_name_plural = "Задействованные предметы"



    def __str__(self):
        return f" Работа № {self.work.pk} | {self.work.name}"
