from django.contrib import admin
from .models import Movie, UserProfile, Favorite, Watchlist, Review, WatchHistory

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'genre', 'category', 'rating', 'is_featured')
    list_filter = ('year', 'genre', 'category', 'is_featured')
    search_fields = ('title', 'director', 'actors', 'description')
    readonly_fields = ('slug', 'created_at', 'updated_at')
    list_per_page = 20
    list_editable = ('is_featured', 'rating')
    
    fieldsets = (
        ('🎬 Asosiy ma\'lumotlar', {
            'fields': ('title', 'slug', 'description', 'year', 'genre', 'category', 'director', 'actors', 'duration', 'rating')
        }),
        ('📁 Media fayllar', {
            'fields': ('poster_file', 'poster_url', 'video_file', 'video_url', 'trailer_url'),
            'description': 'Fayllarni yuklash yoki URL manzilini kiriting'
        }),
        ('⚙️ Sozlamalar', {
            'fields': ('is_featured',),
            'classes': ('collapse',),
        }),
        ('📅 Sana ma\'lumotlari', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    
    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)
        }

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth_date', 'created_at')
    search_fields = ('user__username', 'user__email')
    list_filter = ('created_at',)

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'created_at')
    search_fields = ('user__username', 'movie__title')
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'

@admin.register(Watchlist)
class WatchlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'created_at')
    search_fields = ('user__username', 'movie__title')
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'rating', 'created_at')
    search_fields = ('user__username', 'movie__title', 'comment')
    list_filter = ('rating', 'created_at')
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'

@admin.register(WatchHistory)
class WatchHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'progress', 'watched_at')
    search_fields = ('user__username', 'movie__title')
    list_filter = ('watched_at', 'progress')
    date_hierarchy = 'watched_at'

# Admin panel sarlavhasini o'zgartirish
admin.site.site_header = '🎬 CINEMADIA Admin Panel'
admin.site.site_title = 'Cinemadia Admin'
admin.site.index_title = 'Cinemadia Boshqaruv Paneli'
