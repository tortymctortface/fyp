from django.shortcuts import render
from rest_framework import generics, status
from .serializers import PalaceSerializer, CreatePalaceSerializer
from .models import Palace
from rest_framework.views import APIView
from rest_framework.response import Response


class PalaceView(generics.CreateAPIView):
    queryset = Palace.objects.all()
    serializer_class = PalaceSerializer

class CreatePalaceView(APIView):
    serializer_class = CreatePalaceSerializer
    def post(self,request,format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            phonetic_weight = serializer.data.get('phonetic_weight')
            second_letter_weight = serializer.data.get('second_letter_weight')
            version = serializer.data.get('version')
            theme = serializer.data.get('theme')
            user = self.request.session.session_key
            queryset = Palace.objects.filter(user=user)
            if queryset.exists():
                palace = queryset[0]
                palace.phonetic_weight = phonetic_weight
                palace.second_letter_weight = second_letter_weight
                palace.version = version
                palace.theme = theme
                palace.save(update_fields=['phonetic_weight','second_letter_weight','version','theme'])
                return Response(PalaceSerializer(palace).data, status = status.HTTP_200_OK)
            else:
                palace=Palace(user=user,phonetic_weight= phonetic_weight,second_letter_weight = second_letter_weight, version=version,theme = theme)
                palace.save()
                return Response(PalaceSerializer(palace).data, status = status.HTTP_201_CREATED)
        return Response({'Bad Request': 'Invalid Data...'}, status = status.HTTP_400_BAD_REQUEST)
