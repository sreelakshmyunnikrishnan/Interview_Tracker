from django import forms
from django.db.models import fields

from django.forms.widgets import DateInput, TextInput, Textarea
from intrack.models import AddInt
from intrack.models import Notes

class DateInput(forms.DateInput):
    input_type = 'date'

DEMO_CHOICES =(
    ("Selected","Selected"),
    ("Selected for Next Round","Selected for Next Round"),
    ("Rejected", "Rejected"),
    ("No Update", "No Update"),
)
REC = (
    ("Yes", "Yes"),
    ("No", "No"),
    
)
    
class EntryForm(forms.ModelForm):

    class Meta:
        model=AddInt
        fields='__all__'
        widgets = {
            'user': forms.Select(attrs={'class':'form-control',}),
            'c_name': forms.TextInput(attrs={'class':'form-control',}),
            'c_post': forms.TextInput(attrs={'class':'form-control',}),
            'c_url': forms.URLInput(attrs={'class':'form-control',}),
            'c_contact': forms.NumberInput(attrs={'class':'form-control',}),
            'c_email': forms.EmailInput(attrs={'class':'form-control',}),
            'post_applied': forms.TextInput(attrs={'class':'form-control',}),
            'que_asked': forms.Textarea(attrs={'class':'form-control',}),
            'rec_called': forms.Select(attrs={'placeholder':'Select','placeholder':'Select the User'}),
            'resp_status': forms.Select(attrs={'placeholder':'Select','placeholder':'Select the User'}),
            'self_analysis': forms.Textarea(attrs={'class':'form-control',}),
            'date_applied': DateInput(attrs={'class':'form-control',}),
            'scd_date':DateInput(attrs={'class':'form-control',}),
            }


class NoteForm(forms.ModelForm):
    class Meta:
        model=Notes
        fields='__all__'
        widgets = {
            'user': forms.Select(attrs={'class':'form-control','placeholder':'Select the User'}),
            'note_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}),
            'note_content': forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Notes....'}),
            }