from django.core.management.base import BaseCommand
from cinemadia.models import Movie


class Command(BaseCommand):
    help = 'Namuna filmlarni bazaga qo\'shadi'

    def handle(self, *args, **kwargs):
        # O'chirish (agar kerak bo'lsa)
        # Movie.objects.all().delete()

        movies_data = [
            {
                'title': 'Oppenheimer',
                'description': 'J. Robert Oppenheimer hayoti va atom bombasini yaratish jarayoni haqida film.',
                'year': 2023,
                'genre': 'Drama, Tarixiy',
                'director': 'Christopher Nolan',
                'actors': 'Cillian Murphy, Emily Blunt, Matt Damon',
                'duration': '3 soat',
                'rating': 8.5,
                'poster_url': 'https://image.tmdb.org/t/p/w500/8Gxv8gSFCU0XGDykEGv7zR1n2ua.jpg',
                'trailer_url': 'https://www.youtube.com/watch?v=uYPbbksJxIg',
                'is_featured': True,
                'category': 'premyera',
            },
            {
                'title': 'Barbie',
                'description': 'Barbie o\'zining mukammal dunyosidan chiqib, haqiqiy dunyoni kashf etadi.',
                'year': 2023,
                'genre': 'Komediya, Fantastika',
                'director': 'Greta Gerwig',
                'actors': 'Margot Robbie, Ryan Gosling, Will Ferrell',
                'duration': '1 soat 54 daqiqa',
                'rating': 7.2,
                'poster_url': 'https://image.tmdb.org/t/p/w500/iuFNMS8U5cb6xfzi51Dbkovj7vM.jpg',
                'trailer_url': 'https://www.youtube.com/watch?v=pBk4NYhWNMM',
                'is_featured': False,
                'category': 'tarjima_kino',
            },
            {
                'title': 'The Batman',
                'description': 'Yosh Batman Gotham shahridagi korrupsiya va jinoyatchilarni fosh etishga harakat qiladi.',
                'year': 2022,
                'genre': 'Action, Thriller',
                'director': 'Matt Reeves',
                'actors': 'Robert Pattinson, Zoë Kravitz, Paul Dano',
                'duration': '2 soat 56 daqiqa',
                'rating': 7.8,
                'poster_url': 'https://image.tmdb.org/t/p/w500/74xTEgt7R36Fpooo50r9T25onhq.jpg',
                'trailer_url': 'https://www.youtube.com/watch?v=mqqft2x_Aa4',
                'is_featured': False,
                'category': 'tarjima_kino',
            },
            {
                'title': 'Avatar: The Way of Water',
                'description': 'Jake Sully va Neytiri o\'z oilalari bilan Pandora okeanlarida yangi sarguzashtlarga kirishadilar.',
                'year': 2022,
                'genre': 'Sci-Fi, Fantastika',
                'director': 'James Cameron',
                'actors': 'Sam Worthington, Zoe Saldana, Sigourney Weaver',
                'duration': '3 soat 12 daqiqa',
                'rating': 7.6,
                'poster_url': 'https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg',
                'trailer_url': 'https://www.youtube.com/watch?v=d9MyW72ELq0',
                'is_featured': False,
                'category': 'tarjima_kino',
            },
            {
                'title': 'Spider-Man: Across the Spider-Verse',
                'description': 'Miles Morales multiverse bo\'ylab sarguzashtlarga kirishadi.',
                'year': 2023,
                'genre': 'Animatsiya, Action',
                'director': 'Joaquim Dos Santos',
                'actors': 'Shameik Moore, Hailee Steinfeld, Oscar Isaac',
                'duration': '2 soat 20 daqiqa',
                'rating': 8.7,
                'poster_url': 'https://image.tmdb.org/t/p/w500/8Vt6mWEReuy4Of61Lnj5Xj704m8.jpg',
                'trailer_url': 'https://www.youtube.com/watch?v=cqGjhVJWtEg',
                'is_featured': False,
                'category': 'multfilm',
            },
            {
                'title': 'Guardians of the Galaxy Vol. 3',
                'description': 'Qo\'riqchilar Star-Lord va Rocket Raccoon\'ni qutqarish uchun oxirgi missiyaga chiqadilar.',
                'year': 2023,
                'genre': 'Action, Komediya',
                'director': 'James Gunn',
                'actors': 'Chris Pratt, Zoe Saldana, Dave Bautista',
                'duration': '2 soat 30 daqiqa',
                'rating': 8.0,
                'poster_url': 'https://image.tmdb.org/t/p/w500/r2J02Z2OpNTctfOSN1Ydgii51I3.jpg',
                'trailer_url': 'https://www.youtube.com/watch?v=u3V5KDHRQvk',
                'is_featured': False,
                'category': 'tarjima_kino',
            },
            {
                'title': 'John Wick: Chapter 4',
                'description': 'John Wick butun dunyo bo\'ylab o\'z dushmanlari bilan kurashadi.',
                'year': 2023,
                'genre': 'Action, Thriller',
                'director': 'Chad Stahelski',
                'actors': 'Keanu Reeves, Donnie Yen, Bill Skarsgård',
                'duration': '2 soat 49 daqiqa',
                'rating': 8.1,
                'poster_url': 'https://image.tmdb.org/t/p/w500/vZloFAK7NmvMGKE7VkF5UHaz0I.jpg',
                'trailer_url': 'https://www.youtube.com/watch?v=qEVUtrk8_B4',
                'is_featured': False,
                'category': 'tarjima_kino',
            },
            {
                'title': 'Top Gun: Maverick',
                'description': 'Pete "Maverick" Mitchell yangi avlod uchuvchilarini o\'rgatadi.',
                'year': 2022,
                'genre': 'Action, Drama',
                'director': 'Joseph Kosinski',
                'actors': 'Tom Cruise, Jennifer Connelly, Miles Teller',
                'duration': '2 soat 10 daqiqa',
                'rating': 8.3,
                'poster_url': 'https://image.tmdb.org/t/p/w500/62HCnUTziyWcpDaBO2i1DX17ljH.jpg',
                'trailer_url': 'https://www.youtube.com/watch?v=giXco2jaZ_4',
                'is_featured': False,
                'category': 'tarjima_kino',
            },
            {
                'title': 'Dangal',
                'description': 'Hindistonlik qizlar uchun kurash sportini rivojlantirishga qaratilgan ilham beruvchi hikoya.',
                'year': 2016,
                'genre': 'Drama, Sport',
                'director': 'Nitesh Tiwari',
                'actors': 'Aamir Khan, Fatima Sana Shaikh, Sanya Malhotra',
                'duration': '2 soat 41 daqiqa',
                'rating': 8.4,
                'poster_url': 'https://image.tmdb.org/t/p/w500/4S4YvEjgN7iKdWxaGm7V8qFObMy.jpg',
                'trailer_url': 'https://www.youtube.com/watch?v=x_7YlGv9u1g',
                'is_featured': False,
                'category': 'hind',
            },
            {
                'title': 'Frozen 2',
                'description': 'Elsa va Anna sirlar bilan to\'la yangi sarguzashtlarga kirishadilar.',
                'year': 2019,
                'genre': 'Animatsiya, Musiqiy',
                'director': 'Chris Buck',
                'actors': 'Kristen Bell, Idina Menzel, Josh Gad',
                'duration': '1 soat 43 daqiqa',
                'rating': 7.0,
                'poster_url': 'https://image.tmdb.org/t/p/w500/mINJaaTj8XjC7x2f0HxSbpk3w2t.jpg',
                'trailer_url': 'https://www.youtube.com/watch?v=Zi4LMpSDccc',
                'is_featured': False,
                'category': 'multfilm',
            },
            {
                'title': 'Stranger Things',
                'description': 'Hawkins shahridagi bolalar g\'ayritabiiy hodisalarni tekshiradilar.',
                'year': 2016,
                'genre': 'Sci-Fi, Qo\'rqinchli',
                'director': 'Matt Duffer',
                'actors': 'Millie Bobby Brown, Finn Wolfhard, Winona Ryder',
                'duration': 'Serial',
                'rating': 8.7,
                'poster_url': 'https://image.tmdb.org/t/p/w500/49WJfeN0moxb9IPfGn8AIqMGskD.jpg',
                'trailer_url': 'https://www.youtube.com/watch?v=b9EkMc79ZSU',
                'is_featured': False,
                'category': 'serial',
            },
        ]

        created_count = 0
        for movie_data in movies_data:
            movie, created = Movie.objects.get_or_create(
                title=movie_data['title'],
                defaults=movie_data
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'✓ "{movie.title}" qo\'shildi')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'- "{movie.title}" allaqachon mavjud')
                )

        self.stdout.write(
            self.style.SUCCESS(f'\n✓ Jami {created_count} ta yangi film qo\'shildi!')
        )
