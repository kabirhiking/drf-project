from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from api.serializers import StudentSerializer
from students.models import Student


# DRF serializ
@api_view(['GET'])
def studentsView(request):
    if request.method == 'GET':
        # get all the data from the student table
        Students = Student.objects.all()
        serializer = StudentSerializer(Students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



# manual serializers
# def studentsView(request):
#     students = Student.objects.all()
#     students_list = list(students.values()) 
#     # object or query set converted to JSON format (serializable)
#     return JsonResponse(students_list, safe=False)


# Complex data --> Serializers --> JSON(XML)