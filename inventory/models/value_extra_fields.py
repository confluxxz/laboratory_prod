from django.db.models import Model, ForeignKey, FloatField
from django.db.models.deletion import CASCADE
from inventory.models import ExtraFields, Result

class Value(Model):
    field = ForeignKey(to=ExtraFields, on_delete=CASCADE, related_name='extra_fields', verbose_name='Значение')
    result = ForeignKey(to=Result, on_delete=CASCADE, verbose_name='Результат')
    value = FloatField(default=0, verbose_name='Значение')

    class Meta:
        verbose_name = 'Значение дополнительного поля'
        verbose_name_plural = 'Значения дополнительных полей'
