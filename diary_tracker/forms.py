from django.forms import ModelForm
from diary_tracker.models import DiaryRecord

class DiaryRecordForm(ModelForm):
    class Meta:
        model = DiaryRecord
        fields = ["description"]