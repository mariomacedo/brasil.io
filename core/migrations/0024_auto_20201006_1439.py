# Generated by Django 3.1.1 on 2020-10-06 17:39

from django.db import migrations


def ensure_filtering_fields_config(apps, schema_editor):
    Table = apps.get_model("core.Table")

    for table in Table.objects.all():
        fields = table.field_set.all()

        fields_maps = {f.name: f for f in fields}
        for fieldname in table.filtering_fields or []:
            field = fields.get(name=fieldname)
            if not field.frontend_filter:
                field.frontend_filter = True
                field.save()
                print(f"{table.dataset.slug}.{table.name}.{fieldname} atualizado como frontend_filter")


def rollback(*args, **kwargs):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0023_auto_20201006_1435"),
    ]

    operations = [migrations.RunPython(ensure_filtering_fields_config, rollback)]