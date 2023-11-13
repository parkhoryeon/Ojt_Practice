from rest_framework import serializers
from .models import User


# ################################################################################## 
# Model 기반으로 자동으로 생성
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "__all__" # 해당 모델의 모든 field를 보여주겠다고 하는 것.
            # "pk",
            # "name",
        )
        # 특정 필드 제외
        # exclude = (
        #     "email",
        # )

# ################################################################################## 
# 직접 serializer 생성
# class UserSerializer(serializers.Serializer):

#     pk = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=20)

#     def create(self, validated_data):
#         print('VALIDATED_DATA : ', validated_data)
#         return User.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name", instance.name)
#         instance.save()
#         return instance