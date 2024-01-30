from django.shortcuts import render
from django.views.generic import ListView
from .models  import Post

# Create your views here.

class HomePageViewPost(ListView):
    model = Post
    template_name = 'home.html'

# class blogDetailView(DetailView):
#     model = Post
#     template_name = 'post_datail.html'