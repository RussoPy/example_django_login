from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import TaskSerializer,RegisterSerializer
from .models import Task
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status



# login
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom columns


        token['username'] = user.username
        # ...
        return token




class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



@api_view(['POST'])
def register(req):
    serializer = RegisterSerializer(data=req.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','POST','DELETE','PUT','PATCH'])
def tasks(req,id=-1):
    if req.method =='GET':
        if id > -1:
            try:
                temp_task=Task.objects.get(id=id)
                return Response (TaskSerializer(temp_task,many=False).data)
            except Task.DoesNotExist:
                return Response ("not found")
        all_tasks=TaskSerializer(Task.objects.all(),many=True).data
        return Response ( all_tasks)
    if req.method =='POST':
        tsk_serializer = TaskSerializer(data=req.data)
        if tsk_serializer.is_valid():
            tsk_serializer.save()
            return Response ("post...")
        else:
            return Response (tsk_serializer.errors)
    if req.method =='DELETE':
        try:
            temp_task=Task.objects.get(id=id)
        except Task.DoesNotExist:
            return Response ("not found")    
       
        temp_task.delete()
        return Response ("del...")
    if req.method =='PUT':
        try:
            temp_task=Task.objects.get(id=id)
        except Task.DoesNotExist:
            return Response ("not found")
       
        ser = TaskSerializer(data=req.data)
        old_task = Task.objects.get(id=id)
        res = ser.update(old_task, req.data)
        return Response("‘upd’")



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def test(req):
    user = req.user
    temp_prod = user.task_set.all()
    return Response(TaskSerializer(temp_prod, many=True).data)