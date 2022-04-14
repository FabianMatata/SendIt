from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from crispy_forms.layout import Submit
from django.forms import ModelForm, forms
from .models import Place_Order

from django.forms import ModelForm
from django import forms


class Place_OrderForm(ModelForm):
    class Meta:
        model = Place_Order
        fields = ['item_name','from_location','to_location','collect_by_user']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.helper - FormHelper
            self.helper.form_method = 'post'

