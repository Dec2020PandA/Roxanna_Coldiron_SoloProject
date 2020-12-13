from django import forms
from .models import Item

# switch to model form that is connected to QuoteRequest model
class QuoteRequestForm(forms.Form):
    first_name = forms.CharField(max_length=45)
    last_name = forms.CharField(max_length=45)
    email = forms.EmailField()
    items = forms.ModelMultipleChoiceField(
                widget = forms.SelectMultiple,
                queryset = Item.objects.all()
            )
    description = forms.CharField(widget=forms.Textarea)

# rendering fields manually https://docs.djangoproject.com/en/3.1/topics/forms/#rendering-fields-manually 

# future update: https://docs.djangoproject.com/en/3.1/ref/forms/widgets/#customizing-widget-instances