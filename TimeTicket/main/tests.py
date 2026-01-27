from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .forms import EventRegistrationForm
from .models import Event


class EventViewsTest(TestCase):
    def setUp(self):
        self.event = Event.objects.create(
            title="Test Event",
            starts_at=timezone.now(),
            ends_at=timezone.now(),
        )

    def test_home_page(self):
        response = self.client.get(reverse("main"))
        self.assertEqual(response.status_code, 200)

    def test_event_detail(self):
        response = self.client.get(reverse("event_detail", args=[self.event.pk]))
        self.assertEqual(response.status_code, 200)


class EventValidationTest(TestCase):
    def test_event_end_before_start(self):
        event = Event(
            title="Bad Event",
            starts_at=timezone.now(),
            ends_at=timezone.now() - timezone.timedelta(days=1),
        )
        with self.assertRaises(ValidationError):
            event.clean()


class RegistrationFormTest(TestCase):
    def test_registration_past_event_invalid(self):
        event = Event.objects.create(
            title="Past Event",
            starts_at=timezone.now() - timezone.timedelta(days=2),
            ends_at=timezone.now() - timezone.timedelta(days=1),
        )
        form = EventRegistrationForm(
            data={
                "first_name": "Ivan",
                "last_name": "Petrov",
                "email": "test@example.com",
                "event": event.id,
                "ticket_type": 1,
            }
        )
        self.assertFalse(form.is_valid())
