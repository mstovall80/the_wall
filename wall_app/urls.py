from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path('register', views.register),
    path("login", views.login),
    path("user_post_page", views.user_post_page),
    path("posted_message", views.posted_message),
    path("the_wall", views.the_wall)

]
