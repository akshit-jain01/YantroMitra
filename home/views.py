from django.shortcuts import render
from .models import Associations, Notifications, Memories
from .serializers import AssociationsSerializer, NotificationsSerializer, MemoriesSerializer
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView

# Create your views here.

class AssociationView(APIView):
    def get(self, request):
        try:
            associations = Associations.objects.all()
            serializer = AssociationsSerializer(associations, many = True)
            return Response(serializer.data)
        except:
            return Response({
                'data':serializer.errors,
                'message':'something went wrong'
            }, status=status.HTTP_400_BAD_REQUEST)

    
class NotificationView(APIView):
    def get(self, request):
        try:
            notifications = Notifications.objects.all()
            serializer = NotificationsSerializer(notifications, many = True)
            return Response(serializer.data)
        except:
            return Response({
                'data':serializer.errors,
                'message':'something went wrong'
            }, status=status.HTTP_400_BAD_REQUEST)
        
class MemoriesView(APIView):
    def get(self,request):
        try:
            memories = Memories.objects.all()
            serializer = MemoriesSerializer(memories, many=True)
            return Response(serializer.data)
        except:
            return Response({
                'data':serializer.errors,
                'message':'something went wrong'
            }, status=status.HTTP_400_BAD_REQUEST)

