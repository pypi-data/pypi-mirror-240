# Generated by Django 3.2.10 on 2022-02-17 11:15

import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("dcim", "0005_device_local_context_schema"),
        ("extras", "0013_default_fallback_value_computedfield"),
        ("nautobot_device_lifecycle_mgmt", "0006_cvelcm_vulnerabilitylcm"),
    ]

    operations = [
        migrations.CreateModel(
            name="SoftwareImageLCM",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("created", models.DateField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "_custom_field_data",
                    models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
                ),
                ("image_file_name", models.CharField(max_length=100)),
                ("download_url", models.URLField(blank=True)),
                ("image_file_checksum", models.CharField(blank=True, max_length=256)),
                ("default_image", models.BooleanField(default=False)),
                (
                    "device_types",
                    models.ManyToManyField(
                        blank=True,
                        related_name="_nautobot_device_lifecycle_mgmt_softwareimagelcm_device_types_+",
                        to="dcim.DeviceType",
                    ),
                ),
                (
                    "inventory_items",
                    models.ManyToManyField(
                        blank=True,
                        related_name="_nautobot_device_lifecycle_mgmt_softwareimagelcm_inventory_items_+",
                        to="dcim.InventoryItem",
                    ),
                ),
                (
                    "object_tags",
                    models.ManyToManyField(
                        blank=True,
                        related_name="_nautobot_device_lifecycle_mgmt_softwareimagelcm_object_tags_+",
                        to="extras.Tag",
                    ),
                ),
                (
                    "software",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="software_images",
                        to="nautobot_device_lifecycle_mgmt.softwarelcm",
                    ),
                ),
                ("tags", taggit.managers.TaggableManager(through="extras.TaggedItem", to="extras.Tag")),
            ],
            options={
                "verbose_name": "Software Image",
                "ordering": ("software", "default_image", "image_file_name"),
                "unique_together": {("image_file_name", "software")},
            },
        ),
    ]
