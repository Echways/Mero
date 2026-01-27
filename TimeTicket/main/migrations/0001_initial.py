import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("title", models.CharField(max_length=120, verbose_name="Название мероприятия")),
                (
                    "starts_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Начало мероприятия"
                    ),
                ),
                (
                    "ends_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Конец мероприятия"
                    ),
                ),
                (
                    "short_description",
                    models.CharField(blank=True, max_length=160, verbose_name="Краткое описание"),
                ),
                ("slogan", models.CharField(blank=True, max_length=120, verbose_name="Слоган")),
                ("description", models.TextField(blank=True, verbose_name="Описание мероприятия")),
                (
                    "min_age",
                    models.PositiveSmallIntegerField(
                        default=0, verbose_name="Минимальный возраст для посещения"
                    ),
                ),
                (
                    "ticket_image",
                    models.ImageField(
                        blank=True, null=True, upload_to="events/tickets/", verbose_name="Билет"
                    ),
                ),
                (
                    "promo_image",
                    models.ImageField(
                        blank=True, null=True, upload_to="events/promos/", verbose_name="Промо-фото"
                    ),
                ),
                (
                    "venue",
                    models.CharField(blank=True, max_length=200, verbose_name="Место проведения"),
                ),
                (
                    "base_price",
                    models.PositiveIntegerField(default=0, verbose_name="Цена билета стандарт"),
                ),
                (
                    "coffee_price",
                    models.PositiveIntegerField(default=0, verbose_name="Цена кофе-билет"),
                ),
                (
                    "dinner_price",
                    models.PositiveIntegerField(default=0, verbose_name="Цена обед-билет"),
                ),
                (
                    "vip_price",
                    models.PositiveIntegerField(default=0, verbose_name="Цена за VIP билет"),
                ),
                (
                    "host_avatar",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="events/hosts/",
                        verbose_name="Фото организатора",
                    ),
                ),
                (
                    "host_name",
                    models.CharField(blank=True, max_length=100, verbose_name="Организатор"),
                ),
                (
                    "host_email",
                    models.EmailField(
                        blank=True, max_length=100, verbose_name="Почта организатора"
                    ),
                ),
                (
                    "host_telegram",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Телеграм организатора"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["starts_at"],
            },
        ),
        migrations.CreateModel(
            name="NewUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(blank=True, null=True, verbose_name="last login"),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={"unique": "A user with that username already exists."},
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(blank=True, max_length=150, verbose_name="first name"),
                ),
                (
                    "last_name",
                    models.CharField(blank=True, max_length=150, verbose_name="last name"),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, null=True, unique=True, verbose_name="Email"
                    ),
                ),
                (
                    "mobile_phone",
                    models.CharField(blank=True, max_length=16, verbose_name="Номер телефона"),
                ),
                (
                    "middle_name",
                    models.CharField(blank=True, max_length=100, verbose_name="Отчество"),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="EventRegistration",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("first_name", models.CharField(max_length=100, verbose_name="Имя")),
                ("last_name", models.CharField(max_length=100, verbose_name="Фамилия")),
                ("email", models.EmailField(max_length=100, verbose_name="Ваша почта")),
                (
                    "ticket_type",
                    models.IntegerField(
                        choices=[
                            (1, "Билет 'Standard'"),
                            (2, "Билет с обедом"),
                            (3, "Билет с кофе"),
                            (4, "Билет 'VIP'"),
                        ],
                        default=1,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="registrations",
                        to="main.event",
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="EventVideo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "video",
                    models.FileField(
                        upload_to="events/videos/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=["mp4"]
                            )
                        ],
                    ),
                ),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="videos",
                        to="main.event",
                    ),
                ),
            ],
            options={
                "ordering": ["id"],
            },
        ),
    ]
