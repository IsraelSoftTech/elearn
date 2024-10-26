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
    teachers = serializers.SerializerMethodField()
    enrolled_students = serializers.SerializerMethodField()
    assignments = serializers.SerializerMethodField()

    # change this into a serializerMethod that will get all of the classes
    classes = serializers.IntegerField(default=0, read_only=True)
    progress = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = "__all__"

    def get_assignments(self,obj): 
        return len(obj.assignments.all())

    def get_enrolled_students(self, obj): 
        return len(obj.enrolled_students.all())

    def get_teachers(self,obj): 
        return len(obj.teachers.all())
    

    def get_content(self, obj): 
        allContent = obj.content.all()
        courseContent = []
        for content in allContent: 
            content_stat = {"id": content.pk, "title": content.title, "progress": content.course_progress()}
            courseContent.append(content_stat)

        return courseContent
    
    def get_progress(self, obj): 
        allContent = obj.content.all()
        contentProgress = 0

        for content in allContent: 
            contentProgress += content.course_progress()
        # ensuring no division by 0 issue
        try: 
            courseProgress = (contentProgress/len(allContent)) 
        except: 
            courseProgress = 0 

        return courseProgress

 
 
    def validate_title(self, value): 
        try:
            already_existing_course = Course.objects.filter(title=value)
            if(already_existing_course):
                raise serializers.ValidationError("Course already exist, choose another name.")
            else: 
                return value
        except Course.DoesNotExist:
            return value

   