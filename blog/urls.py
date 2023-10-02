from django.urls import path

from .import views

urlpatterns=[
    path('',views.BlogListCreateAPIView.as_view(),name='blog-list-create'),
    path('<int:pk>/',views.BlogDetailsAPIView.as_view()),
    path('comment/',views.CommentListCreateAPIView.as_view(),name='comment-list-create'),
    path('images/',views.ImagesListCreateAPIView.as_view(),name='image-list-create'),
    path('category/',views.CategoryListCreateAPIView.as_view(),name='category-list-create'),
    path('user/',views.UserListCreateAPIView.as_view(),name='user-list-create'),
]