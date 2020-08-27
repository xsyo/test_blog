from django.urls import path

from .views import main, PostCreateView, PostDetailView

app_name = 'blog'

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('', main, name='main'),
]