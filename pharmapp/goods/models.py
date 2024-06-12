from django.db import models
from django.urls import reverse
from django.db.models import IntegerChoices
from django.utils.translation import gettext_lazy as _


class UnitsType(IntegerChoices):
    MG = 1, _("mg")
    G = 2, _("g")
    KG = 3, _("kg")
    ML = 4, _("ml")
    L = 5, _("l")


class UnitsEquipmentType(IntegerChoices):
    SKS = 1, _("sks")
    exp = 2, _("example")


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории предметов лаборатории'

    def __str__(self):
        return self.name


class Items(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='store_images', blank=True, null=True, verbose_name='Изображение')
    additional_image = models.ImageField(upload_to='store_additional_images', blank=True, null=True, verbose_name='Дополнительное изображение')
    existence = models.BooleanField(default=False, verbose_name='Наличие')
    quantity = models.IntegerField(default=0, verbose_name='Количество')
    # warehouse_quantity = models.IntegerField(default=0, verbose_name="Количество на складе")
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория предмета')
    units = models.IntegerField(verbose_name='Единицы измерения', choices=UnitsType.choices, blank=True, null=True,)
    working_type = models.IntegerField(verbose_name='Тип работы', choices=UnitsEquipmentType.choices, blank=True, null=True,)

    class Meta:
        db_table = 'item'
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
        ordering = ("id",)

    def __str__(self):
        return f'{self.name} Количество - {self.quantity}'

    def display_id(self):
        return f"{self.id:04}"

    def get_absolute_url(self):
        return reverse("store:item", kwargs={"item_slug":self.slug})



    # class UnitsTypeView(APIView):
    #     choices = UnitsType.choices
    #     permission_classes = [AllowAny, ]
    #
    #
    #     def get_choices_data(self):
    #         result = []
    #         for choice in self.choices:
    #             result.append({'value': choice[0], 'text': choice[1]})
    #         return result