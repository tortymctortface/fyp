from rest_framework import serializers
from .models import Palace

class PalaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palace
        fields = ('id', 'user', 'version', 'second_letter_weight', 'phonetic_weight','theme','created_at')

class CreatePalaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palace
        fields = ('version','second_letter_weight','phonetic_weight','theme')