from django.db.models import Model, ForeignKey, IntegerField
from django.db.models.deletion import CASCADE
from .works import Work
from dishes.models import Dishes
class WorkDishes(Model):
    work = ForeignKey(to=Work, on_delete=CASCADE, related_name='dishes', verbose_name='Работа')
    dishes = ForeignKey(to=Dishes, on_delete=CASCADE, verbose_name='Посуда')
    quantity = IntegerField(default=0, verbose_name='Количество')
    class Meta:
        verbose_name = 'Посуда эксперимента'
        verbose_name_plural = 'Посуда эксперимента'

    def __str__(self):
        return "{} {}".format(self.work, self.dishes)
