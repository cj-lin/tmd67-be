# Generated by Django 4.1.5 on 2023-02-11 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ac", "0005_rename_due_date_paymentrecord_due_time_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="paymentrecord",
            name="created_time",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="paymentrecord",
            name="updated_time",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
