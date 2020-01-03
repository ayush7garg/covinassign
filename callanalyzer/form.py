from django import forms
from .models import call

class callForm(forms.ModelForm):
    class Meta:
        model = call
        fields = "__all__"
