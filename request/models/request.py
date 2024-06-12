from django.db.models import Model, CharField, TextField, DateField, ForeignKey
from django.db.models.deletion import CASCADE
from clients.models import ClientSystem

class Request(Model): #todo создать, удалять, изменение, взятие в работу для проверки и выдача результата
    theme = CharField(max_length=100, verbose_name='Тема')
    description = TextField(verbose_name='Описание')
    date_create = DateField(verbose_name='Дата создания')
    date_processed = DateField(verbose_name='Дата обработки')
    applicant = ForeignKey(to=ClientSystem, on_delete=CASCADE, related_name='client_applicant', verbose_name='Заявитель')
    responsible = ForeignKey(to=ClientSystem, on_delete=CASCADE, related_name='client_responsible', verbose_name='Ответсвенный')
    result = TextField(verbose_name='Результат')

    class Meta:
        verbose_name = 'Обращения'
        verbose_name_plural ='Обращение'

    def __str__(self):
        return "{} ({}) {}".format(self.work.theme, self.applicant, self.responsible, self.date_create.strftime('%d.%m.%y'))
