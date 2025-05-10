from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import UploadedFile, ExtractedReceipt
from .ocr_utils import extract_text_from_pdf, parse_receipt_data
from datetime import datetime

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save()
            # Extract text from the uploaded file
            file_path = uploaded_file.file.path
            extracted_text = extract_text_from_pdf(file_path)
            # Parse the extracted text
            parsed_data = parse_receipt_data(extracted_text)

            # Validate the extracted data
            missing_fields = []
            if not parsed_data["merchant_name"]:
                missing_fields.append("Merchant Name")
            if not parsed_data["purchased_at"]:
                missing_fields.append("Date")
            if not parsed_data["total_amount"]:
                missing_fields.append("Total Amount")

            if missing_fields:
                # Mark the file as invalid and set the invalid_reason
                uploaded_file.is_valid = False
                uploaded_file.invalid_reason = f"Missing fields: {', '.join(missing_fields)}"
                uploaded_file.save()
            else:
                # Save the extracted data to the database
                ExtractedReceipt.objects.create(
                    purchased_at=datetime.strptime(parsed_data["purchased_at"], "%Y-%m-%d") if parsed_data["purchased_at"] else None,
                    merchant_name=parsed_data["merchant_name"],
                    total_amount=parsed_data["total_amount"],
                    file_path=file_path,
                )
                # Mark the file as valid
                uploaded_file.is_valid = True
                uploaded_file.save()

            return redirect('success')  # Redirect to a success page
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def success(request):
    return render(request, 'success.html')

def receipt_list(request):
    # Fetch all receipts from the database
    receipts = ExtractedReceipt.objects.all()
    return render(request, 'receipt_list.html', {'receipts': receipts})

