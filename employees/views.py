from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Employee
from .serializers import EmployeeSerializer

# Create your views here.

@api_view(['GET'])
def employee_list(request,id):

    try:
        employees=Employee.objects.get(id=id)
    

        serializer=EmployeeSerializer(employees)
    
        return Response(serializer.data)
    
    except Employee.DoesNotExist:

        return Response(
            {"error":"Emploee not found"},
            status=404
        )

@api_view(['POST'])
def create_employee(request):
    
    serializer= EmployeeSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors)

@api_view(['PUT'])
def update_employee(request, id):
    try:
        employees=Employee.objects.get(id=id)

    except Employee.DoesNotExist:
        return Response(
            {"messege":"Employee not found"},
            status=404
        )
    
    serializer=EmployeeSerializer(employees, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(
        serializer.errors,
        status=400
    )

@api_view(['DELETE'])
def delete_employee(reqest, id):
    try:
        employees=Employee.objects.get(id=id)

    except Employee.DoesNotExist:
        return Response(
            {"error":"Employee does not exist"},
            status=404
        )
    employees.delete()

    return Response(
        {"message":"Employee deleted successfully"},
        status=200
    )
    