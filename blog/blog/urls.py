from django.urls import path
from .views import BlogListView
from .views import BlogDetailView


urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name="post_detail"),
    path('', BlogListView.as_view(), name='home'),
]
