from django.urls import path
from .views import EmployeeListCreateAPIView

urlpatterns=[
    path('employee/',EmployeeListCreateAPIView.as_view()),
    
]