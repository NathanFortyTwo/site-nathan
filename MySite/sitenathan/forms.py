from django import forms 

class TweetForm(forms.Form):
    text = forms.CharField(label = '',max_length=280,widget=forms.TextInput(attrs={
        'autocomplete':'off'
    }))