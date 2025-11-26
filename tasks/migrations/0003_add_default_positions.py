from django.db import migrations


def create_positions(apps, schema_editor):
    Position = apps.get_model("tasks", "Position")
    default_positions = [
        "Developer",
        "Project Manager",
        "QA",
        "Designer",
        "DevOps",
    ]
    for name in default_positions:
        Position.objects.get_or_create(name=name)


def delete_positions(apps, schema_editor):
    Position = apps.get_model("tasks", "Position")
    default_positions = [
        "Developer",
        "Project Manager",
        "QA",
        "Designer",
        "DevOps",
    ]
    Position.objects.filter(name__in=default_positions).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0002_add_default_task_types"),  # ajusta pro nome da tua migração anterior
    ]

    operations = [
        migrations.RunPython(create_positions, delete_positions),
    ]
