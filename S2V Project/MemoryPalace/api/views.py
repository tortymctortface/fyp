from django.shortcuts import render
from rest_framework import generics, status
from .serializers import PalaceSerializer, CreatePalaceSerializer
from .models import Palace
from rest_framework.views import APIView
from rest_framework.response import Response
from .v03.app import create_output_list
from django.http import JsonResponse

class PalaceView(generics.CreateAPIView):
    queryset = Palace.objects.all()
    serializer_class = PalaceSerializer

class GetPalaceView(APIView):
    serializer_class = PalaceSerializer
    lookup_url_kwarg = 'user'

    def get(self, request, format = None):
        user = request.GET.get(self.lookup_url_kwarg)
        if user != None:
            palace= Palace.objects.filter(user=user)
            if len(palace) > 0:
                data = PalaceSerializer(palace[0]).data
                return Response(data, status=status.HTTP_200_OK)
            return Response({'Palace not found':'No saved palace for given user ID.'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'Bad Request': 'No User ID parameter passed'}, status = status.HTTP_400_BAD_REQUEST)    

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
            words_to_remember = serializer.data.get('words_to_remember')
            trigger_words = create_output_list(words_to_remember,theme,float(phonetic_weight),float(second_letter_weight))
            user = self.request.session.session_key
            queryset = Palace.objects.filter(user=user)
            if queryset.exists():
                palace = queryset[0]
                palace.phonetic_weight = phonetic_weight
                palace.second_letter_weight = second_letter_weight
                palace.version = version
                palace.theme = theme
                palace.trigger_words = trigger_words
                palace.words_to_remember=words_to_remember
                palace.save(update_fields=['phonetic_weight','second_letter_weight','version','theme','words_to_remember', 'trigger_words'])
                self.request.session['user'] = palace.user
                return Response(PalaceSerializer(palace).data, status = status.HTTP_200_OK)
            else:
                palace=Palace(user=user,phonetic_weight= phonetic_weight,second_letter_weight = second_letter_weight, version=version,theme = theme, words_to_remember = words_to_remember, trigger_words=trigger_words)
                palace.save()
                self.request.session['user'] = palace.user
                return Response(PalaceSerializer(palace).data, status = status.HTTP_201_CREATED)
        return Response({'Bad Request': 'Invalid Data...'}, status = status.HTTP_400_BAD_REQUEST)

class RecentPalaceView(APIView):
    def get(self,request,format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        data={
            'user':self.request.session.get('user')
        }
        return JsonResponse(data,status=status.HTTP_200_OK)