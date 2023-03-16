from django.shortcuts import render
from .models import Post

# Create your views here.
def blog(request):
		featuredposts = Post.objects.filter(featured=True)[0:3]
		latest = Post.objects.order_by('-timestamp')[0:4]
		context = {
			'object_list': featuredposts,
			'latest': latest
		}
		return render(request,'blog/blogindex.html',context)

def blogpost(request):
	return render(request, 'blog/blogpost.html', {})

	
	