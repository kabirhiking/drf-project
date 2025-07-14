from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees', views.EmployeeViewset, basename='employee')


urlpatterns = [
    # function based url
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentDetailView),
    # class based url
    # path('employees/', views.Employees.as_view()),
    # path('employees/<int:pk>/', views.EmployeeDetail.as_view())
    
    path('', include(router.urls))
    
    
]
