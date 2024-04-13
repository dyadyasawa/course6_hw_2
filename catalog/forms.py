
from django import forms

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        #fields = '__all__'
        fields = ('name', 'description', 'image', 'category', 'price',)

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        forbidden_words_list = [
            'казино',
            'криптовалюта',
            'крипта',
            'биржа',
            'дешево',
            'бесплатно',
            'обман',
            'полиция',
            'радар'
        ]
        for word in forbidden_words_list:
            if word in cleaned_data.lower():
                raise forms.ValidationError('В названии присутствуют недопустимые слова.')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        forbidden_words_list = [
            'казино',
            'криптовалюта',
            'крипта',
            'биржа',
            'дешево',
            'бесплатно',
            'обман',
            'полиция',
            'радар'
        ]
        for word in forbidden_words_list:
            if word in cleaned_data.lower():
                raise forms.ValidationError('В описании присутствуют недопустимые слова.')
        return cleaned_data

class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'
