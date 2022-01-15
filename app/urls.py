from django.urls import path
from . import views

urlpatterns = [
    path('', views.markets, name="index"), 
    path('coin/<str:id>/', views.coin_posts, name='coin_posts'),
    path('coin/delete/<slug:slug>/<str:id>', views.post_delete, name='post_delete'),
    path('coin/edit/<slug:slug>/<str:id>', views.post_edit, name='post_edit'),
    path('post/<slug:slug>/', views.post_detail, name='coin_detail'),
    path('coin/<str:id>/upvote/', views.post_upvote, name='upvote'),
    path('coin/<str:id>/downvote/', views.post_downvote, name='downvote'),
]