from rest_framework import generics
from rest_framework.filters import SearchFilter
from .serializer import UserSerializer
from .models import Blog, Comment ,Images,Category
from user.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
# Create your views here.
from .serializer import BlogSerializer,CommentSerializer,CategorySerializer,ImageSerializer
# from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import action

class BlogListCreateAPIView(generics.ListCreateAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    # parser_classes = (MultiPartParser, FormParser)
    filter_backends=[DjangoFilterBackend]
    # search_fields=['title','category']
    filterset_fields=['category__category']

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     return Response(serializer.data)

    # @action(detail=True, methods=['GET'])
    # def like_count(self, request, pk=None):
        
    #         post = self.get_object()
    #         like_count = post.likes.count()  # Assuming you have a related_name "likes" for your Like model
    #         return Response({"like_count": like_count})



class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class ImagesListCreateAPIView(generics.ListCreateAPIView):
    queryset=Images.objects.all()
    serializer_class=ImageSerializer

class BlogDetailsAPIView(generics.RetrieveAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer


class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
