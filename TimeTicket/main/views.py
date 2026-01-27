from __future__ import annotations

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, TemplateView

from .forms import EventRegistrationForm, SignUpForm
from .models import Event, EventRegistration, EventVideo
from .permissions import staff_required
from .services.exports import build_event_registrations_csv_response
from .services.notifications import send_ticket_email
from .utils import days_until, normalize_host_name, pluralize_days


class MainView(ListView):
    model = Event
    template_name = "index.html"
    context_object_name = "events"


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profileview.html"


class ProfileEventsView(LoginRequiredMixin, ListView):
    model = Event
    template_name = "person_event.html"
    context_object_name = "events"


class ProfileEventVideosView(LoginRequiredMixin, ListView):
    model = EventVideo
    template_name = "person_event_videos.html"
    context_object_name = "videos"


class UserRegView(CreateView):
    form_class = SignUpForm
    template_name = "registration/registration.html"
    success_url = reverse_lazy("login")


class EventDetailView(DetailView):
    model = Event
    template_name = "event_detail.html"
    context_object_name = "event"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event = self.object
        hostname_clean = normalize_host_name(event.host_name)
        ticket_coffee = event.coffee_total_price
        ticket_dinner = event.dinner_total_price
        remaining_days = days_until(event.starts_at)
        if remaining_days > 0:
            start_event = pluralize_days(remaining_days)
        elif remaining_days == 0:
            start_event = "Сегодня"
        else:
            start_event = "Мероприятие прошло"
        context.update(
            {
                "start_event": start_event,
                "hostname": hostname_clean,
                "ticket_coffee": ticket_coffee,
                "ticket_dinner": ticket_dinner,
            }
        )
        return context


class EventRegistrationCreateView(CreateView):
    form_class = EventRegistrationForm
    template_name = "reg_event.html"
    success_url = reverse_lazy("event_registration")

    def form_valid(self, form):
        self.object = form.save()
        send_ticket_email(self.object)
        messages.success(self.request, "Регистрация успешно создана. Билет отправлен на почту.")
        return redirect(self.get_success_url())


@staff_required
def export_event_registrations_csv(request, pk: int):
    event = get_object_or_404(Event, pk=pk)
    registrations = EventRegistration.objects.filter(event=event)
    return build_event_registrations_csv_response(event, registrations)


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Пароль изменен успешно!")
            return redirect("passwordchange")
        messages.error(request, "Неверный ввод.")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "change_password.html", {"form": form})


def healthcheck(request):
    return JsonResponse({"status": "ok"})
