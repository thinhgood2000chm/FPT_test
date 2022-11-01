from rest_framework import serializers


# dùng để kế thừa các lại serialzer.Serializer tránh báo warning
class InheritedSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    # valid dưới này nếu cần


class ExceptionResponseSerializer(InheritedSerializer):
    error_code = serializers.CharField(help_text="Unique code of this error")
    description = serializers.CharField(help_text="Detail description of this error")
