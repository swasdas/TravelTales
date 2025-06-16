from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path("", views.posts_list, name="list"),
    path("new-post/", views.post_new, name="new-post"),
    path("<slug:url_key>", views.post_page, name="page"),
]
