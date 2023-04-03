from django import forms


class TaskNameSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={
            "class": "form-list-find",
            "placeholder": "Search by name"
        }),
    )
