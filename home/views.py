from django.shortcuts import render
from restaurant.models import Restaurant
from restaurant.models import Dish
# Create your views here.
def home_view(request):
    restaurants = Restaurant.objects.all()[:4]
    
    dishs = Dish.objects.all()[:4]
    print('dish===',dishs)
    return render(request, 'index.html', {'restaurants': restaurants, 'dishs': dishs})