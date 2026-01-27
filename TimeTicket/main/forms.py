from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.utils import timezone

from .models import Event, EventRegistration, NewUser


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    last_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    middle_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    mobile_phone = forms.CharField(
        max_length=16, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password1 = forms.CharField(
        max_length=100, widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    password2 = forms.CharField(
        max_length=100, widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    username = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = NewUser
        fields = (
            "username",
            "first_name",
            "last_name",
            "middle_name",
            "email",
            "mobile_phone",
        )


class LoginForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        self.fields["username"].widget.attrs.update({"class": "login-input"})
        self.fields["password"].widget.attrs.update({"class": "login-input"})


class EventRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    last_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    email = forms.EmailField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = EventRegistration
        fields = ["first_name", "last_name", "email", "event", "ticket_type"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["event"] = forms.ModelChoiceField(
            queryset=Event.objects.all(),
            widget=forms.Select(attrs={"class": "select-purchase"}),
        )
        self.fields["ticket_type"] = forms.ChoiceField(
            choices=EventRegistration.TicketType.choices,
            widget=forms.Select(attrs={"class": "select-purchase"}),
        )

    def clean(self):
        cleaned = super().clean()
        event = cleaned.get("event")
        if event and event.ends_at and event.ends_at < timezone.now():
            raise ValidationError("Регистрация на прошедшее событие недоступна.")
        return cleaned
