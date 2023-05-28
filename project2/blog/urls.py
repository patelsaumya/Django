from django.urls import path
from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("posts", views.AllPostsView.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="post-detail-page"),
    # slug - Matches any slug string consisting of ASCII letters or numbers, plus the hyphen and underscore characters.
    # For example, building-your-1st-django-site.
    path("read-later", views.ReadLaterView.as_view(), name="read-later")
]
