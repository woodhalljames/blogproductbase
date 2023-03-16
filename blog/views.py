from django.shortcuts import render

# Create your views here.
def blog(request):
	return render(request, 'blog/blogindex.html', {})

def blogpost(request):
	return render(request, 'blog/blogpost.html', {})

	
	