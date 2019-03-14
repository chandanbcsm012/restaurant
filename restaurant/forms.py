from django import forms
from .models import Restaurant

class RestaurantForm(forms.ModelForm):
    pass
    class Meta:
        model = Restaurant
        fields = '__all__'
