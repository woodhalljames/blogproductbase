from django.shortcuts import render 
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

def subscribe(request): 
    post_data = request.POST.copy()
    email = post_data.get("email", None)

    error_msg = validation_utility.validate_email(email)
    if error_msg:
        messages.error(request, error_msg)
        return HttpResponseRedirect(reverse('appname:subscribe'))

def save_email(email):
    try:
        subscribe_model_instance = SubscribeModel.objects.get(email=email)
    except ObjectDoesNotExist as e:
        subscribe_model_instance = SubscribeModel()
        subscribe_model_instance.email = email
    except Exception as e:
        logging.getLogger("error").error(traceback.format_exc())
        return False

    # does not matter if already subscribed or not...resend the email
    subscribe_model_instance.status = constants.SUBSCRIBE_STATUS_SUBSCRIBED
    subscribe_model_instance.created_date = utility.now()
    subscribe_model_instance.updated_date = utility.now()
    subscribe_model_instance.save()
    return True

def aboutus(request):
    return render(request, 'blog/about-us.html', {})

def soon(request):
    return render(request, 'blog/soon.html', {})