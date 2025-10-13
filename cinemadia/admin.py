from django.contrib import admin
from .models import Movie

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

# Admin panel sarlavhasini o'zgartirish
admin.site.site_header = '🎬 CINEMADIA Admin Panel'
admin.site.site_title = 'Cinemadia Admin'
admin.site.index_title = 'Cinemadia Boshqaruv Paneli'