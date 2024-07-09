from .models import Car
from .serializer import CarSerializer
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView, \
    RetrieveUpdateAPIView
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .permissions import IsCarOwner
# Create your views here.


class ListCreateCarView(ListCreateAPIView):
    model = Car
    serializer_class = CarSerializer

    # permission_classes = [IsAdminUser]
    def get_queryset(self):
        return Car.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = CarSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': "Create new car successfully"
            }, status=status.HTTP_200_OK)

        else:
            return JsonResponse({
                'message': "Failed to create new car"
            }, status=status.HTTP_400_BAD_REQUEST)


class UpdateCarView(RetrieveUpdateAPIView):
    model = Car
    serializer_class = CarSerializer
    permission_classes = [IsCarOwner | IsAdminUser]

    def get_queryset(self):
        return Car.objects.all()

    def update(self, request, *args, **kwargs):
        car = get_object_or_404(Car, id=kwargs.get('pk'))
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': "Update car successfully"
            }, status=status.HTTP_200_OK)

        else:
            return JsonResponse({
                'message': "Update car unsuccessfully"
            }, status=status.HTTP_400_BAD_REQUEST)


class DeleteCarView(RetrieveDestroyAPIView):
    model = Car
    serializer_class = CarSerializer
    permission_classes = [IsAdminUser | IsCarOwner]

    def get_queryset(self):
        return Car.objects.all()

    def delete(self, request, *args, **kwargs):
        car = get_object_or_404(Car, id=kwargs.get('pk'))
        car.delete()

        return JsonResponse({
            'message': "Delete car successfully"
        }, status=status.HTTP_200_OK)


class UpdateDeleteCarView(RetrieveUpdateDestroyAPIView):
    model = Car
    serializer_class = CarSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Car.objects.all()

    def update(self, request, *args, **kwargs):
        car = get_object_or_404(Car, id=kwargs.get('pk'))
        serializer = CarSerializer(car, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': "Update car successfully"
            }, status=status.HTTP_200_OK)

        else:
            return JsonResponse({
                'message': "Update car unsuccessfully"
            }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        car = get_object_or_404(Car, id=kwargs.get('pk'))
        car.delete()

        return JsonResponse({
            'message': "Delete car successfully"
        }, status=status.HTTP_200_OK)
