from django.shortcuts import render 

def home(request):
    """
    Renders the homepage of the restaurant.

    This view prepares a context dictionary containning the restaurant's name
    and a welcome message, which are then passed to the template for display.
    """
    context={
        'restaurant_name': 'Full Moon',
        'welcome_message': 'Welcome to our website!',
    }
    return render(request, 'home/index.html', context)
