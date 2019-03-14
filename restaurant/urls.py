from django.urls import path
from . import views
# from django.views.generic import TemplateView

urlpatterns = [
    path('', views.RestaurantList.as_view(), name="restaurant"),
    path('add', views.RestaurantView.as_view(), name='add-restaturant'),
    path('dish/add', views.DishCreateView.as_view(), name = 'add-dish'),
    path('dish', views.DishView.as_view(), name='dish'),
    path('<int:pk>/dish', views.RestaurantDish.as_view(), name='restaurant-dish'),
]