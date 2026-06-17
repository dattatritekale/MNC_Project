from django.urls import path
from .views import EmployeeDetailAPIView

urlpatterns=[
    path('employee/',EmployeeDetailAPIView.as_view()),
    path('employee/<int:pk>/',EmployeeDetailAPIView.as_view()),
    
]