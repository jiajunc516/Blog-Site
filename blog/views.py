from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post

NUMBER_OF_SHOWN_POST = 3
# Create your views here.
def get_post_list(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, NUMBER_OF_SHOWN_POST)
    p = request.GET.get("page")
    
    try:
        posts = paginator.page(p)
    except PageNotAnInteger:
        # If p is not an integer, deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If p is out of range, deliver the last page
        posts = paginator.page(paginator.num_pages)

    return render(
        request,
        "blog/post/list.html",
        {"post_list": posts}
    )

def get_single_post(request, year, month, day, slug):
    post = Post.objects.filter(
        publish__year = year,
        publish__month = month,
        publish__day = day,
        slug = slug
    ).first()
    return render(
        request,
        "blog/post/blog_page.html",
        {"post": post}
    )