# Generated by Django 4.1.2 on 2023-02-09 09:54

import django.db.models.deletion
import django_fsm
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "state",
                    django_fsm.FSMField(default="unpaid", max_length=50),
                ),
                ("amount", models.IntegerField(default=0)),
                (
                    "created_time",
                    models.DateTimeField(auto_now_add=True, null=True),
                ),
                (
                    "updated_time",
                    models.DateTimeField(auto_now=True, null=True),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TicketProduct",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("chinese_name", models.CharField(max_length=100)),
                ("english_name", models.CharField(max_length=100)),
                ("price", models.IntegerField(blank=True, null=True)),
                ("category", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Ticket",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                (
                    "last_name",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                (
                    "club",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.club",
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ac.order",
                    ),
                ),
                (
                    "ticket_product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ac.ticketproduct",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.IntegerField(verbose_name=0)),
                (
                    "order",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product_items",
                        to="ac.order",
                    ),
                ),
                (
                    "ticket_product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ac.ticketproduct",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PaymentRecord",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("due_date", models.DateTimeField(blank=True, null=True)),
                (
                    "description",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "merchant_id",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("is_paid", models.BooleanField(default=False)),
                (
                    "order",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="ac.order",
                    ),
                ),
            ],
        ),
    ]
