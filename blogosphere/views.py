from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import  BlogSerializer, UserProfileSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Blog,Profile
from django.db.models import Q




class ProfileView(APIView):
  permission_classes= [IsAuthenticated]
  authentication_classes=[JWTAuthentication]

  def post(self, request):
    try:
      data = request.data
      print(data)
      data['user_profile'] = request.user.id
          
      serializer = UserProfileSerializer(data= data)
      

      if not serializer.is_valid():
        return Response({
          'data' : serializer.errors,
          'message': 'Something went wrong'
        }, status = status.HTTP_400_BAD_REQUEST)
      
      serializer.save()

      return Response({
        'data': serializer.data,
        'message': 'profile created successfully'
      })
    except Exception as e:
      print(e)
      return Response({
        'data': {},
        'message': 'something went wrong'
      }, status = status.HTTP_400_BAD_REQUEST)
  
  def patch(self, request):
    try:
      data = request.data
      profile = Profile.objects.filter(uid = data.get('uid'))
      
      if not profile.exists():
        return Response({
          'data': {},
          'message': 'invalid profile id'
        })

      if request.user != profile[0].user_profile:
        return Response({
          'data':{},
          'message': 'You are not authorized to do this'
        }, status= status.HTTP_400_BAD_REQUEST)
      

      serializer = UserProfileSerializer(profile[0], data= data, partial = True)

      if not serializer.is_valid():
          return Response({
            'data' : serializer.errors,
            'message': 'Something went wrong'
          }, status = status.HTTP_400_BAD_REQUEST)
        
      serializer.save()

      return Response({
        'data': serializer.data,
        'message': 'profile updated successfully'
      })
    
    except Exception as e:
      print(e)
      return Response({
        'data': {},
        'message': 'something went wrong'
      }, status = status.HTTP_400_BAD_REQUEST)



class AllBlogsView(APIView):

  def get(self, request):
    try:
      blogs = Blog.objects.all().order_by('?')

      if request.GET.get('search'): 
        search = request.GET.get('search')
        blogs = blogs.filter(Q(title__icontains = search) | Q(blog_text__icontains = search))

      serializer = BlogSerializer(blogs, many = True)

      return Response({
        'data': serializer.data,
        'message': 'blog fetched successful'
      }, status= status.HTTP_201_CREATED)
  
    except Exception as e:
      print(e)
      return Response({
        'data': {},
        'message': 'something went wrong'
      }, status = status.HTTP_400_BAD_REQUEST)

class BlogDetailView(APIView):

  def get(self, request, pk):
    try:
      blog = Blog.objects.get(uid=pk)

      serializer = BlogSerializer(blog)

      return Response({
        'data': serializer.data,
        'message': 'blog fetched successful'
      }, status= status.HTTP_201_CREATED)
  
    except Exception as e:
      print(e)
      return Response({
        'data': {},
        'message': 'something went wrong'
      }, status = status.HTTP_400_BAD_REQUEST)


class BlogView(APIView):
  permission_classes= [IsAuthenticated]
  authentication_classes=[JWTAuthentication]

  def get(self, request):
    try:
      blogs = Blog.objects.filter(user = request.user)

      if request.GET.get('search'): 
        search = request.GET.get('search')
        blogs = blogs.filter(Q(title__icontains = search) | Q(blog_text__icontains = search))

      serializer = BlogSerializer(blogs, many = True)

      return Response({
        'data': serializer.data,
        'message': 'blog fetched successful'
      }, status= status.HTTP_201_CREATED)
    
    except Exception as e:
      print(e)
      return Response({
        'data': {},
        'message': 'something went wrong'
      }, status = status.HTTP_400_BAD_REQUEST)

  def post(self, request):
    try:
      data = request.data
      data['author'] = request.user.id
          
      serializer = BlogSerializer(data= data)
      
      if not serializer.is_valid():
        return Response({
          'data' : serializer.errors,
          'message': 'Something went wrong'
        }, status = status.HTTP_400_BAD_REQUEST)
      
      serializer.save()

      return Response({
        'data': serializer.data,
        'message': 'blog created successfully'
      })
    except Exception as e:
      print(e)
      return Response({
        'data': {},
        'message': 'something went wrong'
      }, status = status.HTTP_400_BAD_REQUEST)

  def patch(self, request):
    try:
      data = request.data
      blog = Blog.objects.filter(uid = data.get('uid'))
      
      if not blog.exists():
        return Response({
          'data': {},
          'message': 'invalid blog uid'
        })

      if request.user != blog[0].author:
        return Response({
          'data':{},
          'message': 'You are not authorized to do this'
        }, status= status.HTTP_400_BAD_REQUEST)
      

      serializer = BlogSerializer(blog[0], data= data, partial = True)

      if not serializer.is_valid():
          return Response({
            'data' : serializer.errors,
            'message': 'Something went wrong'
          }, status = status.HTTP_400_BAD_REQUEST)
        
      serializer.save()

      return Response({
        'data': serializer.data,
        'message': 'blog updated successfully'
      })
    
    except Exception as e:
      print(e)
      return Response({
        'data': {},
        'message': 'something went wrong'
      }, status = status.HTTP_400_BAD_REQUEST)
    
  def delete(self, request):
    try:
      data = request.data
      blog = Blog.objects.filter(uid = data.get('uid'))
      
      if not blog.exists():
        return Response({
          'data': {},
          'message': 'invalid blog uid'
        })

      if request.user != blog[0].author:
        return Response({
          'data':{},
          'message': 'You are not authorized to do this'
        }, status= status.HTTP_400_BAD_REQUEST)
      
      blog[0].delete()

      return Response({
        'data': {},
        'message': 'blog deleted successfully'
      }, status= status.HTTP_201_CREATED)
    

    except Exception as e:
      print(e)
      return Response({
        'data': {},
        'message': 'something went wrong'
      }, status = status.HTTP_400_BAD_REQUEST)
    
