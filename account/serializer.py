from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from blogosphere.serializers import UserProfileSerializer,BlogSerializer


class RegisterSerializer(serializers.Serializer):
  first_name = serializers.CharField()
  last_name = serializers.CharField()
  username = serializers.CharField()
  email = serializers.CharField()
  password = serializers.CharField()
  user_profile=UserProfileSerializer(read_only=True)
  blogs=BlogSerializer(many=True, read_only=True)

  def validate(self, data):

    if User.objects.filter(username = data['username']).exists():

      raise serializers.ValidationError('username is taken')
    
    return data
  
  def create(self, validated_data):
    user = User.objects.create_user(
      first_name = validated_data['first_name'],
      last_name = validated_data['last_name'],
      username = validated_data['username'].lower(),
      email = validated_data['email'],
      password = validated_data['password']
    )
   
    return validated_data
  

class LoginSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField()

  def validate(self, data):

    if not User.objects.filter(username = data['username']).exists():

      raise serializers.ValidationError('Account not found')
    
    return data
  
  def get_jwt_token(self, data):

    user = authenticate(username = data['username'], password = data['password'])
    print(user)
    
    if not user:
      return {'message': 'invalid credentials', 'data': {}}
    
    refresh = RefreshToken.for_user(user)
    
    return { 
      'message': 'login success', 
      'data': {
        'token': {
          'refresh': str(refresh),
          'access': str(refresh.access_token)
        }
      }
    }