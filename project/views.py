from django.shortcuts import render, redirect, reverse
from django.views.decorators.csrf import csrf_exempt
from .forms import ContactForm
from .models import *
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from marketing.models import Signup

def home(request):
	return render(request, 'blog/launch.html', {})


def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact-us/success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'blog/contact-us.html', context)



def aboutus(request):
    return render(request, 'blog/about-us.html', {})

def soon(request):
    return render(request, 'blog/soon.html', {})