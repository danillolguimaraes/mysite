from django.urls import path
from .views import post_view

urlpatterns = [
    path('', post_view.home, name='home'),
    path('post/<slug:slug>/', post_view.PostDetailView.as_view(), name='post_detail'),
]
