from django.urls import path
from . import views

urlpatterns = [
    path("user/", views.user_dashboard, name="user_dashboard"),
    path("user/careers/", views.user_career_list, name="user_career_list"),
]
