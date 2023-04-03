from django import forms

from todo.models import Tag, Task


class TaskNameSearchForm(forms.Form):
    content = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={
            "class": "form-list-find",
            "placeholder": "Search by content"
        }),
    )


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Task
        fields = [
            "name",
            "content",
            "deadline",
            "status",
            "tags"]

    deadline = forms.DateTimeField(
        label='What is deadline?',
        widget=forms.SelectDateWidget
    )
