from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import UserInfo

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ( 'id','Name', 'EmailAddress','ContactNumber','HomeAddress','Birthday','Nickname')
	
	


class ContactListSerializer(serializers.ModelSerializer):
    class Meta:
        model =  UserInfo
        fields = ('id','Name','EmailAddress','ContactNumber','Nickname')