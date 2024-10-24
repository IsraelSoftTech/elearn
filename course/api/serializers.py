from rest_framework import serializers
from course.models import Content, Course

import json

class ContentSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Content
        fields = "__all__"



class CourseSerializer(serializers.ModelSerializer):
    # content = ContentSerializer(many=True, read_only=True)
    content = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = "__all__"

    def get_content(self, obj): 
        allContent = obj.content.all()
        courseContent = []
        for content in allContent: 
            content_stat = {"id": content.pk, "title": content.title, "progress": content.course_progress()}
            courseContent.append(content_stat)
            
        return courseContent
 
 
    def validate_title(self, value): 
        try:
            already_existing_course = Course.objects.filter(title=value)
            if(already_existing_course):
                raise serializers.ValidationError("Course already exist, choose another name.")
            else: 
                return value
        except Course.DoesNotExist:
            return value

   