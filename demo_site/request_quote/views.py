from django.shortcuts import render, redirect, HttpResponse
from .forms import QuoteRequestForm

def main(request):
    form = QuoteRequestForm()
    context = {
        "quoteForm": form
    }
    return render(request, "quote.html", context)

def thankyou(request):
    return HttpResponse("Thank you")