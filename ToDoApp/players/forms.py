from django import forms

from .models import players


class playersform(forms.ModelForm):

    name = forms.CharField (label='Name', widget=forms.TextInput(attrs={"placeholder":"Your name"}))
    class Meta:
        model = players
        fields = [
            'name',
            'player_div',
            'player_club',

        ]
