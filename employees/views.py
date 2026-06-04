from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def employee_list(request):
    employess=[
         {
            "id": 1,
            "name": "Dattatri",
            "role": "Python Developer"
        },
        {
            "id": 2,
            "name": "Rahul",
            "role": "Backend Developer"
        }
    ]
    return Response(employess)