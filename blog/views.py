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