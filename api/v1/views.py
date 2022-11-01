from rest_framework import status

from api.base.api_view import CustomBaseApiView, CustomBaseApiViewNotAuthen
from drf_spectacular.utils import extend_schema

from api.base.jwt_config import generate_jwt_token
from api.base.serializer import ExceptionResponseSerializer
from api.models import UserInfo
from api.v1.serializers import LoginSerializerRequest, LoginSerializerResponse, UserInfoSerializerResponse, \
    RegisterSerializerRequest
import cryptocode

class UserViewForLogin(CustomBaseApiViewNotAuthen):
    @extend_schema(
        operation_id='user-login',
        summary='Login',
        tags=["User"],
        description='Login',
        request=LoginSerializerRequest,
        responses={
            status.HTTP_200_OK: LoginSerializerResponse,
            status.HTTP_401_UNAUTHORIZED: ExceptionResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
        }
    )
    def user_login(self, request):
        serializer = LoginSerializerRequest(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = UserInfo.objects.get(user_name=username)

        if user and password == cryptocode.decrypt(user.password, "123121đgsdfgsdryqư35"):
            response_data = {
                "token": generate_jwt_token(username)
            }
            return self.response_success(LoginSerializerResponse(response_data).data)
        self.http_exception(description="login fall")

    @extend_schema(
        operation_id='user-register',
        summary='Register',
        tags=["User"],
        description='Register',
        request=RegisterSerializerRequest,
        responses={
            status.HTTP_200_OK: None,
            status.HTTP_401_UNAUTHORIZED: ExceptionResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
        }
    )
    def user_register(self, request):
        serializer = RegisterSerializerRequest(data=request.data)
        serializer.is_valid(raise_exception=True)
        full_name = serializer.validated_data['full_name']
        username = serializer.validated_data['username']
        password = cryptocode.encrypt(serializer.validated_data['password'], "123121đgsdfgsdryqư35")
        UserInfo.objects.create(full_name=full_name, user_name=username, password=password)
        self.http_exception(description="register success")


class UserView(CustomBaseApiView):
    @extend_schema(
        operation_id='get-user-info',
        summary='get info',
        tags=["User"],
        description='get user info',
        responses={
            status.HTTP_200_OK: UserInfoSerializerResponse,
            status.HTTP_401_UNAUTHORIZED: ExceptionResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
        }
    )
    def get_user_info(self, request):
        username = self.username
        user_info = UserInfo.objects.get(user_name=username)
        return self.response_success(data=UserInfoSerializerResponse({
            "id": user_info.id,
            "username": user_info.user_name,
            "full_name": user_info.full_name
        }).data)
