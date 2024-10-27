from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView 
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.contrib.auth.models import User
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError


class CreateUser(APIView): 
    def post(self,request): 
        print(request.data)
        try:
            username = request.data.get('username')
            first_name = request.data.get('first_name')
            last_name = request.data.get('last_name')
            email = request.data.get('email')
            password = request.data.get('password')
            password2 = request.data.get('password2')
        except Exception: 
            return Response({"error": "All fields were not provide, username, first_name, last_name, email, password and password 2 are required!"}, status=status.HTTP_400_BAD_REQUEST)

        #  checking if a user already exist with wthis username or email. 
        try: 
            user_alread_exist = User.objects.get(username=username)
            return Response({"error": "User with this username already exist, pick another!"}, status=status.HTTP_400_BAD_REQUEST)
        except: 
            pass 
        
        try: 
            user_alread_exist = User.objects.get(email=email)
            return Response({"error": "User with this email already exist, pick another!"}, status=status.HTTP_400_BAD_REQUEST)
        except: 
            pass 
        
        # validating the user info 
        # checking if the passwords are the same 
        if password != password2:
            return Response({"error": "Sorry your passwords doesn't match."}, status=status.HTTP_400_BAD_REQUEST)
        
        # validating a user's email
        email_validator = EmailValidator(message='Enter a valid email address!')
        try: 
            email_validator(email)
        except ValidationError as e: 
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        # creating a user
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
        except: 
            return Response({"error": "There was an error creating account, please try again later!"}, status=status.HTTP_400_BAD_REQUEST)

        # if user was created 
        refresh = RefreshToken.for_user(user)
        return Response({
                'username': user.username, 
                'first_name': user.first_name, 
                'last_name': user.last_name, 
                'full_name': user.get_full_name(),
                'email': user.email,
                'refresh': str(refresh), 
                'access': str(refresh.access_token),
            })



class LoginUser(APIView): 
    def post(self, request): 
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None: 
            refresh = RefreshToken.for_user(user)

            return Response({
                'username': user.username, 
                'first_name': user.first_name, 
                'last_name': user.last_name, 
                'full_name': user.get_full_name(),
                'email': user.email,
                'refresh': str(refresh), 
                'access': str(refresh.access_token),
            })
        else: 
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)