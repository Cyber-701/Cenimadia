from django.db import models
from django.utils import timezone

class Movie(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    year = models.PositiveIntegerField()
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    actors = models.TextField(help_text="Aktyorlarni vergul bilan ajrating")
    duration = models.CharField(max_length=20)
    rating = models.FloatField(default=0.0)
    is_featured = models.BooleanField(default=False)
    
    # Movie categories
    CATEGORY_CHOICES = [
        ('serial', 'Serial'),
        ('tarjima_kino', 'Tarjima Kino'),
        ('premyera', 'Premyera'),
        ('klassika', 'Klassika'),
        ('yangilik', 'Yangilik'),
        ('eng_yaxshi', 'Eng Yaxshi'),
    ]
    
    category = models.CharField(
        'Kategoriya',
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='yangilik'
    )
    
    # Media files
    poster_file = models.ImageField(upload_to='posters/', blank=True, null=True)
    poster_url = models.URLField(blank=True, null=True)
    video_file = models.FileField(upload_to='videos/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    trailer_url = models.URLField(blank=True, null=True)
    
    # Timestamp fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def get_poster(self):
        if self.poster_file:
            return self.poster_file.url
        return self.poster_url