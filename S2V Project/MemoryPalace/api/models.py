from django.db import models

# Create your models here.

class Palace(models.Model):
    user = models.CharField(max_length=50,unique=True)
    version = models.IntegerField(null = False, default = 1)
    second_letter_weight = models.DecimalField (default = 0.1,decimal_places=2,max_digits = 3,null = False)
    phonetic_weight = models.DecimalField (default = 0.2,decimal_places=2,max_digits = 3,null = False)
    theme = models.CharField(max_length=50, null = False)
    words_to_remember = models.CharField(max_length=5000, null = False)
    trigger_words = models.CharField(max_length=5000, null = True)
    created_at = models.DateTimeField(auto_now_add = True)
