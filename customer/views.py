from django.shortcuts import render
from .forms import CustomerForm
# Create your views here.
def customer(request):
    form = CustomerForm
    return render(request, 'customer.html',{'form':form})