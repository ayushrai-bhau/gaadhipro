from django.db import models

class Teams(models.Model):
    first_name =  models.CharField(max_length=223)
    last_name =  models.CharField(max_length=223)
    designation =  models.CharField(max_length=223)
    photo =  models.ImageField(upload_to='photos/%Y/%m/%d/')
    facebook_link =  models.URLField(max_length=223)
    twitter_link =  models.URLField(max_length=223)
    google_plus_link =  models.URLField(max_length=223)
    created_date =  models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.first_name
     
