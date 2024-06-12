from django.db.models import Model, ForeignKey, CharField
from django.db.models.deletion import CASCADE
from inventory.models import Equipment


class DryMethod (Model):
    equipment = ForeignKey(to=Equipment, on_delete=CASCADE, related_name='dry_methods', verbose_name='Оборудование')
    dry_method = CharField(max_length=100, verbose_name='Способ Сушки')

    class Meta:
        verbose_name = 'Способ работы оборудования'
        verbose_name_plural = 'Способы работы оборудования'

    def __str__(self):
        return self.equipment

