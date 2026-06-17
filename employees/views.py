from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.generics import ListCreateAPIView


# Create your views here.
class EmployeeListCreateAPIView(ListCreateAPIView):
    queryset=Employee.objects.all()
    serializer_class= EmployeeSerializer

