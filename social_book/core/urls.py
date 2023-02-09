from django.urls import path
from . import views

# Add Path to direct to views
urlpatterns = [
    path('', view=views.index, name="index"),
    path('signup', view=views.signup, name="signup")
]