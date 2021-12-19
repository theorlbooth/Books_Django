from django.shortcuts import render
from django.views import View
from .models import Book

class BookListView(View):

    def get(self, request):
        books = Book.objects.all()
        return render(request, 'index.html', { 'books': books })

class BookDetailView(View):

    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        return render(request, 'show.html', { 'book': book })

