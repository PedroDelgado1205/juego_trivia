from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.html import format_html

class UserForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'input',
            'placeholder': 'Nombre de usuario',
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'input',
            'placeholder': 'Contraseña',
        })
    )

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={
            'class': 'input',
            'placeholder': 'Nombre de usuario',
        })
        self.fields['username'].widget = forms.TextInput(attrs={
            'class': 'input',
            'placeholder': 'Nombre de usuario',
        })
        self.fields['username'].widget.attrs['class'] += ' has-icons-left'
        self.fields['password'].widget.attrs['class'] += ' has-icons-left'

    def as_p(self):
        return format_html(
            '<div class="field">'
            '<div class="control has-icons-left">'
            '{username}'
            '<span class="icon is-small is-left"><i class="fa-solid fa-user"></i></span>'
            '</div>'
            '</div>'
            '<div class="field">'
            '<div class="control has-icons-left">'
            '{password}'
            '<span class="icon is-small is-left"><i class="fa-solid fa-lock"></i></span>'
            '</div>'
            '</div>',
            username=self['username'],
            password=self['password'],
        )
