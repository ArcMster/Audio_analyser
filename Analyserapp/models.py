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
