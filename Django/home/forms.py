from  django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label="Kullanıcı Adı")
    password = forms.CharField(max_length=100, label="Parola", widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                raise forms.ValidationError("Kullanıcı Adı veya Parola yanlış !")

        return super(LoginForm, self).clean()

class registerForm(forms.ModelForm):
    username = forms.CharField(max_length=100, label="Kullanıcı Adı")
    name = forms.CharField(max_length=100, label="Adınız")
    surname = forms.CharField(max_length=100, label="Soyadınız")
    email = forms.EmailField()
    password1 = forms.CharField(max_length=100, label="Parola", widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100, label="Parola(Tekrar)", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            "username",
            "name",
            "surname",
            "email",
            "password1",
            "password2"
        ]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Parolalar Eşleşmiyor !")
        return password2


