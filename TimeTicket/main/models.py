from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.models import F, Q
from django.urls import reverse
from django.utils import timezone

from .validators import validate_event_dates


class Event(models.Model):
    title = models.CharField("Название мероприятия", max_length=120)
    starts_at = models.DateTimeField("Начало мероприятия", default=timezone.now)
    ends_at = models.DateTimeField("Конец мероприятия", default=timezone.now)
    short_description = models.CharField("Краткое описание", max_length=160, blank=True)
    slogan = models.CharField("Слоган", max_length=120, blank=True)
    description = models.TextField("Описание мероприятия", blank=True)
    min_age = models.PositiveSmallIntegerField("Минимальный возраст для посещения", default=0)
    ticket_image = models.ImageField(
        "Билет",
        upload_to="events/tickets/",
        blank=True,
        null=True,
    )
    promo_image = models.ImageField(
        "Промо-фото",
        upload_to="events/promos/",
        blank=True,
        null=True,
    )
    venue = models.CharField("Место проведения", max_length=200, blank=True)

    base_price = models.PositiveIntegerField("Цена билета стандарт", default=0)
    coffee_price = models.PositiveIntegerField("Цена кофе-билет", default=0)
    dinner_price = models.PositiveIntegerField("Цена обед-билет", default=0)
    vip_price = models.PositiveIntegerField("Цена за VIP билет", default=0)

    host_avatar = models.ImageField(
        "Фото организатора",
        upload_to="events/hosts/",
        blank=True,
        null=True,
    )
    host_name = models.CharField("Организатор", max_length=100, blank=True)
    host_email = models.EmailField("Почта организатора", max_length=100, blank=True)
    host_telegram = models.CharField("Телеграм организатора", max_length=100, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["starts_at"]
        constraints = [
            models.CheckConstraint(
                check=Q(min_age__gte=0),
                name="event_min_age_non_negative",
            ),
            models.CheckConstraint(
                check=Q(base_price__gte=0)
                & Q(coffee_price__gte=0)
                & Q(dinner_price__gte=0)
                & Q(vip_price__gte=0),
                name="event_prices_non_negative",
            ),
            models.CheckConstraint(
                check=Q(ends_at__gte=F("starts_at")),
                name="event_ends_after_starts",
            ),
        ]

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("event_detail", kwargs={"pk": self.pk})

    def clean(self):
        validate_event_dates(self.starts_at, self.ends_at)

    @property
    def coffee_total_price(self) -> int:
        return self.base_price + self.coffee_price

    @property
    def dinner_total_price(self) -> int:
        return self.base_price + self.dinner_price


class EventVideo(models.Model):
    video = models.FileField(
        upload_to="events/videos/",
        validators=[FileExtensionValidator(allowed_extensions=["mp4"])],
    )
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="videos")

    class Meta:
        ordering = ["id"]

    def __str__(self) -> str:
        return f"{self.event.title} video #{self.pk}"


class EventRegistration(models.Model):
    class TicketType(models.IntegerChoices):
        STANDARD = 1, "Билет 'Standard'"
        DINNER = 2, "Билет с обедом"
        COFFEE = 3, "Билет с кофе"
        VIP = 4, "Билет 'VIP'"

    first_name = models.CharField("Имя", max_length=100)
    last_name = models.CharField("Фамилия", max_length=100)
    email = models.EmailField("Ваша почта", max_length=100)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="registrations")
    ticket_type = models.IntegerField(choices=TicketType.choices, default=TicketType.STANDARD)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name} — {self.event.title}"


class NewUser(AbstractUser):
    email = models.EmailField("Email", unique=True, blank=True, null=True)
    mobile_phone = models.CharField("Номер телефона", max_length=16, blank=True)
    middle_name = models.CharField("Отчество", max_length=100, blank=True)

    def __str__(self) -> str:
        return self.username
