from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.viewsets import ModelViewSet


# Create your views here.
class EmployeeViewset(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class= EmployeeSerializer

