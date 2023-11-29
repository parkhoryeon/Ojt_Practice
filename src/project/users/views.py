from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import User
from django.contrib.auth.hashers import make_password

from rest_framework.viewsets import ModelViewSet

from rest_framework.views import APIView

from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer


def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request, 
            username=username, 
            password=password
        )
        if user is not None:
            login(
                request, 
                user
            )
            return redirect('core:index')
        else:
            return HttpResponse("Invalid login")
    return render(
        request, 
        'users/login.html'
    )

def custom_logout(request):
    logout(request)
    return redirect('users:login')

# ################################################################################## 
# 마법 Final 단계
class UsersAPIViewSet(ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        validated_data = serializer.validated_data
        # 비밀번호를 해싱하여 저장
        validated_data['password'] = make_password(validated_data['password'])
        serializer.save()

# ################################################################################## 
# 마법 1단계
# class UsersAPI(APIView):

#     def get(self, request):
#         print('USERS_GET')
#         all_users = User.objects.all()
#         serializer = UserSerializer(all_users, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         print('USETS_POST')
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             new_user = serializer.save()
#             return Response(
#                 UserSerializer(new_user).data,
#             )
#         else:
#             return Response(serializer.errors) 

# ################################################################################## 
# 마법X
# @api_view([ "GET", "POST" ])
# def users(request):
#     if request.method == "GET":
#         all_users = User.objects.all()
#         serializer = UserSerializer(all_users, many=True)
#         return Response(serializer.data,)
#     elif request.method == "POST":
#         print(request.data)
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             new_user = serializer.save()
#             return Response(
#                 UserSerializer(new_user).data
#             )
#         else:
#             return Response(serializer.errors)

# ################################################################################## 
# 마법 1단계
# class UserAPI(APIView):

#     def get_object(self, pk):
#         print('USER_GET_OBJECT')
#         try:
#             user = User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             raise NotFound
#         return user

#     def get(self, request, pk):
#         print('USER_GET')
#         serializer = UserSerializer(self.get_object(pk))
#         print(serializer)
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         print('USER_PUT')
#         serializer = UserSerializer(
#             self.get_object(pk),
#             data=request.data,
#             partial=True,
#         )
#         if serializer.is_valid():
#             updated_user = serializer.save()
#             return Response(UserSerializer(updated_user).data)
#         else:
#             return Response(serializer.errors)

#     def delete(self, request, pk):
#         print('USER_DELETE')
#         self.get_object(pk).delete()
#         return Response(status=HTTP_204_NO_CONTENT)

# ################################################################################## 
# 마법X
# @api_view([ "GET", "PUT", "DELETE" ])
# def user(request, pk):
#     try:
#         user = User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         raise NotFound
    
#     if request.method == "GET":
#         serializer = UserSerializer(user)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer = UserSerializer(
#             user,
#             data=request.data,
#             partial=True  
#             # [ partial=True ] Serializer는 여기로 들어오는 데이터가 완벽한 형태가 아닐수도 있다는 걸 알게된다.
#             # UserSerializer는 사용자한테서 받지 못한 데이터는 현재 데이터베이스에 있는 user 정보로 유지해야 한다는것을 알고있다.
#         )
#         print('SERIALIZER.IS_VALID() : ', serializer.is_valid())
#         if serializer.is_valid():
#             update_user = serializer.save()  # serializer는 update 메서드를 실행할것이다.
#             return Response(UserSerializer(update_user).data)
#         else: 
#             return Response(serializer.errors)
#     elif request.method == "DELETE":
#         user.delete()
#         return Response(status=HTTP_204_NO_CONTENT)

# 사용자 데이터 만으로 seralizer를 만들면 create 메서드가 실행이되고
# 사용자 데이터랑 데이터베스에서 가져온 데이터로 seralizer를 만들면 update 메서드가 실행이 된다.