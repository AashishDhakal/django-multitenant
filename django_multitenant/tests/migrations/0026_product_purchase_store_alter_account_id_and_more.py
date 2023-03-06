# Generated by Django 4.0 on 2023-02-20 17:41

from django.db import migrations, models
import django.db.models.deletion
import django_multitenant.fields
import django_multitenant.mixins


class Migration(migrations.Migration):

    dependencies = [
        ("tests", "0025_data_load"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
            ],
            bases=(django_multitenant.mixins.TenantModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name="Purchase",
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
            ],
            bases=(django_multitenant.mixins.TenantModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name="Store",
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
                ("name", models.CharField(max_length=50)),
                ("address", models.CharField(max_length=255)),
                ("email", models.CharField(max_length=50)),
            ],
            options={
                "abstract": False,
            },
            bases=(django_multitenant.mixins.TenantModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name="Transaction",
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
                ("date", models.DateField()),
                (
                    "product",
                    django_multitenant.fields.TenantForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="tests.product"
                    ),
                ),
                (
                    "purchase",
                    django_multitenant.fields.TenantForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tests.purchase",
                    ),
                ),
                (
                    "store",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="tests.store"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(django_multitenant.mixins.TenantModelMixin, models.Model),
        ),
        migrations.AddField(
            model_name="purchase",
            name="product_purchased",
            field=models.ManyToManyField(
                through="tests.Transaction", to="tests.Product"
            ),
        ),
        migrations.AddField(
            model_name="purchase",
            name="store",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="tests.store"
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="store",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="tests.store"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="purchase",
            unique_together={("id", "store")},
        ),
        migrations.AlterUniqueTogether(
            name="product",
            unique_together={("id", "store")},
        ),
    ]