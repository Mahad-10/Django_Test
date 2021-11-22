from django.urls import path, include
from test_app import views

urlpatterns = [
    path('api/login/', views.LoginAPIView.as_view()),
    path('api/profile/', views.ProfileAPIView.as_view()),
    path('api/register/', views.RegisterAPIView.as_view(),),

]
