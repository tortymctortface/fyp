from django.db import models

# Create your models here.

class Palace(models.Model):
    user = models.CharField(max_length=50,unique=True)
    version = models.IntegerField(null = False, default = 1)
    second_letter_weight = models.DecimalField (default = 0.1,decimal_places=2,max_digits = 3,null = False)
    phonetic_weight = models.DecimalField (default = 0.2,decimal_places=2,max_digits = 3,null = False)
    theme = models.CharField(max_length=50, null = False)
    created_at = models.DateTimeField(auto_now_add = True)
