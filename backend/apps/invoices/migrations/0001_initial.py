# Generated by Django 3.1.7 on 2021-03-17 05:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('team', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('client', '0002_auto_20210316_2305'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.IntegerField(default=1)),
                ('client_name', models.CharField(max_length=255)),
                ('client_email', models.CharField(max_length=255)),
                ('client_org_number', models.CharField(blank=True, max_length=255, null=True)),
                ('client_address1', models.CharField(blank=True, max_length=255, null=True)),
                ('client_address2', models.CharField(blank=True, max_length=255, null=True)),
                ('client_zipcode', models.CharField(blank=True, max_length=255, null=True)),
                ('client_place', models.CharField(blank=True, max_length=255, null=True)),
                ('client_country', models.CharField(blank=True, max_length=255, null=True)),
                ('client_contact_person', models.CharField(blank=True, max_length=255, null=True)),
                ('client_contact_reference', models.CharField(blank=True, max_length=255, null=True)),
                ('sender_reference', models.CharField(blank=True, max_length=255, null=True)),
                ('invoice_type', models.CharField(choices=[('invoice', 'Invoice'), ('credit_note', 'Credit note')], default='invoice', max_length=20)),
                ('due_days', models.IntegerField(default=14)),
                ('is_sent', models.BooleanField(default=False)),
                ('gross_amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('vat_amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('net_amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('discount_amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='client.client')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_invoices', to=settings.AUTH_USER_MODEL)),
                ('is_credit_for', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='invoices.invoice')),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modified_invoices', to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='team.team')),
            ],
            options={
                'verbose_name': 'Invoice',
                'verbose_name_plural': 'Invoices',
            },
        ),
    ]
