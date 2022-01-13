from django.urls import path
from . import views

urlpatterns = [
    path('', views.markets, name="index"), 
    path('coin/<str:id>/', views.coin_posts, name='coin_posts'),
]