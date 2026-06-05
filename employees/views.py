from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Employee
from .serializers import EmployeeSerializer

# Create your views here.

@api_view(['GET'])
def employee_list(request):
    employees=Employee.objects.all()

    serializer=EmployeeSerializer(employees,many=True)
    
    return Response(serializer.data)

@api_view(['POST'])
def create_employee(request):
    
    serializer= EmployeeSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors)