from django import forms

# may need this https://docs.djangoproject.com/en/2.2/topics/forms/modelforms/

class QuoteRequestForm(forms.Form):
    first_name = forms.CharField(max_length=45)
    last_name = forms.CharField(max_length=45)
    email = forms.EmailField()
    # generate choices from the product model?
    # https://stackoverflow.com/questions/749000/django-how-to-use-stored-model-instances-as-form-choices/749019