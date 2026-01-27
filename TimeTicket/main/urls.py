from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path

from .forms import LoginForm
from .views import (
    EventDetailView,
    EventRegistrationCreateView,
    MainView,
    ProfileEventsView,
    ProfileEventVideosView,
    ProfileView,
    UserRegView,
    change_password,
    export_event_registrations_csv,
    healthcheck,
)

urlpatterns = [
    path("", MainView.as_view(), name="main"),
    path("account/profile/", ProfileView.as_view(), name="profileview"),
    path("account/signup/", UserRegView.as_view(), name="signup"),
    path(
        "account/login/",
        LoginView.as_view(authentication_form=LoginForm, template_name="registration/login.html"),
        name="login",
    ),
    path("account/", include("django.contrib.auth.urls")),
    path("account/logout/", LogoutView.as_view(), name="logout"),
    path("events/<int:pk>/", EventDetailView.as_view(), name="event_detail"),
    path("events/register/", EventRegistrationCreateView.as_view(), name="event_registration"),
    path(
        "events/<int:pk>/registrations/export/",
        export_event_registrations_csv,
        name="event_registrations_export",
    ),
    path("health/", healthcheck, name="healthcheck"),
    path("account/passwordchange/", change_password, name="passwordchange"),
    path("account/profile/events/", ProfileEventsView.as_view(), name="profileevents"),
    path(
        "account/profile/events/videos/",
        ProfileEventVideosView.as_view(),
        name="profileeventvideos",
    ),
]
