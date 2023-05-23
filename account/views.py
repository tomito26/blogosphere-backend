from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import  RegisterSerializer,LoginSerializer
from rest_framework import status
from django.contrib.auth.models import User

class RegisterView(APIView):
  
  def post(self, request):

    try:
      data = request.data
      # print(data)
      serializer = RegisterSerializer(data = data)

      if not serializer.is_valid():
        return Response({
          'data': serializer.errors,
          'message': 'something went wrong'
        }, status = status.HTTP_400_BAD_REQUEST)
 
      
      serializer.save()

      return Response({
        'data': {},
        'message': 'your account is created' 
      }, status = status.HTTP_201_CREATED)
    
    except Exception as e:
      print(e)
      return Response({
        'data': {},
        'message': 'something went wrong'
      }, status = status.HTTP_400_BAD_REQUEST)
  

class LoginView(APIView):

  def post(self, request):

    try: 

      data = request.data
      
      serializer = LoginSerializer(data = data)
      
      if not serializer.is_valid():
        return Response({
          'data': serializer.errors,
          'message': 'Account not found'
        }, status = status.HTTP_400_BAD_REQUEST)
      
      response = serializer.get_jwt_token(serializer.data)

      return Response(response, status = status.HTTP_200_OK)
    
    except Exception as e:
      print(e)
      return Response({
        'data': {},
        'message': 'Invalid credentials'
      }, status = status.HTTP_400_BAD_REQUEST)


class UsersView(APIView):
  def get(self, request): 
    try:
      users = User.objects.all()

      serializer = RegisterSerializer(users, many=True)
      
      return Response({
        'data': serializer.data,
        'message': 'profiles fetched successful'
      }, status= status.HTTP_201_CREATED)
    
    except Exception as e:
      print(e)
      return Response({
        'data': {},
        'message': 'something went wrong'
      }, status = status.HTTP_400_BAD_REQUEST)



class UserDetailView(APIView):
  def get(self, request,pk): 
    try:
      user = User.objects.get(pk=pk)

      serializer = RegisterSerializer(user)
      
      return Response({
        'data': serializer.data,
        'message': 'profiles fetched successful'
      }, status= status.HTTP_201_CREATED)
    
    except Exception as e:
      print(e)
      return Response({
        'data': {},
        'message': 'something went wrong'
      }, status = status.HTTP_400_BAD_REQUEST)