import csv

from django.http import HttpResponse


def build_event_registrations_csv_response(event, registrations):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = f'attachment; filename="event-{event.pk}-registrations.csv"'

    writer = csv.writer(response)
    writer.writerow(["Имя", "Фамилия", "Email", "Тип билета", "Дата регистрации"])
    for reg in registrations:
        writer.writerow(
            [
                reg.first_name,
                reg.last_name,
                reg.email,
                reg.get_ticket_type_display(),
                reg.created_at.isoformat(),
            ]
        )

    return response
