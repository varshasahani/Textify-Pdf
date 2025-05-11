from django.db import models

# Create your models here.

class UploadedFile(models.Model):
    id = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')
    is_valid = models.BooleanField(default=False)
    invalid_reason = models.TextField(null=True, blank=True)
    is_processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"UploadedFile: {self.file_name} (Valid: {self.is_valid})"

    def get_receipts(self):
        """Retrieve all receipts associated with this uploaded file."""
        return self.receipts.all()


class ExtractedReceipt(models.Model):
    id = models.AutoField(primary_key=True)
    uploaded_file = models.ForeignKey(UploadedFile, on_delete=models.CASCADE, related_name="receipts")
    purchased_at = models.DateTimeField(null=True, blank=True)
    merchant_name = models.CharField(max_length=255, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    file_path = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Receipt: {self.merchant_name} on {self.purchased_at} (File: {self.uploaded_file.file_name})"

    def get_details(self):
        """Return a dictionary of receipt details."""
        return {
            "Merchant Name": self.merchant_name,
            "Date": self.purchased_at,
            "Total Amount": self.total_amount,
            "File Path": self.file_path,
        }