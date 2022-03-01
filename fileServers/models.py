from django.db import models
import os
from django.conf import settings


class GeneralFile(models.Model):

    def file_upload_location(self, filename):

        filetypes = {
            "mp4": "videos",
            "mp3": "audio",
            "pdf": "docs",
            "txt": "docs",
            "docx": "docs"
        }
        extension = filename.split(".")[1]
        folder_name = filetypes.get(extension, "other")
        return f"{folder_name}/{filename}"
    
    file_name=models.CharField(max_length=100)
    file_type = models.CharField(max_length=10)
    general_file = models.FileField(upload_to=file_upload_location)