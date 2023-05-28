from django.urls import path

from . import views

# URL Config
urlpatterns = [
    # path("january", views.january),
    path("", views.index, name="index"),
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge") # Dynamic Path Segment
]