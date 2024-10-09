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
    choices = MCQChoiceSerializer(many=True, read_only=True)

class StructuralQuestionSerializer(serializers.ModelSerializer): 
    class Meta:
        model = StructuralQuestion
        fields = "__all__"



class MCQStudentAnswerSerializer(serializers.ModelSerializer): 
    class Meta:
        model = MCQStudentAnswer
        fields = "__all__"

class StructuralStudentAnswerSerializer(serializers.ModelSerializer): 
    class Meta:
        model = StructuralStudentAnswer
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
    
    mcq_answers = MCQStudentAnswerSerializer(many=True, read_only=True)
    stuctural_answers = StructuralStudentAnswerSerializer(many=True, read_only=True)

class AssignmentSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Assignment
        fields = "__all__"

    mcq_questions = MCQQuestionSerializer(many=True, read_only=True)
    struct_questions = StructuralQuestionSerializer(many=True, read_only=True)
    students_submissons = AssignAssignmentSubmissionSerializer(many=True, read_only=True)