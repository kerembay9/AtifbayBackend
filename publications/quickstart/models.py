from django.db import models

class Publication(models.Model):
    reference= models.CharField(max_length=511,blank=True, null=True, verbose_name="Title")
    link= models.URLField(max_length=511,blank=True, null=True)
    explanation= models.CharField(max_length=5095,blank=True)
    adddate= models.DateField(auto_now_add=True)
    total_views=models.IntegerField(default=0)






