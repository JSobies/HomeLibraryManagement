from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from .models import Book, Author, Publisher, Genre, Series, Topic, Note
from .forms import BookForm, NoteForm, AuthorForm, PublisherForm, SeriesForm, GenreForm, TopicForm

# Scenariusz 1: Strona główna z filtrowaniem
def home(request):
    genre_id = request.GET.get('genre')
    topic_id = request.GET.get('topic')
    
    books = Book.objects.all()
    if genre_id:
        books = books.filter(genres__id=genre_id)
    if topic_id:
        books = books.filter(topics__id=topic_id)
        
    context = {
        'books': books,
        'favorite_books': Book.objects.filter(is_favorite=True),
        'read_books': Book.objects.filter(is_read=True),
        'genres': Genre.objects.all(),
        'topics': Topic.objects.all(),
    }
    return render(request, 'home.html', context)

# Scenariusz 4: Rejestracja użytkownika
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# Scenariusz 2 & 3 & 4 & 6: Szczegóły książki i Notatki
def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    notes = Note.objects.filter(book=book).order_by('-created_at')
    form = NoteForm()
    return render(request, 'book_detail.html', {'book': book, 'notes': notes, 'form': form})

@login_required
def add_note(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.book = book
            note.save()
    return redirect('book_detail', id=id)

@login_required
def toggle_read(request, id):
    book = get_object_or_404(Book, id=id)
    book.is_read = not book.is_read
    book.save()
    return redirect('book_detail', id=id)

@login_required
def toggle_favorite(request, id):
    book = get_object_or_404(Book, id=id)
    book.is_favorite = not book.is_favorite
    book.save()
    return redirect('book_detail', id=id)

# Scenariusz 5 & 6: CRUD Książki
class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book_form.html'
    def get_success_url(self): return reverse('book_detail', kwargs={'id': self.object.id})

class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book_form.html'
    pk_url_kwarg = 'id'
    def get_success_url(self): return reverse('book_detail', kwargs={'id': self.object.id})

class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'confirm_delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')

# Scenariusz 8, 9, 10: Podstrony słowników
def author_detail(request, id):
    author = get_object_or_404(Author, id=id)
    return render(request, 'author_detail.html', {'author': author, 'books': author.books.all()})

def publisher_detail(request, id):
    publisher = get_object_or_404(Publisher, id=id)
    return render(request, 'publisher_detail.html', {'publisher': publisher, 'books': Book.objects.filter(publisher=publisher)})

def series_detail(request, id):
    series = get_object_or_404(Series, id=id)
    books = Book.objects.filter(series=series).order_by('publication_date')
    return render(request, 'series_detail.html', {'series': series, 'books': books, 'count': books.count()})

# Scenariusz 7: Panel zarządzania słownikami (Dashboard + CRUD)
@login_required
def dictionaries_dashboard(request):
    return render(request, 'dictionaries_dashboard.html', {
        'authors': Author.objects.all(), 'publishers': Publisher.objects.all(),
        'series': Series.objects.all(), 'genres': Genre.objects.all(), 'topics': Topic.objects.all()
    })

class AuthorCreate(LoginRequiredMixin, CreateView): model = Author; form_class = AuthorForm; template_name = 'dict_form.html'; success_url = reverse_lazy('dictionaries')
class AuthorUpdate(LoginRequiredMixin, UpdateView): model = Author; form_class = AuthorForm; template_name = 'dict_form.html'; pk_url_kwarg = 'id'; success_url = reverse_lazy('dictionaries')
class AuthorDelete(LoginRequiredMixin, DeleteView): model = Author; template_name = 'confirm_delete.html'; pk_url_kwarg = 'id'; success_url = reverse_lazy('dictionaries')

class PublisherCreate(LoginRequiredMixin, CreateView): model = Publisher; form_class = PublisherForm; template_name = 'dict_form.html'; success_url = reverse_lazy('dictionaries')
class PublisherUpdate(LoginRequiredMixin, UpdateView): model = Publisher; form_class = PublisherForm; template_name = 'dict_form.html'; pk_url_kwarg = 'id'; success_url = reverse_lazy('dictionaries')
class PublisherDelete(LoginRequiredMixin, DeleteView): model = Publisher; template_name = 'confirm_delete.html'; pk_url_kwarg = 'id'; success_url = reverse_lazy('dictionaries')

class SeriesCreate(LoginRequiredMixin, CreateView): model = Series; form_class = SeriesForm; template_name = 'dict_form.html'; success_url = reverse_lazy('dictionaries')
class SeriesUpdate(LoginRequiredMixin, UpdateView): model = Series; form_class = SeriesForm; template_name = 'dict_form.html'; pk_url_kwarg = 'id'; success_url = reverse_lazy('dictionaries')
class SeriesDelete(LoginRequiredMixin, DeleteView): model = Series; template_name = 'confirm_delete.html'; pk_url_kwarg = 'id'; success_url = reverse_lazy('dictionaries')

class GenreCreate(LoginRequiredMixin, CreateView): model = Genre; form_class = GenreForm; template_name = 'dict_form.html'; success_url = reverse_lazy('dictionaries')
class GenreUpdate(LoginRequiredMixin, UpdateView): model = Genre; form_class = GenreForm; template_name = 'dict_form.html'; pk_url_kwarg = 'id'; success_url = reverse_lazy('dictionaries')
class GenreDelete(LoginRequiredMixin, DeleteView): model = Genre; template_name = 'confirm_delete.html'; pk_url_kwarg = 'id'; success_url = reverse_lazy('dictionaries')

class TopicCreate(LoginRequiredMixin, CreateView): model = Topic; form_class = TopicForm; template_name = 'dict_form.html'; success_url = reverse_lazy('dictionaries')
class TopicUpdate(LoginRequiredMixin, UpdateView): model = Topic; form_class = TopicForm; template_name = 'dict_form.html'; pk_url_kwarg = 'id'; success_url = reverse_lazy('dictionaries')
class TopicDelete(LoginRequiredMixin, DeleteView): model = Topic; template_name = 'confirm_delete.html'; pk_url_kwarg = 'id'; success_url = reverse_lazy('dictionaries')
