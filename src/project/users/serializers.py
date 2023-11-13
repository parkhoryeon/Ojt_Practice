from rest_framework import serializers
from .models import User


class UserSerializer(serializers.Serializer):

    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20)

    def create(self, validated_data):
        print('VALIDATED_DATA : ', validated_data)
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance