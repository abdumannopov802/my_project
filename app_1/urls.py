from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', secondHomePageView.as_view(), name='about'),
    path('news/', newsPageView.as_view(), name='news'),
    path('images/', imagesPageView.as_view(), name='images'),
    path('admin/', Admin.as_view(), name='admin'),
    path('table/', HomeworkTable, name='table'),
    path('post/', PostDetaliView.as_view(), name='postdetail'),
]