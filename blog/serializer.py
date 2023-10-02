from rest_framework import serializers

from user.models import User
from .models import Blog ,Images,Comment,Category,Tags


from .models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['author_profile']

class ImageSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=Images
        fields=['image']

    def get_image(self, obj):
        return [image.image.url for image in obj.image.all()]




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class CommentSerializer(serializers.ModelSerializer):
    username=serializers.PrimaryKeyRelatedField(write_only=True,queryset=User.objects.all())
    user= serializers.StringRelatedField(source='username')
    blog=serializers.PrimaryKeyRelatedField(write_only=True,queryset=Blog.objects.all())
    class Meta:
        model=Comment
        fields=[
            'username',
            'user',
            'comment',
            'blog'
        ]

class BlogSerializer(serializers.ModelSerializer):
    image=serializers.SerializerMethodField()
    # image=ImageSerializer(many=True)
    comment= CommentSerializer(many=True, read_only=True)
    category=serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(),write_only=True)
    category_name=serializers.StringRelatedField(source='category')
    author_name=serializers.StringRelatedField(source='author')
    author=serializers.PrimaryKeyRelatedField(write_only=True,queryset=User.objects.all())
    author_profile=UserSerializer(source='author',read_only=True)
    likes=serializers.SerializerMethodField()
    # tag = serializers.PrimaryKeyRelatedField(queryset=Tags.objects.all(), write_only=True)
    images=serializers.ListField(write_only=True,
        child=serializers.ImageField())
    tag=serializers.SerializerMethodField()
    tag_input = serializers.ListField(write_only=True,
        child = serializers.CharField()
    )
    def get_likes(self, obj):
        return (user.username for user in obj.likes.all())
    
    def get_tag(self, obj):
          # Assuming 'tag' is a ManyToManyField to 'Tags'
       return [tag.name for tag in obj.tag.all()]

    def get_image(self, obj):
       return [self.context['request'].build_absolute_uri(image.image.url) for image in obj.image.all()]

    class Meta:
        model=Blog
        # fields='__all__'
        fields=[
            'id',
            'title',
            'description',
            'author',
            'author_name',
            'author_profile',
            'likes',
            'category',
            'category_name',
            'tag',
            'tag_input',
            'published_date',
            'image',
            'images',
            'comment',
        ]



    def create(self, validated_data):
        tag_data = validated_data.pop('tag_input',[])
        images_data=validated_data.pop('images',[])
        obj = Blog.objects.create(**validated_data)

        for tag in tag_data:
            tag_instance,created = Tags.objects.get_or_create(name=tag)
            obj.tag.add(tag_instance) 
        
        for image in images_data:
            image_instance,created = Images.objects.get_or_create(image=image)
            obj.image.add(image_instance) 

        return obj
    


    def update(self,instance,validated_data):
        tag_data=validated_data.pop('tag_input',[])
        images_data=validated_data.pop('images',[])
        if tag_data:
            instance.tag.clear()  
            for tag in tag_data:
                tag_instance, created = Tags.objects.get_or_create(name=tag)
                instance.tag.add(tag_instance)
        
        if images_data:
            instance.image.clear()
            for image in images_data:
                image_instance, created=Images.objects.get_or_create(image=image)
                instance.image.add(image_instance)

        return super().update(instance, validated_data)
#


