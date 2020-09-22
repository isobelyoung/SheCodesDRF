from rest_framework import serializers 
from .models import CustomUser

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    # django handles all primary keys, never need to update otherwise db error
    username = serializers.CharField(max_length = 200)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField(max_length = 200)
    password = serializers.CharField(write_only = True)
    profile_picture = serializers.URLField(max_length = 200)
    business_name = serializers.CharField(max_length = 200)

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

class CustomUserDetailSerializer(CustomUserSerializer):

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)
        instance.business_name = validated_data.get('business_name', instance.business_name)
        instance.save()
        return instance