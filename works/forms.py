from django import forms


class CreateWorkForm(forms.Form):

    first_name = forms.CharField()
    last_name = forms.CharField()
    name = forms.CharField()
    description = forms.CharField()
    requires_files = forms.ChoiceField(
        choices=[
            ("0", False),
            ("1", True),
        ],
    )
    additional_files = forms.FileField(required=False)


class UpdateWorkForm(forms.Form):
    work = forms.IntegerField()
    results = forms.FileField()

