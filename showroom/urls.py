from django.urls import path
from . import views

app_name = 'showroom'

urlpatterns = [
    path('',views.BrandsListView, name='brands_list'),

    path('<int:brand_id>', views.CarModelsView, name='car_models_detail'),
    path('<int:brand_id>/<int:car_model_id>', views.CarsListView, name='cars_list'),
    path('<int:brand_id>/<int:car_model_id>/<str:car_id>', views.CarView, name='car_details'),
    path('staff', views.OurStaffView, name='staff_members_page')

]
