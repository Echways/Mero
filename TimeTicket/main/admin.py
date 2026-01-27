from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Event, EventRegistration, EventVideo, NewUser


class EventVideoInline(admin.StackedInline):
    model = EventVideo
    extra = 0


class EventRegistrationInline(admin.StackedInline):
    model = EventRegistration
    extra = 0


class EventAdmin(admin.ModelAdmin):
    inlines = [EventVideoInline, EventRegistrationInline]
    list_display = ("title", "starts_at", "ends_at", "venue")
    search_fields = ("title", "venue", "host_name")
    list_filter = ("starts_at",)


@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "event", "ticket_type", "created_at")
    list_filter = ("ticket_type", "created_at")
    search_fields = ("last_name", "first_name", "email", "event__title")


userfields = list(UserAdmin.fieldsets)
userfields[1] = (
    "Личная информация",
    {"fields": ("first_name", "last_name", "middle_name", "email", "mobile_phone")},
)
UserAdmin.fieldsets = tuple(userfields)


@admin.register(EventVideo)
class EventVideoAdmin(admin.ModelAdmin):
    list_display = ("event", "video")


admin.site.register(Event, EventAdmin)
admin.site.register(NewUser, UserAdmin)
