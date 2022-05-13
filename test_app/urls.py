from django.urls import path, include
from test_app import views

urlpatterns = [
    path('api/register/', views.RegisterAPIView.as_view(), name='register'),
    path('api/login/', views.LoginAPIView.as_view(), name='login'),
    path('api/profile/', views.ProfileAPIView.as_view()),
    path('api/register/', views.RegisterAPIView.as_view(),),
    path('api/image/', views.ImageUploadAPIView.as_view(),),

]
