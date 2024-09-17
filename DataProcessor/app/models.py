# models.py
from django.db import models

class FileMetadata(models.Model):  
    file_key = models.CharField(max_length=255, unique=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.file_key

class WellData(models.Model):
    api_well_number = models.CharField(max_length=20)  
    oil = models.IntegerField()
    gas = models.IntegerField()
    brine = models.IntegerField()

    def __str__(self):
        return self.api_well_number
