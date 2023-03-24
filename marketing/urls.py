from django.contrib import admin
from django.urls import path

from .views import contactView, successView

urlpatterns = [
    path("contact-us/", contactView, name="contact"),
    path("contact-us/success", successView, name="success"),
]