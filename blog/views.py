from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggit.models import Tag
from .models import Post, Comment
from .forms import CommentForm

NUMBER_OF_SHOWN_POST = 3
# Create your views here.
def get_post_list(request, tag_slug=None):
    if tag_slug:
        tag = Tag.objects.filter(slug=tag_slug).first()
        post_list = Post.objects.filter(tags__in=[tag])
    else:
        post_list = Post.objects.all()
        
    tag_list = Tag.objects.all()
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
        {"post_list": posts, "tag_list": tag_list}
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
    tag_list = Tag.objects.all()
    return render(
        request,
        "blog/post/blog_page.html",
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
            "tag_list": tag_list
        }
    )