from django.shortcuts import render 
from django.views.decorators.csrf import csrf_exempt

def home(request):
	return render(request, 'blog/launch.html', {})