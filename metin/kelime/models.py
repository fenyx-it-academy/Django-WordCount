from django.db import models
from datetime import datetime


# Create your models here.
class Kelime(models.Model):
    
    metin_text=models.TextField()
    
   