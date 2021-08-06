from .models import API_GIT
from django.forms import ModelForm

class ApigitForm(ModelForm):
    class Meta:
        model = API_GIT
        fields = ['login']
