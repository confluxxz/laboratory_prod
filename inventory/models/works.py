from django.db.models import Model, ForeignKey, TextField, CharField, BooleanField
from django.db.models.deletion import CASCADE
from clients.models.client import ClientSystem
from research.models import Research


class Work(Model):
    name = CharField(max_length=100, verbose_name='Наименование')
    description = TextField(null=True, blank=True, verbose_name='Описание')
    student = ForeignKey(to=ClientSystem, on_delete=CASCADE, related_name='student', verbose_name='Студент')
    accept_person = ForeignKey(to=ClientSystem, on_delete=CASCADE, default=None, blank=True, null=True, related_name='accept_persons', verbose_name='Согласующий')
    research = ForeignKey(to=Research, on_delete=CASCADE, related_name='works', verbose_name='Исследование', default=None)
    is_approved = BooleanField(default=None, null=True, blank=True, verbose_name='Одобрено')

    class Meta:
        verbose_name = 'Лабораторная работа'
        verbose_name_plural = 'Лабораторные работы'

    def __str__(self):
        return (f"{self.name}. "
                f"Студент: {self.student}. "
                f"Одобрено: {self.is_approved}")