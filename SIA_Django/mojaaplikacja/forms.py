from django import forms
from django.core.exceptions import ValidationError

class FormularzKontaktowy(forms.Form):
    imie = forms.CharField(max_length=100, label="Twoje imie")
    email = forms.EmailField(label="Twoj email")
    wiadomosc = forms.CharField(widget=forms.Textarea, label="wiadomosc")

    def clean_imie(self):
        imie = self.cleaned_data["imie"]
        if any(char.isdigit() for char in imie):
            raise forms.ValidationError("imie nie moze zawierac cyfr")
        return imie

class FormularzRejestracji(forms.Form):
    nazwa_uzytkownika = forms.CharField(max_length=50, label="Nazwa użytkownika")
    email = forms.EmailField(label="Adres e-mail")
    haslo = forms.CharField(widget=forms.PasswordInput, label="Hasło")
    potwierdz_haslo = forms.CharField(widget=forms.PasswordInput, label="Potwierdź hasło")
    akceptacja_regulaminu = forms.BooleanField(required=True, label="Akceptuję regulamin")

    def clean(self):
        cleaned_data = super().clean()
        haslo = cleaned_data.get("haslo")
        potwierdz_haslo = cleaned_data.get("potwierdz_haslo")

        if haslo and potwierdz_haslo and haslo != potwierdz_haslo:
            raise forms.ValidationError("Hasla musza byc identyczne")
        return cleaned_data

    def clean_nazwa_uzytkownika(self):
        nazwa = self.cleaned_data['nazwa_uzytkownika']
        if len(nazwa) < 5:
            raise forms.ValidationError("Nazwa uzytkownika musi mieć co najmniej 5 znaków.")
        return nazwa

    def clean(self):
        cleaned_data = super().clean()
        haslo = cleaned_data.get("haslo")
        potwierdz_haslo = cleaned_data.get("potwierdz_haslo")
        akceptacja = cleaned_data.get("akceptacja_regulaminu")

        if haslo and potwierdz_haslo and haslo != potwierdz_haslo:
            raise forms.ValidationError("Hasła nie są takie same.")

        if not akceptacja:
            raise forms.ValidationError("Musisz zaakceptować regulamin.")
