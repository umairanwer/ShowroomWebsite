from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def BrandsListView(request):
    brands = CarBrand.objects.all()
    return render(request, 'showroom/list_brands.html', {'brands':brands})
    return HttpResponse(f'<h1>Brands List Page</h1><p>{brands[0]}</p>')

def CarModelsView(request, brand_id):
    carModels = CarModel.objects.all().filter(carBrand_id = brand_id)
    return render(request, 'showroom/list_models.html', {'carmodels':carModels})
    return HttpResponse(f'<h1>Car Models List Page</h1><p>{carModels[1]}</p>')


def CarsListView(request, brand_id, car_model_id):
    carModelList = Car.objects.all().filter(carModel_id = car_model_id)
    return render(request, 'showroom/list_cars.html', {'cars_list':carModelList})

def CarView(request, brand_id, car_model_id, car_id):
    car_details = Car.objects.get(chassis_num = car_id)

    return render(request, 'showroom/car_details.html', {'car_details':car_details})
    return HttpResponse(f'<h1>{car_details}</h1>')

def OurStaffView(request):
    staffMembers = Staff.objects.all()
    return render(request, 'showroom/staff_members.html', {'staff_members':staffMembers})
