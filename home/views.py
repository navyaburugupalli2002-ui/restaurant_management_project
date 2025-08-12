from django.shortcuts import render
from django.conf import settings  

def index(request):
    context={
        'phone_number':settings.RESTAURANT_PHONE_NUMBER,
    }
    return render(request, 'home/index.html', context)
