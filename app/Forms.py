from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    # email.widget.attrs.update({'class': 'validate', 'placeholder': 'email'})