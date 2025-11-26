from django.db import migrations


def create_task_types(apps, schema_editor):
    TaskType = apps.get_model("tasks", "TaskType")
    default_types = [
        "Bug",
        "New feature",
        "Breaking change",
        "Refactoring",
        "QA",
    ]
    for name in default_types:
        TaskType.objects.get_or_create(name=name)


def delete_task_types(apps, schema_editor):
    TaskType = apps.get_model("tasks", "TaskType")
    default_types = [
        "Bug",
        "New feature",
        "Breaking change",
        "Refactoring",
        "QA",
    ]
    TaskType.objects.filter(name__in=default_types).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_task_types, delete_task_types),
    ]
