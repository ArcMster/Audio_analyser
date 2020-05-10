from django.db import models

# Create your models here.



class Input_audios(models.Model):
    audio_1 = models.FileField(upload_to='media')
    audio_2 = models.FileField(upload_to='media')
    audio_3 = models.FileField(upload_to='media')
    audio_analyse = models.FileField(upload_to='media')

class Output_audios(models.Model):
    search_1 = models.FileField(upload_to='media')
    search_2 = models.FileField(upload_to='media')
    search_3 = models.FileField(upload_to='media')
    search_4 = models.FileField(upload_to='media')
    search_5 = models.FileField(upload_to='media')
    search_6 = models.FileField(upload_to='media')

class Response(models.Model):
    file = models.FileField(upload_to='media')
    aud1_response = models.TextField(max_length=20)
    aud2_response = models.TextField(max_length=20)
    aud3_response = models.TextField(max_length=20)
    aud4_response = models.TextField(max_length=20)
    aud5_response = models.TextField(max_length=20)
    aud6_response = models.TextField(max_length=20)

