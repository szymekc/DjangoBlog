from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('add_post', views.add_post, name='add_post'),
    path('add_comment', views.add_comment, name='add_comment'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
