from django.forms import ModelForm
from study_bee.models import TransactionRecord

class TransactionRecordForm(ModelForm):
    class Meta:
        model = TransactionRecord
        fields = ["name", "type", "amount", "description"]
