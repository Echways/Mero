from django.core.exceptions import ValidationError


def validate_event_dates(starts_at, ends_at):
    if starts_at and ends_at and ends_at < starts_at:
        raise ValidationError({"ends_at": "Дата окончания должна быть позже начала."})
