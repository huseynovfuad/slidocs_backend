# Generated by Django 3.2 on 2024-03-05 06:42

import ckeditor.fields
from django.db import migrations, models
import mainapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('content', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name_plural': 'About Us',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=400)),
                ('email', models.EmailField(max_length=254)),
                ('message', ckeditor.fields.RichTextField()),
                ('attach', models.FileField(blank=True, null=True, upload_to=mainapp.models.upload_to_contact)),
            ],
            options={
                'verbose_name_plural': 'Contact',
            },
        ),
        migrations.CreateModel(
            name='PrivacyPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('content', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name_plural': 'Privacy Policy',
            },
        ),
        migrations.CreateModel(
            name='RefundPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('content', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name_plural': 'Refund Policy',
            },
        ),
        migrations.CreateModel(
            name='TermCondition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('content', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name_plural': 'Term and Conditions',
            },
        ),
    ]
