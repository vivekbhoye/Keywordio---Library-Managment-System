from django.urls import path
from .views import BookListView, BookCreateView, BookDeleteView, BookDetailView,BookUpdateView

urlpatterns = [
    path('', BookListView.as_view(), name='home'),
    path('book/new/', BookCreateView.as_view(), name='book-create'),
    path('book/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
    path('book/detail/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('book/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
]
