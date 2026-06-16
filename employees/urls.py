from django.urls import path
from .views import EmployeeListAPIView

urlpatterns=[
    path('employee/',EmployeeListAPIView.as_view()),
    
]