from django.shortcuts import render, redirect, HttpResponse
from .forms import QuoteRequestForm

def main(request):
    if request.method == 'POST':
        form = QuoteRequestForm(request.POST)
        if form.is_valid():
            # add cleaned data 
            # create quote object
            # quote = QuoteRequest()
            # quote.first_name = form.cleaned_data['first_name']
            form.save()
            return redirect(thankyou)
    else: 
        form = QuoteRequestForm()
        context = {
            "quoteForm": form
        }
    return render(request, "quote.html", context)

def thankyou(request):
    return render(request, "thankyou.html")