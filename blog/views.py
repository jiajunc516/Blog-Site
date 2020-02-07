from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Comment
from .forms import CommentForm

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

    # List of active comments for this post
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == "POST":
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object
            new_comment = comment_form.save(commit=False)
            # Assign current post to the comment
            new_comment.post = post
            # Save comment to database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request,
        "blog/post/blog_page.html",
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form
        }
    )