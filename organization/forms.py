from django import forms
from django.contrib.auth.models import User

from .models import Organization, Special_event

# in here which type of data output on this section of table  
# that is select by fields and add the model name on their
class OrganizationForm(forms.ModelForm):

    class Meta:
        model = Organization
        fields = ['established', 'organization_name', 'organization_type', 'organization_logo']


class Special_eventForm(forms.ModelForm):

    class Meta:
        model = Special_event
        fields = ['topic', 'date']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

