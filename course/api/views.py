from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from course.models import Course, Content
from .serializers import CourseSerializer, ContentSerializer
from assignment.api.serializers import AssignmentSerializer
from assignment.models import Assignment


class ContentList(APIView):
    def get(self, request, course_id):
        try: 
            course = Course.objects.get(pk=course_id)
        except Course.DoesNotExist: 
            return Response({"message": "No content"}, status=status.HTTP_404_NOT_FOUND)
        
        contents = course.content.all()
        
        serializer = ContentSerializer(contents, many=True)

        return Response({"data":serializer.data})
    
    def post(self,request, course_id):
        serializer = ContentSerializer(data=request.data)

        try:
            course = Course.objects.get(pk=course_id)
        except Course.DoesNotExist:
            return Response({"message": "Course does not exist!"}, status=status.HTTP_404_NOT_FOUND)

        if serializer.is_valid():
            serializer.save()

            # assigning the content to the course
            try:
                course.content.add(serializer.data['id'])
                course.save()
            except: 
                content = Content.objects.get(pk=serializer.data['id'])
                content.delete()
                return Response({"message":"That was an issue assigning content to course, try again"}, status=status.HTTP_406_NOT_ACCEPTABLE)

            return Response({"data":serializer.data}, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class ContentDetail(APIView): 
    def get(self, request, pk, course_id): 
        try:
            content = Content.objects.get(pk=pk)
        except Content.DoesNotExist:
            return Response({"message": "Content does not exist"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ContentSerializer(content)

        return Response({"data":serializer.data})

    def put(self,request,pk, course_id): 
        try:
            content = Content.objects.get(pk=pk)
        except Content.DoesNotExist:
            return Response({"message": "Content does not exist"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ContentSerializer(content, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({"data":serializer.data}, status=status.HTTP_200_OK )
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self,request, pk, course_id):
        try:
            content = Content.objects.get(pk=pk)
        except Content.DoesNotExist:
            return Response({"message": "Course does not exist"}, status=status.HTTP_404_NOT_FOUND)

        try:
            content.delete()
            return Response({"message": "Content deleted successfully."}, status=status.HTTP_200_OK)
        except NotImplementedError:
            return Response({"message": "There was an error trying to delete content."}, status=status.HTTP_400_BAD_REQUEST)

# Course assignment detail 
class CourseAssignmentDetail(APIView): 
    def get(self,request,course_id, assignment_id): 
        try:
            assignment = Assignment.objects.get(pk=assignment_id)
        except Assignment.DoesNotExist: 
            return Response({"message": "No content"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AssignmentSerializer(assignment)

        return Response({"data": serializer.data})
    
    def put(self, request, course_id, assignment_id): 
        try:
            assignment = Assignment.objects.get(pk=assignment_id)
        except Assignment.DoesNotExist: 
            return Response({"message": "No content"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AssignmentSerializer(assignment, data=request.data)

        if serializer.is_valid(): 
            serializer.save()

            return Response({"success": "Assignment successfully Updated", "data": serializer.data}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request,course_id, assignment_id): 
        try:
            assignment = Assignment.objects.get(pk=assignment_id)
        except Assignment.DoesNotExist: 
            return Response({"message": "No content"}, status=status.HTTP_404_NOT_FOUND)
        
        try: 
            assignment.delete()
            return Response({"message": "Assignement successfully deleted"}, status=status.HTTP_204_NO_CONTENT)
        except: 
            return Response({"message": "Error Deleting Assignment"}, status=status.HTTP_400_BAD_REQUEST)

# Course assignment
class CourseAssignmentList(APIView): 
    def get(self, request, course_id):
        try:
            course = Course.objects.get(pk=course_id)
        except Course.DoesNotExist: 
            return Response({"message": "No content"}, status=status.HTTP_404_NOT_FOUND)
        
        assignments = course.assignments.all()
        serializer = AssignmentSerializer(assignments, many=True)

        return Response({"data": serializer.data})
    
    def post(self, request, course_id):
        serializer = AssignmentSerializer(data=request.data)

        try:
            course = Course.objects.get(pk=course_id)
        except Course.DoesNotExist: 
            return Response({"message": "No content"}, status=status.HTTP_404_NOT_FOUND)
        
        if serializer.is_valid():
            serializer.save()

            try: 
                course.assignments.add(serializer.data['id'])
                course.save()
            except: 
                assignment = Assignment.objects.get(pk=serializer.data['id'])
                assignment.delete()

                return Response({"error": "There was an error creating a course assignment"}, status=status.HTTP_400_BAD_REQUEST)

            return Response({"message":"Assignment created successfully","data": serializer.data}, status=status.HTTP_201_CREATED)
        
        else: 
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class CourseList(APIView): 
    def get(self, request): 
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)

        data = []
        for course in serializer.data: 
            course_data = {'id': course['id'], 'title': course['name'], 'enrolled_students': len(course['enrolled_students']), 'teachers': len(course['teacher']), 'completion': 0}
            data.append(course_data)

        return Response({"data":data, "total_courses": len(data), "inactive_courses": 0})
    
    def post(self, request): 
        serializer = CourseSerializer(data=request.data)

        if serializer.is_valid(): 
            serializer.save()

            return Response({"data":serializer.data})
        
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class CourseDetails(APIView):
    def get(self,request,pk): 
        try:
            course = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response({"message": "Course does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CourseSerializer(course)
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        try:
            course = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response({"message": "Course does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CourseSerializer(course,data=request.data)


        course_content = request.data.get('course_content', None)
        

        if serializer.is_valid(): 
            serializer.save()

            # updating the course content
            if course_content:
                content_data = []
                content = {}
                for id in course_content: 
                    try:
                        content = Content.objects.get(pk=id)
                        content_data.append(content)
                    except Content.DoesNotExist: 
                        continue
                if content:
                    course.content.add(content)
                    course.save()



            return Response({"data":serializer.data})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, pk):
        try:
            course = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response({"message": "Course does not exist"}, status=status.HTTP_404_NOT_FOUND)

        try:
            course.delete()
            return Response({"message": "Course deleted successfully"}, status=status.HTTP_200_OK)
        except NotImplementedError:
            return Response({"message": "There was an error trying to delete course"}, status=status.HTTP_400_BAD_REQUEST)