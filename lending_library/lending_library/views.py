"""Views for the base of my site."""
from django.shortcuts import render


def home_view(request):
    """View for the home page."""
    return render(
        request,
        'lending_library/home.html',
        context={}
    )
