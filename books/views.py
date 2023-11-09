from django.shortcuts import render
from .models import Book
# Create your views here.

def index(req):
    books = Book.objects.all()
    return render(req,'index.html',{ "books": books})
