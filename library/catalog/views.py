from django.http import HttpResponse
from django.shortcuts import render
from .models import Book, BookInstance
from django.views.generic import CreateView, DetailView
# Create your views here.


def index(request):

    num_book = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_insatnces_available = BookInstance.objects.filter(
        status__exact='a').count()
    context = {
        'numb_book': num_book,
        'num_instances': num_instances,
        'num_insatnces_available': num_insatnces_available
    }

    return render(request, 'catalog/index.html', context=context)


class BookCreate(CreateView):
    model = Book
    fields = '__all__'


class BookDetail(DetailView):
    model = Book
