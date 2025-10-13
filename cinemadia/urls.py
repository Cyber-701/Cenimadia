from django.urls import path
from . import views

app_name = 'cinemadia'

urlpatterns = [
    path('', views.home, name='home'),
    path('movie/<slug:slug>/', views.movie_detail, name='movie_detail'),
    path('category/<str:category>/', views.category_view, name='category'),
    path('genre/<str:genre>/', views.genre_view, name='genre'),
    
    # User authentication
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    
    # User interactions
    path('movie/<int:movie_id>/favorite/', views.toggle_favorite, name='toggle_favorite'),
    path('movie/<int:movie_id>/watchlist/', views.toggle_watchlist, name='toggle_watchlist'),
    path('movie/<int:movie_id>/review/', views.add_review, name='add_review'),
    
    # User lists
    path('favorites/', views.favorites_list, name='favorites'),
    path('watchlist/', views.watchlist_view, name='watchlist'),
]
