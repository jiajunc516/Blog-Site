from django.urls import path
from . import views

app_name = "wiki"
urlpatterns = [
    # post views
    path("", views.wiki_home, name = "wiki_host"),
]