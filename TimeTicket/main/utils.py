from django.utils import timezone


def pluralize_days(days: int) -> str:
    forms = ["день", "дня", "дней"]
    if days % 10 == 1 and days % 100 != 11:
        form_index = 0
    elif 2 <= days % 10 <= 4 and (days % 100 < 10 or days % 100 >= 20):
        form_index = 1
    else:
        form_index = 2
    return f"{days} {forms[form_index]}"


def normalize_host_name(value: str) -> str:
    return " ".join(value.replace("_", "-").split("-"))


def days_until(value) -> int:
    return (value - timezone.now()).days
