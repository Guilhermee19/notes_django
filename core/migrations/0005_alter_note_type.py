# Generated by Django 5.0.3 on 2024-03-07 20:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0004_note_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="note",
            name="type",
            field=models.CharField(
                blank=True,
                choices=[("NOTES", "notes"), ("CHECK", "check"), ("LIST", "list")],
                default="NOTES",
                max_length=255,
                null=True,
            ),
        ),
    ]
