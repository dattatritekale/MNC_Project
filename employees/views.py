from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Employee
from .serializers import EmployeeSerializer
from django.db.models import Q

# Create your views here.

class EmployeeListAPIView(APIView):
    def get(self, request):
        employee=Employee.objects.all()
        serializer=EmployeeSerializer(employee, many=True)

        return Response(serializer.data)
    