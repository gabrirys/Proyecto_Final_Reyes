# Generated by Django 4.2.3 on 2023-08-16 13:17

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('subtitulo', models.CharField(max_length=200)),
                ('contenido', ckeditor.fields.RichTextField()),
                ('fecha_publicado', models.DateTimeField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='images_blog/')),
                ('pie_imagen', models.CharField(max_length=300)),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articulos_creados', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
