# Generated by Django 5.0.3 on 2024-03-07 20:04

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_note_color_bg_note_view_order"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="note",
            options={"verbose_name": "Note", "verbose_name_plural": "Notes"},
        ),
    ]