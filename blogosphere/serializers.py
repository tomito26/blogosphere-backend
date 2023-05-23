from rest_framework import serializers
from .models import Blog,Profile

class BlogSerializer(serializers.ModelSerializer):
  class Meta:
    model = Blog
    fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    exclude = ['created_at', 'updated_at']

