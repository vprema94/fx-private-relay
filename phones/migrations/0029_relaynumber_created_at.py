# Generated by Django 4.2.9 on 2024-01-31 21:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("phones", "0028_remove_relaynumber_deprecated_remaining_minutes"),
    ]

    operations = [
        migrations.AddField(
            model_name="relaynumber",
            name="created_at",
            field=models.DateTimeField(null=True),
        ),
    ]