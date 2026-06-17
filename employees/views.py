from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters


# Create your views here.
class EmployeeViewset(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class= EmployeeSerializer

    filter_backends =[
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    search_fields =[
        'name',
        'designation'
    ]

    ordering_fields=[
        'name',
        'created_at'
    ]

