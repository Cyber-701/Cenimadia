from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q, Avg, Count
from django.core.paginator import Paginator
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Movie, Favorite, Watchlist, Review, WatchHistory, UserProfile, MovieVote
from .forms import CustomUserCreationForm, ReviewForm, UserProfileForm
from collections import defaultdict
  
# Create your views here.
def home(request):
    # Search functionality
    query = request.GET.get('q', '')
    if query:
        movies = Movie.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(genre__icontains=query) |
            Q(director__icontains=query) |
            Q(actors__icontains=query)
        ).order_by('-rating', '-year')
    else:
        movies = Movie.objects.all().order_by('-created_at')
    
    # Paginationn
    paginator = Paginator(movies, 12)  # 12 movies per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    featured_movie = Movie.objects.filter(is_featured=True).first()
    
    # Organize movies by category
    movies_by_category = defaultdict(list)
    for movie in Movie.objects.all()[:30]:  # Limit for performance
        movies_by_category[movie.category].append(movie)
    
    # Get popular and random movies
    popular_movies = get_popular_movies()
    random_movies = get_random_movies()
    
    context = {
        'movies': page_obj,
        'featured_movie': featured_movie,
        'movies_by_category': movies_by_category,
        'popular_movies': popular_movies,
        'random_movies': random_movies,
        'query': query,
        'total_count': movies.count() if query else Movie.objects.count(),
    }
    return render(request, 'home.html', context)

def movie_detail(request, slug):
    movie = get_object_or_404(Movie, slug=slug)
    movies = Movie.objects.exclude(id=movie.id)[:6]  # Related movies
    
    # Get user's vote if authenticated
    user_vote = None
    if request.user.is_authenticated:
        try:
            vote = MovieVote.objects.get(user=request.user, movie=movie)
            user_vote = vote.vote_type
        except MovieVote.DoesNotExist:
            user_vote = None
    
    context = {
        'movie': movie,
        'movies': movies,
        'related_movies': movies,
        'user_vote': user_vote,
    }
    return render(request, 'movie_detail.html', context)

