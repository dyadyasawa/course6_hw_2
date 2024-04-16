
from django import forms

from catalog.models import Product, Version


class StyleMixin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():

            # if field_name == 'current_version_indicator':
            #     field.widget.attrs["class"] = "form-check-input"

            field.widget.attrs["class"] = "form-control"



class ProductForm(StyleMixin):

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

    class Meta:
        model = Product
        # fields = '__all__'
        fields = ('name', 'description', 'image', 'category', 'price',)

    widgets = {
        'current_version_indicator': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    }

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        for word in ProductForm.forbidden_words_list:
            if word in cleaned_data.lower():
                raise forms.ValidationError('В названии присутствуют недопустимые слова.')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']


        for word in ProductForm.forbidden_words_list:
            if word in cleaned_data.lower():
                raise forms.ValidationError('В описании присутствуют недопустимые слова.')
        return cleaned_data


class VersionForm(StyleMixin):

    class Meta:
        model = Version
        fields = '__all__'
        widgets = {
            'current_version_indicator': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

