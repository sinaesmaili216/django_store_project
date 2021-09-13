

from django import forms

from customer.models import Address, Customer


class OrderAddress(forms.Form):
    address = forms.ModelChoiceField(queryset=Address.objects.all())

    def __init__(self, user, *args, **kwargs):
        super(OrderAddress, self).__init__(*args, **kwargs)

        self.fields['address'].queryset = Address.objects.filter(customer__user=user)
