import os
from django.core.exceptions import ValidationError

ALLOWED_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.pdf'}
MAX_FILE_SIZE =5 * 1024 * 1024

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise ValidationError("unsupported file extension, allowd is .jpg, .png, .jpeg, .pdf")

def validate_file_size(value):
    if value.size > MAX_FILE_SIZE:
        raise ValidationError(f'file too large. Size must be <= {MAX_FILE_SIZE //(1024 *1024)}MB')
        