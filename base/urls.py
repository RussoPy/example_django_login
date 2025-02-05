from django.urls import path
from .views import tasks,register,test
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('tasks/', tasks ),
    path('tasks/<int:id>',tasks),
    path('register/', register ),
    path('test',test),
    path('login', TokenObtainPairView.as_view()),    
 

]
