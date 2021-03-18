from django import forms
from .models import Person, FileUpload
from django.forms import ModelForm

class ProductForm(forms.Form):
    name = forms.CharField(max_length=200)
    price = forms.IntegerField()


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'


class FileForm(ModelForm):
    class Meta:
        model = FileUpload
        fields = '__all__'


