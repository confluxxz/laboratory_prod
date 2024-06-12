from django import forms
from experiments.models import UnitsType,UnitsEquipmentType

class CreateExperimentForm(forms.Form):
    quantity = forms.IntegerField(label='Количество')
    units = forms.ChoiceField(
        choices=UnitsType.choices,
        label='Единицы измерения'
    )
    date = forms.DateTimeField(label='Дата проведения эксперимента', help_text="В формате: дд.мм.гг час:00",
                               )

class CreateExperimentFormEquipment(forms.Form):
    working_type = forms.ChoiceField(
        choices=UnitsEquipmentType,
        label='Способ работы'
    )
    date = forms.DateTimeField(label='Дата проведения эксперимента', help_text="В формате: дд.мм.гг час:00",
                               )