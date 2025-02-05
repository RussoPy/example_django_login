from django.urls import path
from .views import register,test
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt import views as jwt_views
from base import views



urlpatterns = [
    path('tasks/<int:pk>/', views.task_detail, name='task-detail'),
    path('register/', register ),
    path('test',test),
    path('login', TokenObtainPairView.as_view()),   
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('all-tasks', views.get_all_tasks, name='all-tasks'),

]
