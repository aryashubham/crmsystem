from pyexpat import model
from django import forms

from leads.models import Lead


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ('first_name', 'last_name', 'email', 'age', 'dis', 'source','agent')

# class LeadUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Lead
#         fields = ('first_name', 'last_name', 'age')

