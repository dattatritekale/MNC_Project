from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Employee
from .serializers import EmployeeSerializer
from django.db.models import Q

# Create your views here.

class EmployeeAPIView(APIView):
    def get(self, request):
        employee=Employee.objects.all()
        serializer=EmployeeSerializer(employee, many=True)

        return Response(serializer.data)
    
    def post(self, request):
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)