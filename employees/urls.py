from django.urls import path
from .views import employee_list, create_employee

urlpatterns=[
    path('employee/',employee_list),
    path('employee/create/',create_employee),
]