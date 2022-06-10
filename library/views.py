from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,DeleteView,DetailView,UpdateView

from .models import Book

# Create your views here.

# List view of all the books from database using generic listview
class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = "library/homepage.html"

#  To add Book to database  using generic createview
#  LoginRequiredMixin : so only logged in user can add book
class BookCreateView(LoginRequiredMixin,CreateView):
    model = Book
    fields = ['name','author','no_of_pages']
    template_name = "library/book_create.html"

#  To Delete book from database using generic delete view
#  LoginRequiredMixin : so only logged in user can delete book
class BookDeleteView(LoginRequiredMixin,DeleteView):
    model = Book
    context_object_name = 'book'
    success_url = reverse_lazy('home')
    template_name = "library/book_delete.html"

# To get Book Details from database using generic detail view
class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = "library/book_detail.html"


# To update Book Details from database using generic update view
#  LoginRequiredMixin : so only logged in user can update book details
class BookUpdateView(LoginRequiredMixin,UpdateView):
    model = Book
    fields = ['name','author','no_of_pages']
    context_object_name = 'book'
    template_name = "library/book_update.html"

