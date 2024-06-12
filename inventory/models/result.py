from django.db.models import Model, ForeignKey, FileField, CharField

class Result (Model):
    name = CharField(max_length=100, verbose_name='Наименование')
    dry_method = CharField(max_length=200, verbose_name='Метод сушки')
    analyse_method = CharField(max_length=100, verbose_name='Метод аналитического исследования, прибор для исследования')
    form = CharField(max_length=100, verbose_name='Форма полученных частиц')
    file = FileField(null=True, blank=True, upload_to=None, max_length=255)
    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'

    def __str__(self):
        return self.name