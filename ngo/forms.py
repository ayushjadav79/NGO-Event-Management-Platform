from django import forms
from .models import NGO

class NGORegistrationForm(forms.ModelForm):
    class Meta:
        model = NGO
        fields = '__all__'
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
        }