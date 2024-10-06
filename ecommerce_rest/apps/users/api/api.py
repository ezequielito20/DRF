from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import action

from apps.users.models import User
from apps.users.api.serializers import UserSerializer, UserListSerializer, UpdateUserSerializer, PasswordSerializer


class UserViewSet(viewsets.GenericViewSet):
    serializer_class = UserSerializer
    list_serializer_class = UserListSerializer
    queryset = None
    
    def get_object(self, pk):
        return get_object_or_404(self.serializer_class.Meta.model, pk=pk)
    
    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.serializer_class.Meta.model.objects.filter(is_active=True)\
                                                                    .values('id','username','email','name')
        return self.queryset
    
    @action(detail=True, methods=['POST', 'GET', 'PUT'], url_path='cambio_pass')
    def set_password(self, request, pk=None):
        user = self.get_object(pk)
        password_serializer = PasswordSerializer(data=request.data)
        if password_serializer.is_valid():
            user.set_password(password_serializer.validate(request.data)['password'])
            user.save()
            return Response({'message':'Contraseña actualizada correctamente!'}, status=status.HTTP_200_OK)
        return Response({'message':'Contraseña no actualizada!'}, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        users = self.get_queryset()
        users_serializer = self.list_serializer_class(users, many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        user_serializer = self.serializer_class(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'message':'Usuario creado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response({'message':'Usuario no creado', 'errors':user_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        user = self.get_object(pk)
        user_serializer = self.serializer_class(user)
        return Response(user_serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk=None):
        user = self.get_object(pk)
        user_serializer = UpdateUserSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'message':'Usuario actualizado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'message':'Usuario no actualizado', 'errors':user_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        user_destroy = self.serializer_class.Meta.model.objects.filter(id=pk).update(is_active=False)
        if user_destroy == 1:
            return Response({'message':'Usuario eliminado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'message':'Usuario no eliminado!'}, status=status.HTTP_404_NOT_FOUND)

# class UserAPIView(APIView):
#     def get(self, request):
#         users = User.objects.all()
#         users_serializer = UserSerializer(users, many=True)
#         return Response(users_serializer.data)    

# @api_view(['GET', 'POST'])
# def user_api_view(request):

#     # list
#     if request.method == 'GET':
#         # queryset
#         users = User.objects.all().values('id','username','email','password')
#         users_serializer = UserSerializer(users, many=True)

#         return Response(users_serializer.data, status=status.HTTP_201_CREATED)    

#     # create
#     elif request.method == 'POST':
#             user_serializer = UserSerializer(data=request.data)

#             # validation
#             if user_serializer.is_valid():
#                 user_serializer.save()
#                 return Response(user_serializer.data, status=status.HTTP_201_CREATED)
#             return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def user_detail_api_view(request, pk):
#     # queryset
#     user = User.objects.filter(id=pk).first()

#     # validation
#     if user:

#         # retrieve
#         if request.method == 'GET':
#             if pk is not None:
#                 user_serializer = UserSerializer(user)
#                 return Response(user_serializer.data, status=status.HTTP_200_OK)
        
#         # update
#         elif request.method == 'PUT':
#             user_serializer = UserSerializer(user, data=request.data)
#             if user_serializer.is_valid():
#                 user_serializer.save()
#                 return Response(user_serializer.data, status=status.HTTP_200_OK)
#             return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#         # delete
#         elif request.method == 'DELETE':
#                 user.delete()
#                 return Response({'message':'usuario eliminado correctamente!'},status=status.HTTP_200_OK)

#     return Response({'message':'Usuario no encontrado!'}, status=status.HTTP_400_BAD_REQUEST)   
