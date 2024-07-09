from django.urls import path
from . import api, views

urlpatterns = [

    path('', views.car_list, name="cars_list"),
    path('test/', views.test, name='test'),
    path('brands/', views.brands_list, name='brands_list'),
    path('brands/<str:name>/', views.car_list_by_brand, name="cars_list_by_brand"),
    path('api/', api.ListCreateCarView.as_view(), name="get_create_car"),
    path('api/<int:pk>/', api.UpdateDeleteCarView.as_view(), name="update_delete_car"),
    path('api/update/<int:pk>/', api.UpdateCarView.as_view(), name="update_car"),
    path('api/delete/<int:pk>/', api.DeleteCarView.as_view(), name="delete_car"),
]