def register(request):
    """User registration view"""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Muvaffaqiyatli ro\'yxatdan o\'tdingiz!')
            return redirect('cinemadia:home')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    """User profile view"""
    user = request.user
    favorites = Favorite.objects.filter(user=user).select_related('movie')[:6]
    watchlist = Watchlist.objects.filter(user=user).select_related('movie')[:6]
    watch_history = WatchHistory.objects.filter(user=user).select_related('movie')[:6]
    reviews = Review.objects.filter(user=user).select_related('movie')[:5]
    
    # Get or create user profile
    profile, created = UserProfile.objects.get_or_create(user=user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil muvaffaqiyatli yangilandi!')
            return redirect('cinemadia:profile')
    else:
        form = UserProfileForm(instance=profile)
    
    context = {
        'user': user,
        'profile': profile,
        'form': form,
        'favorites': favorites,
        'watchlist': watchlist,
        'watch_history': watch_history,
        'reviews': reviews,
        'stats': {
            'favorites_count': favorites.count(),
            'watchlist_count': watchlist.count(),
            'reviews_count': reviews.count(),
            'watched_count': watch_history.count(),
        }
    }
    return render(request, 'profile.html', context)

def category_view(request, category):
    """View for displaying movies by category"""
    category_choices = dict(Movie.CATEGORY_CHOICES)
    category_name = category_choices.get(category, '')
    
    movies = Movie.objects.filter(category=category).order_by('-rating', '-year')
    
    # Pagination
    paginator = Paginator(movies, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'movies': page_obj,
        'category': category,
        'category_name': category_name,
        'total_count': movies.count(),
    }
    
    # Use specific template for each category
    template_map = {
        'tarjima_kino': 'tarjima_kino.html',
        'premyera': 'premyera.html',
        'hind': 'hind.html',
        'multfilm': 'multfilm.html',
        'serial': 'serial.html',
    }
    
    template_name = template_map.get(category, 'category.html')
    return render(request, template_name, context)

def genre_view(request, genre):
    """View for displaying movies by genre"""
    movies = Movie.objects.filter(genre__icontains=genre).order_by('-rating', '-year')
    
    # Pagination
    paginator = Paginator(movies, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'movies': page_obj,
        'genre': genre,
        'total_count': movies.count(),
    }
    return render(request, 'genre.html', context)

@login_required
@require_POST
def toggle_favorite(request, movie_id):
    """Toggle movie in favorites"""
    movie = get_object_or_404(Movie, id=movie_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, movie=movie)
    
    if not created:
        favorite.delete()
        is_favorite = False
        message = 'Sevimlilardan o\'chirildi'
    else:
        is_favorite = True
        message = 'Sevimlilarga qo\'shildi'
    
    return JsonResponse({
        'is_favorite': is_favorite,
        'message': message,
        'favorites_count': Favorite.objects.filter(movie=movie).count()
    })

@login_required
@require_POST
def toggle_watchlist(request, movie_id):
    """Toggle movie in watchlist"""
    movie = get_object_or_404(Movie, id=movie_id)
    watchlist, created = Watchlist.objects.get_or_create(user=request.user, movie=movie)
    
    if not created:
        watchlist.delete()
        in_watchlist = False
        message = 'Ko\'rish ro\'yxatidan o\'chirildi'
    else:
        in_watchlist = True
        message = 'Ko\'rish ro\'yxatiga qo\'shildi'
    
    return JsonResponse({
        'in_watchlist': in_watchlist,
        'message': message
    })

@login_required
def add_review(request, movie_id):
    """Add review to movie"""
    movie = get_object_or_404(Movie, id=movie_id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.movie = movie
            review.save()
            
            # Update movie rating
            avg_rating = Review.objects.filter(movie=movie).aggregate(Avg('rating'))['rating__avg']
            if avg_rating:
                movie.rating = round(avg_rating, 1)
                movie.save()
            
            messages.success(request, 'Fikringiz qo\'shildi!')
            return redirect('cinemadia:movie_detail', slug=movie.slug)
    else:
        form = ReviewForm()
    
    return render(request, 'add_review.html', {
        'form': form,
        'movie': movie
    })

@login_required
def favorites_list(request):
    """List all user's favorite movies"""
    favorites = Favorite.objects.filter(user=request.user).select_related('movie')
    
    paginator = Paginator(favorites, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'favorites.html', {
        'favorites': page_obj,
        'total_count': favorites.count()
    })

@login_required
def watchlist_view(request):
    """List all user's watchlist movies"""
    watchlist = Watchlist.objects.filter(user=request.user).select_related('movie')
    
    paginator = Paginator(watchlist, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'watchlist.html', {
        'watchlist': page_obj,
        'total_count': watchlist.count()
    })


@login_required
@require_POST
def vote_movie(request, movie_id):
    """Handle movie like/dislike votes"""
    movie = get_object_or_404(Movie, id=movie_id)
    vote_type = request.POST.get('vote_type')
    
    if vote_type not in ['like', 'dislike']:
        return JsonResponse({'error': 'Invalid vote type'}, status=400)
    
    # Get or create vote
    vote, created = MovieVote.objects.get_or_create(
        user=request.user,
        movie=movie,
        defaults={'vote_type': vote_type}
    )
    
    # If vote exists and is different, update it
    if not created and vote.vote_type != vote_type:
        # Remove old vote count
        if vote.vote_type == 'like':
            movie.likes_count = max(0, movie.likes_count - 1)
        else:
            movie.dislikes_count = max(0, movie.dislikes_count - 1)
        
        # Update vote type
        vote.vote_type = vote_type
        vote.save()
    elif not created and vote.vote_type == vote_type:
        # User clicked same vote - remove it
        vote.delete()
        if vote_type == 'like':
            movie.likes_count = max(0, movie.likes_count - 1)
        else:
            movie.dislikes_count = max(0, movie.dislikes_count - 1)
        movie.save()
        
        return JsonResponse({
            'success': True,
            'likes_count': movie.likes_count,
            'dislikes_count': movie.dislikes_count,
            'user_vote': None
        })
    
    # Add new vote count
    if vote_type == 'like':
        movie.likes_count += 1
    else:
        movie.dislikes_count += 1
    
    movie.save()
    
    return JsonResponse({
        'success': True,
        'likes_count': movie.likes_count,
        'dislikes_count': movie.dislikes_count,
        'user_vote': vote_type
    })


def get_popular_movies():
    """Get popular movies based on votes and engagement"""
    from django.db.models import F, Case, When, IntegerField
    
    movies = Movie.objects.annotate(
        total_votes=F('likes_count') + F('dislikes_count'),
        popularity_score=Case(
            When(total_votes=0, then=0),
            default=(F('likes_count') * 100 / F('total_votes')) + (F('total_votes') / 10),
            output_field=IntegerField()
        )
    ).filter(total_votes__gt=0).order_by('-popularity_score')[:10]
    
    return movies


def get_random_movies():
    """Get random movies for carousel"""
    return Movie.objects.order_by('?')[:15]
