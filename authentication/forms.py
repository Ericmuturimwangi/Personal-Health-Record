from django import forms
from users.models import HealthEntry
import bleach

ALLOWED_TAGS = []
ALLOWED_ATTRIBUTES = {}

class HealthEntry(forms.ModelForm):
    class Meta:
        model = HealthEntry
        fields = ['date', 'symptoms', 'medications', 'mood', 'notes', 'attachment']

    def clean_mood(self):
        mood = self.cleaned_data.get("mood", "")
        if len (mood) >50:
            raise forms.ValidationError("Mood too long")
        return mood
        

        