from django.shortcuts import render
from .models import Post

# Create your views here.
def get_post_list(request):
    posts = Post.objects.all()
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