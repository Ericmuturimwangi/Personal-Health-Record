from django import forms
from users.models import HealthEntry
import bleach

ALLOWED_TAGS = []
ALLOWED_ATTRIBUTES = {}

class HealthEntry(forms.ModelForm):
    class Meta:
        model = HealthEntry
        fields = ['date', 'symptoms', 'medications', 'mood', 'notes', 'attachment']

    def clean_notes(self):
        notes = self.cleaned_data.get('notes', '')
        cleaned = bleach.clean(notes, tags=ALLOWED_TAGS, attributes = ALLOWED_ATTRIBUTES, strip=True)
        return cleaned

        