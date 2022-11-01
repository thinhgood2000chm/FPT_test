import json

from django.core.serializers.json import DjangoJSONEncoder
from rest_framework import serializers, status

from api.base.exception import CustomAPIException
from api.base.jwt_config import TokenAuthentication
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.base.serializer import InheritedSerializer


class CustomBaseApiViewNotAuthen(GenericViewSet):
    permission_classes = ()
    parser_classes = (JSONParser,)
    serializer_class = InheritedSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.username = None

    def _response(self, data, status_code=status.HTTP_200_OK):
        return Response(
            data=json.loads(json.dumps(data, cls=DjangoJSONEncoder)),
            status=status_code,
        )

    def response_success(self, data, status_code=status.HTTP_200_OK):
        return self._response(data, status_code)

    def http_exception(self, error_code=None, description=None, status_code=status.HTTP_400_BAD_REQUEST):
        raise CustomAPIException(status_code=status_code, detail={
            'error_code': error_code,
            'description': description
        })


class CustomBaseApiView(CustomBaseApiViewNotAuthen):
    authentication_classes = (TokenAuthentication,)

    def initial(self, request, *args, **kwargs):
        # initial TRONG APIVIEW SẼ CHẠY TRƯỚC KHI CÁC PHƯƠNG THỨC ĐƯỢC GỌI
        super().initial(request, *args, **kwargs)
        # GẮN ATTRIBUTE USERNAME SAU KHI CHECK AUTHEN XONG ĐỂ LẤY THÔNG TIN USERNAME
        self.username = request.username
