from django import forms
from .models import Book, Note, Author, Publisher, Series, Genre, Topic

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'isbn', 'publication_date', 'pages', 'cover', 'language', 'publisher', 'authors', 'series', 'genres', 'topics']
        widgets = {
            'publication_date': forms.DateInput(attrs={'type': 'date'}),
        }

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Wpisz treść notatki...'}),
        }

class AuthorForm(forms.ModelForm):
    class Meta: model = Author; fields = '__all__'

class PublisherForm(forms.ModelForm):
    class Meta: model = Publisher; fields = '__all__'

class SeriesForm(forms.ModelForm):
    class Meta: model = Series; fields = '__all__'

class GenreForm(forms.ModelForm):
    class Meta: model = Genre; fields = '__all__'

class TopicForm(forms.ModelForm):
    class Meta: model = Topic; fields = '__all__'