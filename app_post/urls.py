from django.urls import path
from .views import HomePageViewPost

urlpatterns = [
    path('', HomePageViewPost.as_view(), name='home')
]