from http import server
from urllib import response
from django.shortcuts import render


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer

# Create your views here.

@api_view(['GET'])
def Employees_List(request):
    employees = Employee.objects.all()
    serializers = EmployeeSerializer(employees, many=True)
    return Response(serializers.data)


@api_view(['POST'])
def employees_add(request):
    
    serializers = EmployeeSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['POST'])
def employees_update(request, pk):
    employee = Employee.objects.get(id=pk)
    serializers = EmployeeSerializer(instance=employee, data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['DELETE'])
def employee_delete(request, pk):
    employee = Employee.objects.get(id=pk)
    employee.delete()
    return Response('Employee has succefully deleted')
