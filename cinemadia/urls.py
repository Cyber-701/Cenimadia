from django.urls import path
from . import views

app_name = 'cinemadia'

urlpatterns = [
    path('', views.home, name='home'),
    path('movie/<slug:slug>/', views.movie_detail, name='movie_detail'),
    path('profile/', views.profile, name='profile'),
]