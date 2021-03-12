from django.db import models

# Create your models here.

class Palace(models.Model):
    user = models.CharField(max_length=50,unique=True)
    version = models.IntegerField(null = False)
    second_letter_weight = models.DecimalField (default = 0,decimal_places=2,max_digits = 3,null = True)
    phonetic_weight = models.DecimalField (default = 0,decimal_places=2,max_digits = 3,null =True)
    theme = models.CharField(max_length=50, null = True)
    previous_word_weight = models.DecimalField (default = 0,decimal_places=2,max_digits = 3,null = True)
    first_letter_weight = models.DecimalField (default = 0,decimal_places=2,max_digits = 3,null = True)
    words_to_remember = models.CharField(max_length=50000, null = False)
    trigger_words = models.CharField(max_length=50000, null = True)
    created_at = models.DateTimeField(auto_now_add = True)
