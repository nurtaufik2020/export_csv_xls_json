from django import forms

FORMAT_CHOICES=(
    ('xls','xls'),
    ('csv','csv'),
    ('json','json'),
)
#ini bukan form yang connect ke database tapi untuk menyelect format
class FormatForm(forms.Form):
    format= forms.ChoiceField(choices=FORMAT_CHOICES, widget=forms.Select(attrs={'class':'form-select'}))