from django.db import models
from django.contrib.auth.models import User
import uuid


class BaseModel(models.Model):
  uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now_add=True)

  class Meta:
    abstract = True

class Profile(BaseModel):
  user_profile = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
  bio = models.TextField(blank=True, null=True)
  profile_image = models.FileField(blank=True, null=True, upload_to='profile-image')

  def __str__(self) -> str:
    return self.user.username


class Blog(BaseModel):
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs")
  title = models.CharField(max_length=500)
  main_image = models.FileField(upload_to='blog-post-image')
  blog_text = models.TextField()
  tag = models.CharField(max_length=500)
  duration_reading = models.CharField(max_length=500)


  def __str__(self) -> str:
    return self.title