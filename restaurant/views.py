from django.shortcuts import render
from .forms import RestaurantForm
from django.views.generic import CreateView, ListView, View
from .models import Restaurant, Dish
# # Create your views here.
# def restaurants_view(req):
#     form = RestaurantForm
#     return render(req, 'restaurant.html', {'form':form})


class RestaurantView(CreateView):
    template_name = 'restaurant_form.html'
    model = Restaurant
    fields = '__all__'
    success_url = '/restaurant'


class RestaurantList(ListView):
    template_name = 'restaurant.html'
    model = Restaurant
    success_url = '/restaurant'


class DishCreateView(CreateView):
    model = Dish
    fields = '__all__'
    success_url = '/restaurant'


class DishView(View):
    template_name = 'dish.html'

    def get(self, request, *args, **kwargs):
        dishs = Dish.objects.all()
        return render(request, self.template_name, {'dishs': dishs})

class RestaurantDish(View):
    template_name = 'dish.html'

    def get(self, request, *args, **kwargs):
        dishs = Dish.objects.filter(restaurant_name=kwargs['pk'])
        return render(request, self.template_name, {'dishs': dishs})