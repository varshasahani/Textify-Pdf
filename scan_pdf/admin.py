from django.contrib import admin
from .models import UploadedFile, ExtractedReceipt

# Register your models here.
admin.site.register(UploadedFile)
admin.site.register(ExtractedReceipt)
