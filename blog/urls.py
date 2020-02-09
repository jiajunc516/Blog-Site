from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    # post views
    path("", views.get_post_list, name = "post_list"),
    path("<int:year>/<int:month>/<int:day>/<str:slug>/",
        views.get_single_post,
        name = "single_post"),
    path("tag/<str:tag_slug>/",
        views.get_post_list,
        name = "post_list_by_tag"),
]