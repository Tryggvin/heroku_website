from django.forms import ModelForm, widgets
from cart.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'streetName', 'houseNumber', 'city', 'country', 'postalCode']
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form_control', 'autocomplete': 'off', 'maxlength': 100}),
            'streetName': widgets.TextInput(attrs={'class': 'form_control', 'autocomplete': 'off', 'maxlength': 100}),
            'houseNumber': widgets.TextInput(attrs={'class': 'form_control', 'autocomplete': 'off', 'type': 'number'}),
            'city':widgets.TextInput(attrs={'class': 'form_control', 'autocomplete': 'off', 'maxlength': 100}),
            'country': widgets.Select(attrs={'class': 'form_control'}),
            'postalCode': widgets.TextInput(attrs={'class': 'form_control', 'autocomplete': 'off', 'type': 'number'})
        }
