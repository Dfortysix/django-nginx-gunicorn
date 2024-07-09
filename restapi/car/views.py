from django.shortcuts import render
from .models import Car, Manufacturer
from django.core.paginator import Paginator
from django.db.models import Q, Min, Max


# Create your views here
def car_list(request):
    query = request.GET.get("query")
    price_query = request.GET.get("price")
    cars = Car.objects.all().order_by('price')
    # min_car_price = round(cars.first().price)
    # max_car_price = round(cars.last().price)
    price_stats = cars.aggregate(min_price=Min('price'), max_price=Max('price'))
    min_car_price = round(price_stats['min_price'])
    max_car_price = round(price_stats['max_price'])
    if query:
        cars = cars.filter(name__icontains=query).order_by('price')
    if price_query:
        cars = cars.filter(Q(price__gte=min_car_price) &
                           Q(price__lte=price_query))

    range_price = round((max_car_price - min_car_price) / 5)
    paginator = Paginator(cars, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'cars': cars,
        'page_obj': page_obj,
        'max_price': max_car_price,
        'min_price': min_car_price,
        'range_price': range_price
    }
    return render(request, 'car/carlist.html', context=context)


def car_list_by_brand(request, name):
    cars = Car.objects.all().filter(brand__name=name)
    context = {
        'cars': cars
    }
    print(cars)
    return render(request, 'car/carlist_bybrand.html', context=context)


def brands_list(request):
    brands = Manufacturer.objects.all().order_by('name')
    context = {
        'manufacturers': brands
    }
    return render(request, 'car/manufacturers_list.html', context=context)


def test(request):
    brands = Manufacturer.objects.all().order_by('name')
    context = {
        'manufacturers': brands
    }
    return render(request, 'car/manufacturers_list.html', context=context)
