from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Mot de passe', 'type':"text"}),
        label="Mot de passe")
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Confirme Mot de passe', 'type':"text"}),
        label="Confirmer le mot de passe")
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Nom d\'utilisateur', 'type':"text"})
    )
    email = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'email', 'type':"text"})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Les mots de passe ne correspondent pas.")

        return cleaned_data