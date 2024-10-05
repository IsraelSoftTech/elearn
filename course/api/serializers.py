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


    def validate_name(self, value): 
        try:
            already_existing_course = Course.objects.filter(name=value)
            if(already_existing_course):
                raise serializers.ValidationError("Course already exist, choose another name.")
            else: 
                return value
        except Course.DoesNotExist:
            return value

   