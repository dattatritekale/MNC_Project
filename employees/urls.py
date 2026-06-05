from django.urls import path
from .views import employee_list, create_employee, update_employee, delete_employee

urlpatterns=[
    path('employee/<int:id>/',employee_list),
    path('employee/create/',create_employee),
    path('employee/<int:id>/update/', update_employee),
    path('employee/<int:id>/delete/', delete_employee),
]