from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from course.models import Course, Content
from .serializers import CourseSerializer, ContentSerializer


class ContentList(APIView):
    def get(self, request):
        contents = Content.objects.all()
        serializer = ContentSerializer(contents, many=True)

        return Response(serializer.data)
    
    def post(self,request):
        serializer = ContentSerializer(data=request.data)

        course_id = request.data.get('course', None)

        # checking to see is a course is passed
        if course_id is None:
            return Response({"message": "Can not create content without an associative course"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            course = Course.objects.get(pk=course_id)
        except Course.DoesNotExist:
            return Response({"message": "Course does not exist!"}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()

            # assigning the content to the course
            try:
                course.content.add(serializer.data['id'])
                course.save()
            except: 
                print(serializer)
                serializer.delete()
                return Response({"message":"That was an issue assigning content to course, try again"}, status=status.HTTP_406_NOT_ACCEPTABLE)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class ContentDetail(APIView): 
    def get(self, request, pk): 
        try:
            content = Content.objects.get(pk=pk)
        except Content.DoesNotExist:
            return Response({"message": "Content does not exist"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ContentSerializer(content)

        return Response(serializer.data)

    def put(self,request,pk): 
        try:
            content = Content.objects.get(pk=pk)
        except Content.DoesNotExist:
            return Response({"message": "Content does not exist"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ContentSerializer(content, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK )
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self,request, pk):
        try:
            content = Content.objects.get(pk=pk)
        except Content.DoesNotExist:
            return Response({"message": "Course does not exist"}, status=status.HTTP_404_NOT_FOUND)

        try:
            content.delete()
            return Response({"message": "Content deleted successfully."}, status=status.HTTP_200_OK)
        except NotImplementedError:
            return Response({"message": "There was an error trying to delete content."}, status=status.HTTP_400_BAD_REQUEST)


class CourseList(APIView): 
    def get(self, request): 
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)

        return Response(serializer.data)
    
    def post(self, request): 
        serializer = CourseSerializer(data=request.data)

        if serializer.is_valid(): 
            serializer.save()

            return Response(serializer.data)
        
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class CourseDetails(APIView):
    def get(self,request,pk): 
        try:
            course = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response({"message": "Course does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CourseSerializer(course)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
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



            return Response(serializer.data)
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