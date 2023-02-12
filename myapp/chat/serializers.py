from rest_framework import serializers
from .models import Messages
from user.models import BaseUser


class MessageSerializer(serializers.ModelSerializer):

    sender_name = serializers.SlugRelatedField(many=False, slug_field='username', queryset=BaseUser.objects.all())
    receiver_name = serializers.SlugRelatedField(many=False, slug_field='username', queryset=BaseUser.objects.all())

    class Meta:
        model = Messages
        fields = ['sender_name', 'receiver_name', 'description', 'time']

