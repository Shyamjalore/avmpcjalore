# Generated by Django 4.2.5 on 2023-10-01 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avmform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('fathername', models.CharField(max_length=120)),
                ('batch', models.IntegerField()),
                ('passout', models.IntegerField()),
                ('mobile', models.CharField(max_length=10)),
                ('presentaddress', models.TextField()),
                ('permanentaddress', models.TextField()),
                ('occupation', models.CharField(max_length=250)),
                ('workaddress', models.TextField()),
                ('qualification', models.CharField(default=None, max_length=50)),
                ('DOB', models.DateField()),
                ('whatsapp', models.CharField(blank=True, default=None, max_length=12, null=True)),
                ('interest', models.TextField(blank=True, default=None, null=True)),
                ('achievement', models.TextField(blank=True, default=None, null=True)),
                ('organization', models.TextField(blank=True, default=None, null=True)),
                ('improvement', models.TextField(blank=True, default=None, null=True)),
                ('suggestion', models.TextField(blank=True, default=None, null=True)),
                ('image', models.ImageField(default=None, upload_to='uploads/')),
            ],
        ),
    ]
