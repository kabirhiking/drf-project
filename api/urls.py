from django.urls import path
from . import views

urlpatterns = [
    # function based url
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentDetailView),
    # class based url
    path('employees/', views.Employees.as_view()),
    path('employees/<int:pk>/', views.EmployeeDetail.as_view())
    
    
]
