from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    
    # Książki (Scenariusze 2, 3, 5, 6)
    path('book/add/', views.BookCreateView.as_view(), name='book_add'),
    path('book/<int:id>/', views.book_detail, name='book_detail'),
    path('book/<int:id>/edit/', views.BookUpdateView.as_view(), name='book_edit'),
    path('book/<int:id>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
    path('book/<int:id>/toggle-read/', views.toggle_read, name='toggle_read'),
    path('book/<int:id>/toggle-favorite/', views.toggle_favorite, name='toggle_favorite'),
    path('book/<int:id>/note/', views.add_note, name='add_note'),
    
    # Podstrony słowników (Scenariusze 8, 9, 10)
    path('author/<int:id>/', views.author_detail, name='author_detail'),
    path('publisher/<int:id>/', views.publisher_detail, name='publisher_detail'),
    path('series/<int:id>/', views.series_detail, name='series_detail'),
    
    # Zarządzanie Słownikami - Dashboard i CRUD (Scenariusz 7)
    path('dictionaries/', views.dictionaries_dashboard, name='dictionaries'),
    
    path('author/add/', views.AuthorCreate.as_view(), name='author_add'),
    path('author/<int:id>/edit/', views.AuthorUpdate.as_view(), name='author_edit'),
    path('author/<int:id>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
    
    path('publisher/add/', views.PublisherCreate.as_view(), name='publisher_add'),
    path('publisher/<int:id>/edit/', views.PublisherUpdate.as_view(), name='publisher_edit'),
    path('publisher/<int:id>/delete/', views.PublisherDelete.as_view(), name='publisher_delete'),
    
    path('series/add/', views.SeriesCreate.as_view(), name='series_add'),
    path('series/<int:id>/edit/', views.SeriesUpdate.as_view(), name='series_edit'),
    path('series/<int:id>/delete/', views.SeriesDelete.as_view(), name='series_delete'),

    path('genre/add/', views.GenreCreate.as_view(), name='genre_add'),
    path('genre/<int:id>/edit/', views.GenreUpdate.as_view(), name='genre_edit'),
    path('genre/<int:id>/delete/', views.GenreDelete.as_view(), name='genre_delete'),

    path('topic/add/', views.TopicCreate.as_view(), name='topic_add'),
    path('topic/<int:id>/edit/', views.TopicUpdate.as_view(), name='topic_edit'),
    path('topic/<int:id>/delete/', views.TopicDelete.as_view(), name='topic_delete'),
]