from rest_framework import serializers
from course.models import Content, Course

class ContentSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Content
        fields = "__all__"



class CourseSerializer(serializers.ModelSerializer):
    content = ContentSerializer(many=True, read_only=True)  # Assuming you want to allow updating the content


    class Meta:
        model = Course
        fields = "__all__"

   