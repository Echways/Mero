from django.contrib.auth.decorators import user_passes_test


def staff_required(view):
    return user_passes_test(lambda user: user.is_active and user.is_staff)(view)
