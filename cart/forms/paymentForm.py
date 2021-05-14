from django.forms import ModelForm, widgets
from cart.models import Payment


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = ['cardOwner', 'cardNumber', 'expirationDateMonth', 'expirationDateYear', 'cvc']
        exclude = ['id']
        widgets = {
            'cardOwner': widgets.TextInput(attrs={'class': 'form_control', 'autocomplete': 'off', 'maxlength': 100}),
            'cardNumber': widgets.TextInput(attrs={'class': 'form_control', 'autocomplete': 'off', 'type':"tel", 'inputmode': "numeric", 'pattern':"[0-9\s]{13,19}", 'autocomplete':"cc-number", 'maxlength':"19", 'placeholder':"xxxx xxxx xxxx xxxx"}),
            'expirationDateMonth': widgets.Select(attrs={'class': 'form_control'}),
            'expirationDateYear':widgets.Select(attrs={'class': 'form_control'}),
            'cvc': widgets.TextInput(attrs={'class': 'form_control', 'autocomplete': 'off'}),
        }
