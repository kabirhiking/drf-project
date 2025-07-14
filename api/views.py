from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from api.serializers import EmployeeSerializer, StudentSerializer
from students.models import Student
from rest_framework.views import APIView
from employees.models import Employee
from django.http import Http404
from rest_framework import mixins, generics



# DRF serializatio
# function based serializer
@api_view(['GET', 'POST'])
def studentsView(request):
    if request.method == 'GET':
        # get all the data from the student table
        Students = Student.objects.all()
        serializer = StudentSerializer(Students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# manual serializers
# def studentsView(request):
#     students = Student.objects.all()
#     students_list = list(students.values()) 
#     # object or query set converted to JSON format (serializable)
#     return JsonResponse(students_list, safe=False)


# Complex data --> Serializers --> JSON(XML)


@api_view(['GET','PUT', 'DELETE'])
def studentDetailView(requst, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if requst.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif requst.method == 'PUT':
        serializer = StudentSerializer(student, data=requst.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif requst.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


# class based serializer
# class Employees(APIView):
#     def get(self, request):
#         empployees = Employee.objects.all()
#         serializer = EmployeeSerializer(empployees, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
        
#     def post(self, request):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
       

# class EmployeeDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             raise Http404
            
#     def get(self, request, pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)  
    
#     def put(self, request, pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
         
#     def delete(self, request, pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerializer(employee, data=request.data)
#         return Response(status=status.HTTP_204_NO_CONTENT)
    

# Mixins -->>Mixins are a way to reuse code in object-oriented programming. They allow you to add functionality to classes without using inheritance, effectively "mixing in" methods and properties from one class (the mixin) into another. 
# class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
    
#     def get(self, request):
#         return self.list(request)
    
#     def post(self, request):
#         return self.create(request)
    

# # mixin with primary key
# class EmployeeDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    # queryset = Employee.objects.all()
    # serializer_class = EmployeeSerializer
    
    # def get(self, request, pk):
    #     return self.retrieve(request, pk)
    
    # def put(self, request, pk):
    #     return self.update(request, pk)
    
    # def delete(self, request, pk):
    #     return self.destroy(request, pk)


# Generics
class Employees(generics.ListCreateAPIView):
     queryset = Employee.objects.all()
     serializer_class = EmployeeSerializer

# Generics with primary key
class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk' 
    
    