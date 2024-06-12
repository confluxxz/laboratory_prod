from django.db.models import Model, ForeignKey, CharField,FloatField, BooleanField
from django.db.models.deletion import CASCADE
from inventory.models import Equipment


class ExtraFields (Model):
    equipment = ForeignKey(to=Equipment, on_delete=CASCADE, related_name='extra_fields', verbose_name='Оборудование')
    name = CharField(max_length=100, verbose_name='Название дополнительного поля')
    hint = CharField(max_length=300, verbose_name='Подсказка')
    importance = BooleanField(blank=True, default=True, verbose_name='Обязательность')
    value = FloatField(default=0, verbose_name='Значение по умолчанию')
    class Meta:
        verbose_name = 'Дополнительное поле'
        verbose_name_plural = 'Дополнительные поля'

    def __str__(self):
        return f"{self.equipment.name} - {self.name}"
