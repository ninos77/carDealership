from django.shortcuts import render,get_object_or_404
from .models import Car

# Create your views here.

def cars(request):
  all_cars = Car.objects.order_by('-created_date')
  data = {'all_cars':all_cars}
  return render (request,'cars/cars.html',data)


def car_detail(request, id):
  singel_car = get_object_or_404(Car,pk=id)
  data = {'singel_car':singel_car}
  return render (request,'cars/car_detail.html',data)

