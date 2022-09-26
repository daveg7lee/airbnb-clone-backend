from django.urls import path
from . import views

urlpatterns = [path("", views.Withlists.as_view())]
