from rest_framework import generics, viewsets
from rest_framework.filters import SearchFilter
from .serializer import UserSerializer
from .models import Blog, Comment ,Images,Category,Likes
from user.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
# Create your views here.
from .serializer import BlogSerializer,CommentSerializer,CategorySerializer,ImageSerializer,LikeSerializer
# from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

# users=User.objects.all()
# for user in users:
#      token=Token.objects.get_or_create(user=user)
#      print(token)

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
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
    @action(detail=True, methods=['GET'])
    def likes_count(self, request, pk=None):
        
            blog = self.get_object()
            like_count = blog.likes.count() 
            return Response({"like_count": like_count})
    

class CommentListCreateAPIView(generics.ListCreateAPIView):
    authentication_classes=[TokenAuthentication]
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class ImagesListCreateAPIView(generics.ListCreateAPIView):
    queryset=Images.objects.all()
    serializer_class=ImageSerializer

class LikesListCreateAPIView(generics.ListCreateAPIView):
    queryset=Likes.objects.all()
    serializer_class=LikeSerializer


class BlogDetailsAPIView(generics.RetrieveAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer


