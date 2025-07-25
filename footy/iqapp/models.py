from django.db import models
class beginner(models.Model):
  name = models.CharField(max_length=255)
  content = models.TextField()
  image = models.ImageField(upload_to='post_images/',blank=True,null=True)
  
class intermediate(models.Model):
  name = models.CharField(max_length=255)
  content = models.TextField()
  image = models.ImageField(upload_to='post_images/',blank=True,null=True)
  
class pro(models.Model):
  name = models.CharField(max_length=255)
  content = models.TextField()
  image = models.ImageField(upload_to='post_images/',blank=True,null=True)