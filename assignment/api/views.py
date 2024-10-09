from rest_framework.response import Response 
from .serializers import * 
from ..models import *
from rest_framework.views import APIView
from rest_framework import status

class AssignmentList(APIView): 
    def get(self, request):
        assignments = Assignment.objects.all()
        serializer = AssignmentSerializer(assignments, many=True)

        return Response(serializer.data)
    
    def post(self, request):
        serializer = AssignmentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({"message":"Assignment created successfully","data": serializer.data}, status=status.HTTP_201_CREATED)
        
        else: 
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class AssignmentDetail(APIView): 
    def get(self,request,pk): 
        assignment = Assignment.objects.get(pk=pk)
        serializer = AssignmentSerializer(assignment)

        return Response({"data": serializer.data})
    
    def put(self, request, pk): 
        assignment = Assignment.objects.get(pk=pk)
        serializer = AssignmentSerializer(assignment, data=request.data)

        if serializer.is_valid(): 
            serializer.save()

            return Response({"success": "Assignment successfully Updated", "data": serializer.data}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request,pk): 
        try:
            assignment = Assignment.objects.get(pk=pk)
        except Assignment.DoesNotExist: 
            return Response({"error": "No content"}, status=status.HTTP_204_NO_CONTENT)
        
        try: 
            assignment.delete()

        except: 
            return Response({"error": "Error Deleting Assignment"}, status=status.HTTP_400_BAD_REQUEST)
