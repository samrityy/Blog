from django.urls import path
from rest_framework import routers
from .import views
from .views import BlogViewSet 
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

# urlpatterns=[
#     # path('',views.BlogListCreateAPIView.as_view(),name='blog-list-create'),
#     path('<int:pk>/',views.BlogDetailsAPIView.as_view()),
#     path('comment/',views.CommentListCreateAPIView.as_view(),name='comment-list-create'),
#     path('images/',views.ImagesListCreateAPIView.as_view(),name='image-list-create'),
#     path('category/',views.CategoryListCreateAPIView.as_view(),name='category-list-create'),
#     path('like/',views.LikesListCreateAPIView.as_view(),name='like-list-create'),
# ]





urlpatterns = [
    path('<int:pk>/',views.BlogDetailsAPIView.as_view()),
    path('comment/',views.CommentListCreateAPIView.as_view(),name='comment-list-create'),
    path('images/',views.ImagesListCreateAPIView.as_view(),name='image-list-create'),
    path('category/',views.CategoryListCreateAPIView.as_view(),name='category-list-create'),
    path('likes/',views.LikesListCreateAPIView.as_view(),name='like-list-create'),
    path('blogs/<int:pk>/likes/', views.BlogViewSet.as_view({'get': 'likes_count'}), name='likes-count'),
    path('auth/login/', obtain_auth_token, name='create-token'),
]




router = routers.DefaultRouter()
router.register(r'',  BlogViewSet)
urlpatterns += [
    path('', include(router.urls)),
]