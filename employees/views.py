from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView


# Create your views here.
class EmployeeDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class= EmployeeSerializer

