from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage, name="homepage"), #homepage view is added as url
    path('post/new/', views.post_new, name="post_new"),
    path('post/<int:pk>/', views.post_detail, name="post_detail"),
    path('post/<int:pk>/edit/', views.post_edit, name="post_edit"),
    path('post/<int:pk>/delete/', views.post_delete, name="post_delete"),
    path('post/search/', views.post_search, name="post_search")
]