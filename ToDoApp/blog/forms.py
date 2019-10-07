from django import forms

from .models import Articles


class ArticlesModelform (forms.ModelForm):


    class Meta:
        model = Articles
        fields =[
            'title',
            'content',
            'active',
            # 'publish_date',
        ]
