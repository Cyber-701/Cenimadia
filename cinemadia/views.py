from django.shortcuts import render, get_object_or_404
from .models import Movie
from collections import defaultdict

# Create your views here.
def home(request):
    movies = Movie.objects.all()
    featured_movie = Movie.objects.filter(is_featured=True).first()
    
    # Organize movies by category
    movies_by_category = defaultdict(list)
    for movie in movies:
        movies_by_category[movie.category].append(movie)
    
    context = {
        'movies': movies,
        'featured_movie': featured_movie,
        'movies_by_category': movies_by_category,
    }
    return render(request, 'home.html', context)

def movie_detail(request, slug):
    movie = get_object_or_404(Movie, slug=slug)
    movies = Movie.objects.exclude(id=movie.id)[:6]  # Related movies
    context = {
        'movie': movie,
        'movies': movies,
        'related_movies': movies,
    }
    return render(request, 'movie_detail.html', context)

def profile(request):
    return render(request, 'profile.html')