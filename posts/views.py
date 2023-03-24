from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from marketing.models import Signup
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import views
from django.db.models import Count, Q
from .forms import CommentForm



def search(request): 
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
    	queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(meta__icontains=query)
    	).distinct()

    context = {
        'queryset': queryset
    }
    return render(request, 'blog/search_results.html', context)



def get_category_count():
    queryset = Post.objects.values('categories__title').annotate(Count('categories__title')) #.annotate is a dictionry parameter
    
    return queryset


def blog(request):
    category_count = get_category_count()
    featuredposts = Post.objects.filter(featured=True)[0:1]
    latest = Post.objects.order_by('-timestamp')[0:4]
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    most_recent = Post.objects.order_by('-timestamp')[0:3]

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
            paginated_queryset = paginator.page(1)
    except EmptyPage:
            paginated_queryset = paginator.page(paginator.num_pages)

    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email 
        new_signup.save()

    context = {
        'object_list': featuredposts,
        'latest': latest,
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
        'most_recent': most_recent,
        'category_count': category_count,
    }

    return render(request,'blog/blogindex.html',context)


def blogpost(request, slug):
    most_recent = Post.objects.order_by('-timestamp')[0:3]
    category_count = get_category_count()
    post = get_object_or_404(Post, slug=slug)
    
    if post:
           post.view_count = post.view_count + 1
           post.save()

           # Or
          

    context = {
        'post': post,
        'most_recent': most_recent,
        'category_count': category_count,
        }
    return render(request, 'blog/blogpost.html', context)


	