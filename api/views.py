from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from api.serializers import StudentSerializer
from students.models import Student


# DRF serializatio
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


@api_view(['GET'])
def studentDetailView(requst, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if requst.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)