from django.contrib.auth.models import Group
from rest_framework import serializers
from djoser.conf import settings


class MyTokenSerializer(serializers.ModelSerializer):
    auth_token = serializers.CharField(source="key")
    user_group = serializers.SerializerMethodField('get_group')

    def get_group(self, obj):
        return obj.user.groups.values_list('name', flat=True).first()

    class Meta:
        model = settings.TOKEN_MODEL
        fields = ("auth_token", "user_group")