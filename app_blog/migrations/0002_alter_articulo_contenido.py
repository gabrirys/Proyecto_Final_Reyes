# Generated by Django 4.2.3 on 2023-08-15 13:46

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='contenido',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
