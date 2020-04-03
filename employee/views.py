from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from employee.serializers import EmployeeTypeSerializer, ProductSerializer
from employee.models import EmployeeType, Product
# Create your views here.


def index(request):
    # return HttpResponse("Successfully created Employee app")
    return render(request, 'employee/home.html')


class EmployeeTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows EmployeeType to be viewed or edited.
    """
    lookup_field = 'id'
    serializer_class = EmployeeTypeSerializer

    def get_queryset(self):
        return EmployeeType.objects.all()


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Product to be viewed or edited.
    """
    lookup_field = 'id'
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()