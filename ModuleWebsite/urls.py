from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about_us"),
    path("location", views.location, name="about_us_locations"),
    path("events", views.index, name="events"),
    path("events_detail", views.index, name="events_detail"),
    path("home", views.index, name="home"),
    path("sermons", views.index, name="sermons"),
    path("gallery", views.index, name="gallery"),
    path("blog", views.index, name="blog"),
    path("blog", views.index, name="blog_detail"),
    path("drilling", views.drilling, name="drilling"),

]