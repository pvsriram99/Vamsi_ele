from django import forms
from vamsiele.models import users
class usersdetailsform(forms.ModelForm):
    class Meta:
        model = users
        fields = '__all__'