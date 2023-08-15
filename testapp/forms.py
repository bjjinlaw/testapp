from django import forms
from testapp.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("title", "description", "category", "status", )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"