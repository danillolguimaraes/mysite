from django.shortcuts import render
from django.views.generic import DetailView
from ..models.post import Post

def home(request):
    posts = Post.objects.filter(status=1).order_by('-created_on')
    return render(request, 'post.html', {'posts': posts})

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
