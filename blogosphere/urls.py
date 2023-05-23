from django.urls import path
from blogosphere.views import BlogView,AllBlogsView,ProfileView, BlogDetailView


urlpatterns = [
    path('blogs/', BlogView.as_view()),
    path('all_blogs/', AllBlogsView.as_view()),
    path('blog_detail/<str:pk>/', BlogDetailView.as_view()),
    path('profile/', ProfileView.as_view()),
 
]