from rest_framework import serializers
from ..models import * 

class MCQChoiceSerializer(serializers.ModelSerializer): 
    class Meta:
        model = MCQChoice
        fields = "__all__"


class MCQQuestionSerializer(serializers.ModelSerializer): 
    class Meta:
        model = MCQQuestion
        fields = "__all__"

class StructuralQuestionSerializer(serializers.ModelSerializer): 
    class Meta:
        model = StructuralQuestion
        fields = "__all__"

class AssignmentSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Assignment
        fields = "__all__"

class MCQStudentAnswerSerializer(serializers.ModelSerializer): 
    class Meta:
        model = MCQStudentAnswer
        fields = "__all__"

class StructuralStudentAnswerSerializer(serializers.ModelSerializer): 
    class Meta:
        model = StructuralStudentAnswer
        fields = "__all__"


class AssignAssignmentSubmissionSerializer(serializers.ModelSerializer): 
    class Meta:
        model = AssignAssignmentSubmission
        fields = "__all__"