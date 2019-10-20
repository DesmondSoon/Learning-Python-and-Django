from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm



class RegistrationForm(UserCreationForm):

    email = forms.EmailField(required=True)


    # name = forms.CharField (label='Name', widget=forms.TextInput(attrs={"placeholder":"Your name"}))
    class Meta:

        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save( commit=False )
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email= self.cleaned_data['email']

        if commit:
            user.save()


        return user

class EditUserProfile(UserChangeForm):

    class Meta:

        model=User

        fields =(

            'first_name',
            'last_name',
            'email',
            'password'
        )
