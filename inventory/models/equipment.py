from django.db.models import Model, ForeignKey, BooleanField, CharField, FileField
from django.db.models.deletion import CASCADE
from .works import Work
from clients.models import ClientSystem
class Equipment(Model):
    name = CharField(max_length=100, verbose_name='Название оборудования')
    is_avaliable = BooleanField(default=True,verbose_name='Готов к работе')
    place = CharField(max_length=500, default="", verbose_name="Место хранения")
    file_instruction = FileField(null=True, blank=True, upload_to=None, max_length=255)
    laboratory_assistant = ForeignKey(to=ClientSystem, on_delete=CASCADE, related_name='laboratory_assistant', verbose_name='Ответственный за оборудование')
    class Meta:
        verbose_name = 'Оборудование эксперимента'
        verbose_name_plural = 'Оборудование эксперимента'

    def __str__(self, *args, **kwargs):
        return (f"{self.name}. "
                f"Ответственный: {self.laboratory_assistant}. "
                f"Место: {self.place}")
