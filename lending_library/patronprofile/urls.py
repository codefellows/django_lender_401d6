from django.conf.urls import url
from django.shortcuts import render
# from patronprofile.views import a_view
from books.models import Book


def a_view(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'patronprofile/profile.html', context=context)


urlpatterns = [
    url('^profile$', a_view, name='a_profile')
]
