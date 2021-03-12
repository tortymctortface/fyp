from rest_framework import serializers
from .models import Palace

class PalaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palace
        fields = ('id', 'user', 'version', 'previous_word_weight','first_letter_weight','second_letter_weight', 'phonetic_weight','theme','created_at','words_to_remember', 'trigger_words')

class CreatePalaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palace
        fields = ('version','first_letter_weight','second_letter_weight','phonetic_weight', 'previous_word_weight','theme','words_to_remember')