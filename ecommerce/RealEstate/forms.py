from django import forms
from.models import PhotoCard


class PhotoCardForm(forms.ModelForm):
    class Meta:
        model = PhotoCard
        fields = ['photo', 'name', 'type',  'price', 'delivery_time', 'delivery_cost']
