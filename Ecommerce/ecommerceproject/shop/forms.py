from django import forms
from .models import Product,Category
class CategoryForms(forms.ModelForm):
    class Meta:
        model=Category
        fields=['name','slug','description', 'image']