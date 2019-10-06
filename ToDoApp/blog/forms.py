from django import forms

from .models import Articles


class articlesform (forms.ModelForm):

    class meta:
        fields :[
            'title',
            'content',
            'publish_date',
        ]
