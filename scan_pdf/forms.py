from django import forms
from .models import UploadedFile
from django.core.exceptions import ValidationError

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file_name', 'file']

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if not file.name.endswith('.pdf'):
            raise ValidationError("Only PDF files are allowed.")
        if file.content_type != 'application/pdf':
            raise ValidationError("The uploaded file is not a valid PDF.")
        return file