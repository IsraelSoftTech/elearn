from rest_framework.response import Response 
from .serializers import * 
from ..models import *
from rest_framework.views import APIView
from rest_framework import status


class MCQChoiceDetail(APIView): 
    def get(self,request,pk): 
        try:
            mcq_choice = MCQChoice.objects.get(pk=pk)
        except MCQChoice.DoesNotExist: 
            return Response({"message": "No content"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MCQChoiceSerializer(mcq_choice)

        return Response({"data": serializer.data})
    
    def put(self, request, pk): 
        try:
            mcq_choice = MCQChoice.objects.get(pk=pk)
        except MCQChoice.DoesNotExist: 
            return Response({"message": "No content"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MCQChoiceSerializer(mcq_choice, data=request.data)

        if serializer.is_valid(): 
            serializer.save()

            return Response({"success": "MCQ Choice successfully Updated", "data": serializer.data}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request,pk): 
        try:
            mcq_choice = MCQChoice.objects.get(pk=pk)
        except MCQQuestion.DoesNotExist: 
            return Response({"message": "No content"}, status=status.HTTP_404_NOT_FOUND)
        
        try: 
            mcq_choice.delete()
            return Response({"message": "MCQ Choice successfully deleted"}, status=status.HTTP_204_NO_CONTENT)
        except: 
            return Response({"message": "Error Deleting Assignment"}, status=status.HTTP_400_BAD_REQUEST)


class MCQChoiceList(APIView): 
    def get(self, request):
        try:
            mcq_choices = MCQChoice.objects.all()
        except MCQChoice.DoesNotExist: 
            return Response({"message": "No content"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MCQChoiceSerializer(mcq_choices, many=True)

        return Response({"data": serializer.data})
    
    def post(self, request):
        serializer = MCQChoiceSerializer(data=request.data)
        mcq_id = request.data['mcq-question']

        try: 
            mcq_question = MCQQuestion.objects.get(pk=mcq_id)
        except  Assignment.DoesNotExist: 
            return Response({"message": "Failed, MCQ question doesn't exist"}, status=status.HTTP_404_NOT_FOUND)

        if serializer.is_valid():
            serializer.save()
            mcq_choice = MCQChoice.objects.get(pk=serializer.data['id'])
            try: 
                print(mcq_question)
                mcq_question.choices.add(mcq_choice)
                mcq_question.save()
            except: 
                mcq_choice.delete()
                return Response({"There was an error assigning the choice to the MCQ question"})
            return Response({"message":"MCQ choice created successfully","data": serializer.data}, status=status.HTTP_201_CREATED)
        
        else: 
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        


class MCQQuestionDetail(APIView): 
    def get(self,request,pk): 
        try:
            mcq_question = MCQQuestion.objects.get(pk=pk)
        except Assignment.DoesNotExist: 
            return Response({"message": "No content"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MCQQuestionSerializer(mcq_question)

        return Response({"data": serializer.data})
    
    def put(self, request, pk): 
        try:
            mcq_question = MCQQuestion.objects.get(pk=pk)
        except MCQQuestion.DoesNotExist: 
            return Response({"message": "No content"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MCQQuestionSerializer(mcq_question, data=request.data)

        if serializer.is_valid(): 
            serializer.save()

            return Response({"success": "MCQ Question successfully Updated", "data": serializer.data}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request,pk): 
        try:
            mcq_question = MCQQuestion.objects.get(pk=pk)
        except MCQQuestion.DoesNotExist: 
            return Response({"message": "No content"}, status=status.HTTP_404_NOT_FOUND)
        
        try: 
            mcq_question.delete()
            return Response({"message": "MCQ Question successfully deleted"}, status=status.HTTP_204_NO_CONTENT)
        except: 
            return Response({"message": "Error Deleting Assignment"}, status=status.HTTP_400_BAD_REQUEST)


class MCQQuestionList(APIView): 
    def get(self, request):
        try:
            mcqQuestions = MCQQuestion.objects.all()
        except Assignment.DoesNotExist: 
            return Response({"message": "No content"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MCQQuestionSerializer(mcqQuestions, many=True)

        return Response({"data": serializer.data})
    
    def post(self, request):
        serializer = MCQQuestionSerializer(data=request.data)
        assignment_id = request.data['assignment']

        try: 
            assingment = Assignment.objects.get(pk=assignment_id)
        except  Assignment.DoesNotExist: 
            return Response({"message": "Failed, assignement doesn't exist"}, status=status.HTTP_404_NOT_FOUND)

        if serializer.is_valid():
            serializer.save()
            mcq_question = MCQQuestion.objects.get(pk=serializer.data['id'])
            try: 
                assingment.mcq_questions.add(mcq_question)
                assingment.save()
            except: 
                mcq_question.delete()
                return Response({"There was an error assigning the question to the assignement"})
            return Response({"message":"MCQ Question created successfully","data": serializer.data}, status=status.HTTP_201_CREATED)
        
        else: 
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        


class AssignmentList(APIView): 
    def get(self, request):
        try:
            assignments = Assignment.objects.all()
        except Assignment.DoesNotExist: 
            return Response({"message": "No content"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AssignmentSerializer(assignments, many=True)

        return Response({"data": serializer.data})
    
    def post(self, request):
        serializer = AssignmentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({"message":"Assignment created successfully","data": serializer.data}, status=status.HTTP_201_CREATED)
        
        else: 
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class AssignmentDetail(APIView): 
    def get(self,request,pk): 
        try:
            assignment = Assignment.objects.get(pk=pk)
        except Assignment.DoesNotExist: 
            return Response({"message": "No content"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AssignmentSerializer(assignment)

        return Response({"data": serializer.data})
    
    def put(self, request, pk): 
        try:
            assignment = Assignment.objects.get(pk=pk)
        except Assignment.DoesNotExist: 
            return Response({"message": "No content"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AssignmentSerializer(assignment, data=request.data)

        if serializer.is_valid(): 
            serializer.save()

            return Response({"success": "Assignment successfully Updated", "data": serializer.data}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request,pk): 
        try:
            assignment = Assignment.objects.get(pk=pk)
        except Assignment.DoesNotExist: 
            return Response({"message": "No content"}, status=status.HTTP_404_NOT_FOUND)
        
        try: 
            assignment.delete()
            return Response({"message": "Assignement successfully deleted"}, status=status.HTTP_204_NO_CONTENT)
        except: 
            return Response({"message": "Error Deleting Assignment"}, status=status.HTTP_400_BAD_REQUEST)
