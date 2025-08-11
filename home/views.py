from django.shortcuts import render
from .models import Restaurant

def home_view(request):
    restaurant=Restaurant.objects.first()
    restaurant_name=restaurant.name
if restaurant else "Restaurant Name Not Set"
    return render(request, 'home/index.html', {'restaurant_name': restaurant_name})
