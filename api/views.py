from django.shortcuts import render
from rest_framework import viewsets
from .models import Audio
from .serializers import AudioSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# Create your views here.


class AudioView(viewsets.ModelViewSet):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})