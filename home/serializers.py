from rest_framework import serializers
from .models import Associations, Notifications, Memories

class AssociationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Associations
        fields = ['id','name','image']

    name = serializers.CharField()
    image = serializers.ImageField()

class NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = ['id', 'notification']
    
class MemoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Memories
        fields = ['id', 'title', 'video', 'description']