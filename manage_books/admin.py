from django.contrib import admin
from .models import Book, Author, Publisher, Genre, Series, Topic, Note

# Rejestracja modeli w panelu admina
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Genre)
admin.site.register(Series)
admin.site.register(Topic)
admin.site.register(Note)