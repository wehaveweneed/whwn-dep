from django.forms.widgets import TextInput, Textarea, HiddenInput
from django.forms.extras.widgets import SelectDateWidget
from django import forms

from whwn.models.item import Item
from whwn.models.itemcategory import ItemCategory
from whwn.models.itemsku import ItemSKU

class PublicItemForm(forms.Form):
    form_attrs = {
        'item': {
            "placeholder": "e.g., AAA Batteries or Volunteer",
            "style": "width: 100%",
        },
        "description": {
            "placeholder": "Bulk pack of batteries  -OR-  I have [medical/legal/clerical/construction/etc.] experience",
            "style": "width: 100%",
            "rows": 5,
        },
        "first_name": {"placeholder": "John", "size": 30, 
                       "class": "contact-input"},
        "last_name": {"placeholder": "Smith", "size": 30,
                      "class": "contact-input"},
        "phone": {"placeholder": "(123) 456-7890", "type": "tel", 
                  "size": 15, "class": "contact-input"},
        "email": {"placeholder": "jsmith@example.com", "type": "email", 
                  "size": 30, "class": "contact-input"},
    }

    name = forms.CharField(widget=TextInput(attrs=form_attrs['item']))
    first_name = forms.CharField(widget=TextInput(attrs=form_attrs['first_name']))
    last_name = forms.CharField(widget=TextInput(attrs=form_attrs['last_name']))
    phone = forms.CharField(widget=TextInput(attrs=form_attrs['phone']))
    email = forms.CharField(widget=TextInput(attrs=form_attrs['email']))
    sku = forms.ModelChoiceField(
        queryset=ItemSKU.objects.all(),
        empty_label=None
    )

class CreateItemForm(forms.ModelForm):

    sku = forms.ModelChoiceField(
        queryset=ItemSKU.objects.all(),
        empty_label=None
    )

    categories = forms.ModelChoiceField(
        queryset=ItemCategory.objects.all(),
        empty_label=None
    )

    class Meta:
        model = Item
        exclude = ["status", "updated_date", "posted_date", "attributes",
                   "unique_id", "user_id", "date", "owner",
                   "post_id", "expiration_date"]
        widgets = {
            'name': TextInput(attrs={"class": "post-form-name", 
                                     "placeholder": "eg: blanket"}),
            'description': Textarea(
                attrs={'class': 'post-form-description'}
            ),
            'amount': TextInput(attrs={'class': 'post-form-quantity'}),
        }

    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user_id', None)
        super(CreateItemForm, self).__init__(*args, **kwargs)

class EditItemForm(forms.ModelForm):

    class Meta:
        model = Item

    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user_id', None)
        super(EditItemForm, self).__init__(*args, **kwargs)

class DeleteForm(forms.Form):
    pass

class UploadFileForm(forms.Form):
    file = forms.FileField(required=False)
    #consider adding a date time uploaded field
