from django.db import models
from datetime import datetime, date
# Create your models here.
from django.db import models
from user.models import User

class Category(models.Model):
    category=models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.category


class Tags(models.Model):
    name=models.CharField(max_length=50,unique=True)
    def __str__(self):
        return self.name
     


class Blog(models.Model):
    title=models.CharField(max_length=30)
    description=models.TextField(max_length=50,default='default description')
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    author_profile=models.ForeignKey(User,on_delete=models.SET_NULL, null=True,related_name='user_profile')
    likes=models.ManyToManyField(User,related_name='liked_blogs')
    category=models.ForeignKey(Category,on_delete=models.SET_NULL, null=True)
    tag=models.ManyToManyField(Tags,related_name='tags')
    published_date=models.DateField(auto_now_add=False, auto_now=False, blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    

    def __str__(self):
        return self.title
    

class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE ,related_name='liked' )

class Images(models.Model):
    image=models.ImageField(upload_to="images/")
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='image',null=True)

    # def image_url(self):
    #     if self.image:
    #         return f"{settings.BASE_URL}{self.image.url}"
    # 
    
    def __str__(self):
        return str(self.image)

class Comment(models.Model):
    comment=models.CharField (max_length=100 ,null=True)
    blog=models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comment') #reverse
    username = models.ForeignKey(User, on_delete=models.CASCADE)


