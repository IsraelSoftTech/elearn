from rest_framework import serializers
from user.models import Profile, Discussion
from django.contrib.auth.models import User

class UsrSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class ProfileSerializer(serializers.ModelSerializer): 
    user = UsrSerializer(many=True, read_only=True)

    class Meta: 
        model=Profile 
        fields= "__all__"


class DiscussionSerializer(serializers.ModelSerializer): 
    # user = ProfileSerializer(read_only=True)

    class Meta: 
        model = Discussion
        fields = "__all__"